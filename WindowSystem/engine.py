import pygame, time

class Screen:

	width = 700
	height = 700

	screen = pygame.display.set_mode((width,height))
	#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

	def drawRect(self,x,y,width,height,fill="#ffffff"):
		pygame.draw.rect(self.screen, pygame.Color(fill), pygame.Rect(x,y,width,height))
	def drawText(self, x, y, font, size, text, color, bGColor=None):
		if(bGColor != None):
			bGColor = pygame.Color(bGColor)
		self.screen.blit(pygame.font.SysFont(font, size).render(text, True, pygame.Color(color), bGColor), (x,y))

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
	see = 1

	destructible = 1
	selected = 0

	x = 0
	y = 20
	width = 100
	height = 100

	move = 0
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

class Clock:
	c = ''

	def __init__(self):
		self.c = time.time()

	def deltaTime(self):
		dt = time.time() - self.c
		self.c+=dt
		return int(dt*1000)