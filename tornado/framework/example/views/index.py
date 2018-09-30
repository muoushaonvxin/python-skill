from tornado.web import RequestHandler
import json

class IndexHandler(RequestHandler):
	def get(self, *args, **kwargs):
		self.write("lucky guy")

class SunckHandler(RequestHandler):
	def get(self, *args, **kwargs):
		self.write("lucky guy")
