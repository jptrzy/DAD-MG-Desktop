
from engine import *
from classes import *
import threading, time, sys, json, os, pygame

print('run')
pygame.init()

class Game:

       sC = True

       width = 700
       height = 700

       screen = pygame.display.set_mode((width,height))

       windows = []

       wC = Window(height=200, width=200, title="Console")
       windows.append(wC)
       console = []
       cField = ''
       pChars = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',',','.','!','1','2','3','4','5','6','7','8','9','0',' ','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

       wAPC = Window(height=120, width=200, title="APC")
       wAPCP = 0
       windows.append(wAPC)
       pCCW = [] #Window, what list(0-pC/1-mGC), id character

       playerHaracters = []
       nonPlayerHaracters = []

       run = 1

       def loadHaracters(self, path):
              tab = []
              for i in [f for f in os.listdir(path) if f.endswith('.json')]:
                     f = open(path+"/"+i,"r")
                     tab.append(Character())
                     for k, v in json.loads(f.read()).items():
                            tab[len(tab)-1][k] = v
                     f.close()
              return tab

       def update(self):
              lB1 = 0
              B1 = 0
              while(self.run):
                     for e in pygame.event.get():
                            if(e.type == pygame.QUIT):
                                   self.run = 0
                     lB1 = B1
                     B1 = pygame.mouse.get_pressed()[0]
                     pos = pygame.mouse.get_pos()
                     if(B1 == lB1 and B1 != 0):
                            self.B1Pressed(pos[0], pos[1])
                     elif(B1 > lB1):
                            self.B1Down(pos[0], pos[1])
                     elif(B1 < lB1):
                            self.B1Up(pos[0], pos[1])


       def drawRect(self, x,y,width,height,fill):
              pygame.draw.rect(self.screen, pygame.Color(fill), pygame.Rect(x,y,width,height))
       def drawText(self, x, y, font, size, text, color, bGColor):
              if(bGColor != None):
                     bGColor = pygame.Color(bGColor)
              self.screen.blit(pygame.font.SysFont(font, size).render(text, True, pygame.Color(color), bGColor), (x,y))


       def draw(self):
              while(self.run):
                     self.screen.fill((0,0,0))
                     self.drawText(0, 0, 'Times', 15, "C", "#ffffff", "#000000")
                     if(self.sC):
                            listOfPCCW = [el[0] for el in self.pCCW]
                            for w in reversed(self.windows):





                                   if(w.see):
                                          if(w.click):
                                                 self.drawRect(w.x+10, w.y-20, w.width-10, 20, '#00b300')
                                                 self.drawText(w.x+25, w.y-20, 'Times', 17, w.title, '#ffffff', '#00b300')
                                          else:
                                                 self.drawRect(w.x+10, w.y-20, w.width-10, 20, '#00cd00')
                                                 self.drawText(w.x+25, w.y-20, 'Times', 17, w.title, '#ffffff', '#00cd00')
                                          self.drawRect(w.x, w.y, w.width, +w.height, '#5f5f5f')
                                          self.drawRect(w.x, w.y-20, 10, 20, '#0000ff')
                                          if(w == self.wAPC):
                                                 for i in range(0,5):
                                                        if(len(self.playerHaracters) > i+5*self.wAPCP):
                                                               self.drawRect(self.wAPC.x, self.wAPC.y+20*i, w.width, 20, '#0000ff')
                                                               self.drawText(self.wAPC.x, self.wAPC.y+20*i, "Times", 17, self.playerHaracters[i+5*self.wAPCP].name, "#ffffff", "#0000ff")
                                                 self.drawRect(self.wAPC.x, self.wAPC.y+self.wAPC.height-20, 20, 20, '#ff0000')
                                                 self.drawRect(self.wAPC.x+self.wAPC.width-20, self.wAPC.y+self.wAPC.height-20, 20, 20, '#ff0000')
                                          elif(w == self.wC):
                                                 for i, v in enumerate(self.console):
                                                        pass
                                                        self.drawText(w.x, w.y+20*i,"Times", 17, v, "#ffffff", None)
                                                 self.drawText(w.x, w.y+w.height-20,"Times", 17, self.cField+"|", "#ffffff", None)


                                          elif(w in listOfPCCW):
                                                 c = self.pCCW[listOfPCCW.index(w)][1]
                                                 for i, v in enumerate([attr for attr in dir(c) if not callable(getattr(c, attr)) and not attr.startswith("__")]):
                                                        pass
                                                        self.drawText(w.x+1, w.y+20*i,"Times", 17, (v +" "+ c[v]), "#ffffff", None)
                                                 self.drawRect(w.x+10, w.y-20, 10, 20, '#ff0000')
                            for i in range(0,len(self.windows)):
                                   self.drawRect(i*self.width/len(self.windows), self.height-20, self.width/len(self.windows), 20, fill='#ff0000')

                            pygame.display.flip()
                            self.sC = False
                            time.sleep(1/60)

       def B1Down(self, x, y):
              if(x>self.wAPC.x and x<self.wAPC.x+20 and y>self.wAPC.y+self.wAPC.height-20 and y<self.wAPC.y+self.wAPC.height):
                     if(self.wAPCP>0):
                            self.wAPCP-=1
              elif(x>self.wAPC.x+self.wAPC.width-20 and x<self.wAPC.x+self.wAPC.width and y>self.wAPC.y+self.wAPC.height-20 and y<self.wAPC.y+self.wAPC.height):
                     if((self.wAPCP+1)*5<len(self.playerHaracters)):
                            self.wAPCP+=1
              elif(x>self.wAPC.x and x<self.wAPC.x+self.wAPC.width and y>self.wAPC.y and y<self.wAPC.y+self.wAPC.height-20):
                     for i in range(0,5):
                            if(len(self.playerHaracters) > i+5*self.wAPCP and y>self.wAPC.y+20*i and y<self.wAPC.y+20*(i+1)):
                                   nW = Window(title="CC-"+self.playerHaracters[self.wAPCP*5+i].name, width=200, height=200)
                                   self.windows.append(nW)
                                   self.pCCW.append([nW, self.playerHaracters[self.wAPCP*5+i]])
                                   tab = []
                                   for i, k in enumerate([attr for attr in dir(self.playerHaracters[self.wAPCP*5+i]) if not callable(getattr(self.playerHaracters[self.wAPCP*5+i], attr)) and not attr.startswith("__")]):
                                          tab.append([20*i,20*i,20,200,False,k])
                                   nW['Box']=tab

                     for ww in self.windows:
                            ww.click = 0
                     self.wAPC.click=1
              else:
                     listOfPCCW = [el[0] for el in self.pCCW]
                     for w in self.windows:
                            if(x>w.x+20 and x<w.x+w.width and y>w.y-20 and y<w.y):
                                   w.move = True
                                   w.dx = x - w.x
                                   w.dy = y - w.y
                                   break
                            elif(x>w.x and x<w.x+10 and y>w.y-20 and y<w.y):
                                   w.see=0
                            elif(x>w.x+10 and x<w.x+20 and y>w.y-20 and y<w.y and w in listOfPCCW):
                                   self.pCCW.remove(self.pCCW[listOfPCCW.index(w)])
                                   self.windows.remove(w)
                                   break
                     for w in self.windows:
                            if(x>w.x and x<w.x+w.width and y>w.y and y<w.y+w.height):
                                   for ww in self.windows:
                                          ww.click = 0
                                   w.click=1
                                   break
              self.sC = True
       def B1Up(self,  x, y): 
              for w in self.windows:
                     w.move = False
              self.sC = True
       def B1Pressed(self,  x, y):
              for w in self.windows:
                     if(w.move):
                            w.x = x - w.dx
                            w.y = y - w.dy
              self.sC = True
       def pressButton(self, e):
              if(self.wC.click):
                     print(e)
                     if(e.keycode == 13):
                            self.console.append(self.cField)
                            self.cField = ''
                     elif(e.keycode == 8):
                             self.cField=self.cField[:-1]
                     elif(e.char in self.pChars):
                            self.cField+=e.char
              if(e.keycode==27):
                     self.run = 0
                     sys.exit(0)
                     exit(0)
              self.sC = 1
       def __init__(self):
              self.playerHaracters=self.loadHaracters("data/playerHaracters")

              #self.root.bind("<Button-1>", self.ButtonDown)
              #self.root.bind("<ButtonRelease-1>", self.ButtonUp)
              #self.root.bind("<B1-Motion>", self.Button1Move)
              #self.root.bind("<Key>", self.pressButton)
              
             
              threading.Thread(target=self.draw).start()
              #threading.Thread(target=self.update).start()
              self.update()
g = Game()