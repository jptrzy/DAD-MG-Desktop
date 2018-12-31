import pygame

class Screen:

	width = 700
	height = 700

	screen = pygame.display.set_mode((width,height))

	def drawRect(self,x,y,width,height,fill="#ffffff"):
		pygame.draw.rect(self.screen, pygame.Color(fill), pygame.Rect(x,y,width,height))

	def __init__(self, **args):
		for i in args:
			self[i] = args[i]
	def __setitem__(self, key, value):
		self.__dict__[key] = value
	def __getitem__(self, key):
		try:
			return self.__dict__[key]
		except:
			return None

class Window:
	see = True

	destructible = 0
	selected = 0

	x = 0
	y = 20
	width = 100
	height = 100

	move = False
	dx = 0
	dy = 0

	title = 'name'

########
	cBD = 0 #can be delete

	click = 0



	def __init__(self, **args):
		for i in args:
			self[i] = args[i]
	def __setitem__(self, key, value):
		self.__dict__[key] = value
	def __getitem__(self, key):
		try:
			return self.__dict__[key]
		except:
			return None