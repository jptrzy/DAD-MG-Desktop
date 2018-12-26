class Character:
	def __init__(self, **args):
		self['box'] = [
		[0,0,20,'imie'],
		[0,20,40,'pD'],
		]


		self["imie"] = "Imie"
		self["klasaIPoziom"] = ""
		self["rasa"] = ""
		self["pD"] = "ssssssssssssssssssssssssssssss"


		for i in args:
			self[i] = args[i]



	def __setitem__(self, key, value):
		self.__dict__[key] = value
	def __getitem__(self, key):
		return self.__dict__[key]