import os

BASE_DIRS = os.path.dirname(__file__)

options = {
	"port": 9000,	
}

settings = {
	"static_path": os.path.join(BASE_DIRS, "static"),
	"template_path": os.path.join(BASE_DIRS, "template"),
	"debug": True,
	"autoreload": True	
}
