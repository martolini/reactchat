from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone as dtimezone
from apps.chat.models import Channel, Message

import pytz
import json
import time

class Clique(models.Model):
	name = models.CharField(max_length=20)

	def __unicode__(self):
		return self.name

class Startup(models.Model):
	name = models.CharField(max_length=30)
	clique = models.ForeignKey(Clique, related_name='startups')

	def __unicode__(self):
		return self.name

class ProfileManager(BaseUserManager):
	def create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('Profile needs an email address')
		user = self.model(
			email=self.normalize_email(email),
			display_name=email.split('@')[0],
			**extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password):
		user = self.create_user(email,
			password=password,
			is_superuser=True,
			is_staff=True)
		user.save(using=self._db)
		return user

class Profile(AbstractBaseUser, PermissionsMixin):
	timezone = models.CharField(max_length=100, choices = [(x, x) for x in pytz.common_timezones], default='Europe/Oslo')
	email = models.EmailField(max_length=255, unique=True)
	display_name = models.CharField(max_length=50)
	is_staff = models.BooleanField(default=False)
	date_joined = models.DateTimeField(default=dtimezone.now)
	startup = models.ForeignKey(Startup, related_name='profiles', null=True)
	channels = models.ManyToManyField(Channel, through='chat.Membership', null=True)
	USERNAME_FIELD = 'email'

	objects = ProfileManager()

	def get_full_name(self):
		return self.email

	def get_short_name(self):
		return self.email

	def __unicode__(self):
		return self.email

	def get_initial_channels_as_json(self):
		channels = json.dumps(list(self.startup.clique.channels.all().values('id', 'name')))
		return channels

	def get_initial_messages_as_json(self):
		messages = Message.objects.filter(channel__in=self.startup.clique.channels.all()).select_related('channel', 'user').only('id', 'text', 'channel_id', 'channel__name', 'user__display_name')
		messages = [
			{
				'id': message.id,
				'username': message.user.display_name,
				'channel_id': message.channel_id,
				'text': message.text,
				'channel_name': message.channel.name,
				'created_at': time.mktime(message.created_at.timetuple())*1000,
			} for message in messages]
		return json.dumps(messages)