
class character:
	page = 0

	box = [
	[['imie']],
	[['pD'],['poziom']],
	[['klasa'],['rasa']],
	[],
	[['sila'],['budowa']],
	[['rzuObr'],['rzuObr']],
	[['atletyka']],
	[],
	[['zrecznosc'],['charyzma']],
	[['rzuObr'],['rzuObr']],
	[['akrobatyka'],['graAktorsa']],
	[['ukradkowosc'],['oszukiwanie']],
	[['zreczna dlon'],['przekonywanie']],
	[[],['zastraszanie']],
	[],
	[['roztropnosc'],['intelekt']],
	[['rzuObr'],['rzuObr']],
	[['medycyna'],['arkana']],
	[['osfajanie'],['przeszukiwanie']],
	[['spostrzegawczosc'],['historia']],
	[['survival'],['natura']],
	[['wyczuciePobudek'],['religia']],
	[],
	[['ekwipunek']],
	[['ekwipunek', {'repeat': 1}]]


	]

	def draw(self, x, y):
		width = self.window.width
		height = self.window.height
		for yy in range(0, len(self.box)):
			for xx in range(0, len(self.box[yy])):
				if(len(self.box[yy])>0 and len(self.box[yy][xx])>0):
					lenght = int(42/len(self.box[yy]))
					if(len(self.box[yy][xx])>1 and self.box[yy][xx][1].get('repeat', None) != None):
						minu = len(self.box[yy][xx][0]+': ')
						self.drawText(x+xx*width/len(self.box[yy]),y+yy*20, 'Pixeled.ttf', 28, (str(self.che[self.box[yy][xx][0]]))[lenght*(self.box[yy][xx][1]['repeat'])-minu:lenght*(self.box[yy][xx][1]['repeat']+1)-minu], '#ffffff')
					else:
						self.drawText(x+xx*width/len(self.box[yy]),y+yy*20, 'Pixeled.ttf', 28, (self.box[yy][xx][0]+': '+str(self.che[self.box[yy][xx][0]]))[:lenght], '#ffffff')


	def __init__(self, args):
		for i in args:
			self[i] = args[i]
		self.window.title = 'pHCL'
		self.window.width = 480
		self.window.height = len(self.box)*20

	def __setitem__(self, key, value):
		self.__dict__[key] = value
	def __getitem__(self, key):
		return None