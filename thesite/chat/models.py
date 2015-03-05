from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import json
from django.utils import timezone
import time

class Clique(models.Model):
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class Channel(models.Model):
	name = models.CharField(max_length=20)
	clique = models.ForeignKey(Clique, related_name='chatrooms')

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
		print time.mktime(self.created_at.timetuple())*1000
		return json.dumps(dict(
			id = self.id,
			username = self.user.username,
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

class Startup(models.Model):
	name = models.CharField(max_length=30)
	clique = models.ForeignKey(Clique, related_name='startups')

	def __unicode__(self):
		return self.name

class Profile(AbstractUser):
	startup = models.ForeignKey(Startup, related_name='profiles', null=True)
	channels = models.ManyToManyField(Channel, through='Membership', null=True)

	def get_initial_channels_as_json(self):
		channels = json.dumps(list(self.channels.all().values('id', 'name')))
		return channels

	def get_initial_messages_as_json(self):
		messages = Message.objects.filter(channel__in=self.channels.all()).select_related('channel', 'user').only('id', 'text', 'channel_id', 'channel__name', 'user__username')
		messages = [
			{
				'id': message.id,
				'username': message.user.username,
				'channel_id': message.channel_id,
				'text': message.text,
				'channel_name': message.channel.name,
				'created_at': time.mktime(message.created_at.timetuple())*1000,
			} for message in messages]
		return json.dumps(messages)

class Membership(models.Model):
	user = models.ForeignKey(Profile)
	channel = models.ForeignKey(Channel)
	is_admin = models.BooleanField(default=False)