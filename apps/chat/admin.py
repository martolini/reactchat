from django.contrib import admin
from .models import Channel, Message, Membership

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
