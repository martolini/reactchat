from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import Startup, Clique, Profile

@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

@admin.register(Clique)
class CliqueAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')

class ProfileChangeForm(UserChangeForm):
	username = forms.CharField(required=False)
	class Meta:
		model = Profile
		fields = ('email', 'password', 'display_name', 'startup',)

@admin.register(Profile)
class ProfileAdmin(UserAdmin):
	form = ProfileChangeForm
	# The forms to add and change user instances

	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('email', 'is_staff', 'is_superuser')
	list_filter = ('is_superuser','is_staff')
	fieldsets = (
		(None, {'fields': ('email', 'password', 'display_name', 'startup')}),
	)
	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password','startup')}
		),
	)
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()