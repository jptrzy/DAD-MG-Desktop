from engine import *
import threading, sys, json, os, pygame, random, time

pygame.init()

class main:

	screen = Screen()

	options = {
	'windowDeleteButtonBackColor':'#ff0000',
	'windowDeleteButtonTextColor':'#ffffff',
	'windowCloseButtonBackColor':'#0000ff',
	'windowCloseButtonTextColor':'#ffffff',
	'windowSelectTitleBackColor':'#00a300',
	'windowSelectTitleTextColor':'#ffffff',
	'windowTitleBackColor':'#00e600',
	'windowTitleTextColor':'#ffffff',
	'windowBackColor':'#444444'
	}
	windows = []

	run = 1

	def newWindow(self, st, **args):
		def getWindows():
			return self.windows

		nW = Window()


		args['window']=nW
		args['getWindows']=getWindows
		args['newWindow']=self.newWindow
		args['drawRect']=self.screen.drawRect
		args['drawText']=self.screen.drawText


		nW['mainClass'] =getattr(getattr(__import__('app.'+st), st), st)(args)
		self.windows.append(nW)
		return 0


	def events(self):
		lB1 = [0,0,0]
		B1 = [0,0,0]
		while(self.run):
			for e in pygame.event.get():
			    if(e.type == pygame.QUIT):
			           self.run = 0
			           sys.exit()
			    if(e.type == pygame.KEYDOWN):
			           self.pressButton(e.key)


			for i in range(0,3):
				lB1[i] = B1[i]
				B1[i] = pygame.mouse.get_pressed()[i]
				pos = pygame.mouse.get_pos()
				if(B1[i] == lB1[i] and B1[i] != 0):
				    self.B1Pressed(B1, pos[0], pos[1])
				elif(B1[i] > lB1[i]):
				    self.B1Down(B1, pos[0], pos[1])
				elif(B1[i] < lB1[i]):
				    self.B1Up(lB1, pos[0], pos[1])
			time.sleep(1/50)
			



	def update(self):
		c = Clock()
		while(self.run):
			c.deltaTime()
			for w in self.windows:
				if(w['mainClass']!=None and hasattr(w['mainClass'], 'update')):
					if(w['mainClass'].update()):
						self.windows.remove(w)
			time.sleep(1-c.deltaTime()/1000)
		return 0

	def graphicUpdate(self):
		def drawWindow(w, x, y):
			pygame.draw.lines(self.screen.screen, pygame.Color('#000000'), False, [[x-1, y-20], [x-1, y+w.height], [x+w.width, y+w.height], [x+w.width, y-21], [x-1, y-21]], 2)
			if(w.selected):
				self.screen.drawRect(x,y-20,w.width,20,self.options['windowSelectTitleBackColor'])
			else:
				self.screen.drawRect(x,y-20,w.width,20,self.options['windowTitleBackColor'])
			self.screen.drawRect(x,y-20,10,20,self.options['windowCloseButtonBackColor'])
			if(w.destructible):
				self.screen.drawRect(x+10,y-20,10,20,self.options['windowDeleteButtonBackColor'])
			self.screen.drawRect(x,y,w.width,w.height,self.options['windowBackColor'])
			self.screen.drawText(x+20, y-20, 'Times', 17, w.title, self.options['windowTitleTextColor'])
		while self.run:
			self.screen.screen.fill((0,0,0))
			for w in reversed(self.windows):
				if(w.see):
					x = w.x
					y = w.y
					drawWindow(w,x,y)
					if(w['mainClass']!=None and hasattr(w['mainClass'], 'draw')):
						w['mainClass'].draw(x, y)
			time.sleep(1/30)

			pygame.display.flip()
		return 0

	def pressButton(self, keycode):
		for w in self.windows:
			if(w.selected):
				if(w['mainClass']!=None and hasattr(w['mainClass'], 'keyDown')):
					threading.Thread(target=w['mainClass'].keyDown, args=(chr(keycode))).start()
					return 0
				return 0
		return 0

	def B1Down(self, num, x, y):
		for w in self.windows:
			if(x>w.x and x<w.x+10 and y>w.y-20 and y<w.y):
				w.see=0
				return 0
			elif(x>w.x+10 and x<w.x+20 and y>w.y-20 and y<w.y and w.destructible):
				self.windows.remove(w)
				return 0
			elif(x>w.x and x<w.x+w.width and y>w.y-20 and y<w.y):
				for ww in self.windows:
					ww.selected=0
				w.selected = 1
				if(w['mainClass']!=None and hasattr(w['mainClass'], 'buttonDown')):
					threading.Thread(target=w['mainClass'].buttonDown, args=(num,x-w.x,y-w.y)).start()
				w.dx = w.x - x
				w.dy = w.y - y
				w.move=1
				return 0
			elif(x>w.x and x<w.x+w.width and y>w.y and y<w.y+w.height):
				for ww in self.windows:
					ww.selected=0
				w.selected = 1
				if(w['mainClass']!=None and hasattr(w['mainClass'], 'buttonDown')):
					threading.Thread(target=w['mainClass'].buttonDown, args=(num,x-w.x,y-w.y)).start()
				return 0
		return 0
	def B1Up(self, num, x, y):
		for w in self.windows:
			w.move=0
			if(w.selected):
				if(w['mainClass']!=None and hasattr(w['mainClass'], 'buttonUp')):
					threading.Thread(target=w['mainClass'].buttonUp, args=(num,x-w.x,y-w.y)).start()

		return 0
	def B1Pressed(self, num, x, y):
		for w in self.windows:
			if(w.selected):
				if(w['mainClass']!=None and hasattr(w['mainClass'], 'buttonPress')):
					threading.Thread(target=w['mainClass'].buttonPress, args=(num,x-w.x,y-w.y)).start()
			if(w.move):
				w.x = x+w.dx
				w.y = y+w.dy
				return 0
		return 0


	def __init__(self):

		self.newWindow('test')
		

		threading.Thread(target=self.graphicUpdate).start()
		threading.Thread(target=self.update).start()
		self.events()
		input()


main = main()