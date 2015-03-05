from django.conf import settings
from django.utils.importlib import import_module
from tornado import web, ioloop
from sockjs.tornado import SockJSRouter
from django.core.management.base import BaseCommand

class Command(BaseCommand):

	def handle(self, **options):
		module_name, cls_name = settings.SOCKJS_HANDLER.rsplit('.', 1)
		module = import_module(module_name)
		cls = getattr(module, cls_name)
		channel = getattr(settings, 'SOCKJS_CHANNEL', '/echo')
		router = SockJSRouter(cls, channel)
		app_settings = {
			'debug': settings.DEBUG
		}

		port = 8888
		app = web.Application(router.urls, **app_settings)
		app.listen(port, no_keep_alive=True)
		print 'Running tornado on port %d with channel %s' % (port, channel)
		try:
			ioloop.IOLoop.instance().start()
		except KeyboardInterrupt:
			pass