

class Window:
	see = True

	click = 0
	move = False
	dx = 0
	dy = 0

	x = 0
	y = 20
	width = 100
	height = 100

	title = 'name'


	def __init__(self, **args):
		for i in args:
			self[i] = args[i]
	def __setitem__(self, key, value):
		self.__dict__[key] = value
	def __getitem__(self, key):
		return self.__dict__[key]