from django.shortcuts import render

def index(request, template='chat/index.html'):
	return render(request, template)
