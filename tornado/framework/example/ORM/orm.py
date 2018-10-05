from .tornadoMySQL import TornadoMySQL

class ORM(object):
	def save(self):
		tableName = (self.__class__.__name__).lower()
		fieldsStr = valuesStr = "("
		for field in self.__dict__:
			fieldsStr += (field + ",")
			if isinstance(self.__dict__[field], str):
				valuesStr += ("'" + self.__dict__[field] + "',")
			else:
				valuesStr += (str(self.__dict__[field]) + ",")
		fieldsStr = fieldsStr[:len(fieldsStr) - 1] + ")"
		valuesStr = valuesStr[:len(valuesStr) - 1] + ")"
		sql = "insert into " + tableName + " " + fieldsStr + " values " + valuesStr
		db = TornadoMySQL()
		db.insert(sql)

	def delete(self):
		pass

	def update(self):
		pass

	@classmethod
	def all(cls):
		tableName = (cls.__name__).lower()
		sql = "select * from " + tableName
		db = TornadoMySQL()
		print(sql)
		return db.get_all_obj(sql, tableName)

	@classmethod
	def filter(cls):
		pass
