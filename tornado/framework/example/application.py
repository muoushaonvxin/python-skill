import tornado.web
from views import index
import config

class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r'/', index.IndexHandler),
			(r'/sunck', index.SunckHandler)
		]
		super(Application, self).__init__(handlers, **config.settings)
