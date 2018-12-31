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

cc = __import__('test')
c = getattr(cc, 'test')
a = c()
aa = c()
print(a.s)
a.s = 1
print(a.s)
print(aa.s)