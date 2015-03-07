from django.shortcuts import render
from django.conf import settings

def index(request, template='chat/index.html'):
	if settings.DEV:
		url = 'http://localhost:3456/chat'
	else:
		url = 'http://msroed.net:3456/chat'
	return render(request, template, {'url': url})
