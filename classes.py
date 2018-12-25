class Character:
	def __init__(self, **args):
		self["name"] = "Name"
		self["discription"] = "Dis"
		for i in args:
			self[i] = args[i]



	def __setitem__(self, key, value):
		self.__dict__[key] = value
	def __getitem__(self, key):
		return self.__dict__[key]