from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'username')

@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'clique')

@admin.register(Clique)
class CliqueAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
	'''
		Admin View for Chatroom
	'''
	list_display = ('id', 'name', 'clique')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
	list_display = ('id', 'user')

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'channel')
