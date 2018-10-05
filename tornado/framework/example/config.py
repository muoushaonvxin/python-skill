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

mysql = {
	"host": "127.0.0.1",
	"user": "root",
	"passwd": "root",
	"dbName": "test"	
}
