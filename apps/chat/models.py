from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import json
from django.utils import timezone
import time

class Channel(models.Model):
	name = models.CharField(max_length=20)
	clique = models.ForeignKey('profiles.Clique', related_name='channels')

	def __unicode__(self):
		return self.name

	def as_json(self):
		return json.dumps(dict(
			id = self.id,
			name = self.name,
			))

class Message(models.Model):
	created_at = models.DateTimeField(default=timezone.now)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='messages')
	channel = models.ForeignKey(Channel, related_name='messages')
	text = models.TextField()

	def as_json(self):
		return json.dumps(dict(
			id = self.id,
			username = self.user.display_name,
			channel_id = self.channel_id,
			text = self.text,
			created_at = time.mktime(self.created_at.timetuple())*1000
			)
		)

	@staticmethod
	def from_json(data):
		data = json.loads(data)
		m = Message.objects.create(user_id=data['user_id'], txt=data['txt'], channel_id=json['chatroom_id'])
		return m

class Membership(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	channel = models.ForeignKey(Channel)
	is_admin = models.BooleanField(default=False)