from ORM.orm import ORM

class Students(ORM):
	def __init__(username,password):
		self.username = username
		self.password = password
