from sockjs.tornado import SockJSRouter, SockJSConnection
from django.utils.importlib import import_module
from django.conf import settings
from django.contrib.auth import get_user, get_user_model
import json
from .models import Message, Profile

engine = import_module(settings.SESSION_ENGINE)
session_cookie_name = settings.SESSION_COOKIE_NAME

class ChatHandler(SockJSConnection):
	clients = set()

	def get_user_from_data(self,data):
		class Dummy(object):
			pass
		req = Dummy()
		session_key = str(data.get_cookie(session_cookie_name)).split('=')[-1]
		req.session = engine.SessionStore(session_key)
		return get_user(req)

	def on_message(self, message):
		message = json.loads(message)
		channel = message['channelID']
		text = message['text']
		m = Message.objects.create(channel_id=channel, user=self.user, text=text)
		data = {'type': 'message', 'message':m.as_json()}
		self.broadcast(self.clients, data)

	def on_open(self, data):
		user = self.get_user_from_data(data=data)
		if not user.is_authenticated():
			self.close()
			return
		self.user = user
		self.clients.add(self)
		self.send_initial_data()

	def send_initial_data(self):
		self.send(
			{
				'type': 'initial_data',
				'channels': self.user.get_initial_channels_as_json(),
				'messages': self.user.get_initial_messages_as_json()
			}
		)

	def on_close(self, data):
		self.clients.remove(self)