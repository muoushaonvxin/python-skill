import tornado.web
from views import index
import config
import os

class Application(tornado.web.Application):
    def __init__(self):
	handlers = [
	    (r'/', index.IndexHandler),
	    (r'/sunck', index.SunckHandler),
	    (r'(.*)$', tornado.web.StaticFileHandler, {"path": os.path.join(config.BASE_DIRS, "static/html"), 
                                                       "default_filename": "index.html"})
	]
	super(Application, self).__init__(handlers, **config.settings)
