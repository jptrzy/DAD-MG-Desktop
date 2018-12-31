import time, json

class Character:
	def __init__(self, **args):
		self["imie"] = "Imie"
		self["klasa"] = ""
		self["poziom"] = ""
		self["rasa"] = ""
		self["pD"] = ""
		self["ekwipunek"] = "jest w nim wielki miecz ghulina wielkiego zaklety przez drogiego i noszony prze za mnie trzeciego"


		for i in args:
			self[i] = args[i]



	def __setitem__(self, key, value):
		self.__dict__[key] = value 
	def __getitem__(self, key):
		try:
			return self.__dict__[key]
		except:
			return ''


class test:

	lis = [Character(),Character(),Character(),Character(),Character(),Character()]
	page = 0
	close = 0

	def draw(self, x, y):
		for i in range(0, 5):
			if(len(self.lis)>self.page*5+i):
				self.drawRect(x,y+20*i,self.window.width,20,fill="#007700")
				self.drawText(x,y+20*i, 'Pixeled.ttf', 28, self.lis[5*self.page+i].imie, '#ffffff')
		self.drawRect(x,y+self.window.height-20,20,20,fill="#00aa00")
		self.drawRect(x+self.window.width-20,y+self.window.height-20,20,20,fill="#00aa00")

	def update(self):
		#print(__name__)
		return self.close 
	def keyDown(self, char):#chr(keycode) to char #ord
		return 0 
	def buttonDown(self, num, x, y):
		if(num[0]):
			if(x>0 and x<20 and y>self.window.height-20 and y<self.window.height):
				if(self.page > 0):
					self.page-=1
				return 0
			elif(x>self.window.width-20 and x<self.window.width and y>self.window.height-20 and y<self.window.height):
				if(self.page*5<len(self.lis)):
					self.page+=1
				return 0
			else:
				for i in range(0, 5):
					if(x>0 and x<self.window.width and y>20*i and y<20*(i+1)):
						print(i)
						self.newWindow('character',che=self.lis[5*self.page+i])
						return 0
		return 0
	def __init__(self, args):
		for i in args:
			self[i] = args[i]
		self.window.title = 'pHCL'
		self.window.width = 200
		self.window.height = 120

	def __setitem__(self, key, value):
		self.__dict__[key] = value
	def __getitem__(self, key):
		return None