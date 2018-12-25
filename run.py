
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

       ck = Window(cBD=1)
       ck['character'] = Character()
       windows.append(ck)

       wC = Window(height=200, width=200, title="Console")
       windows.append(wC)
       console = []
       cField = ''
       pChars = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',',','.','!','1','2','3','4','5','6','7','8','9','0',' ','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']

       wAPC = Window(height=120, width=200, title="APC")
       wAPC["wAPCP"] = 0
       windows.append(wAPC)

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
                     print(self.sC)
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

       def draw(self):
              def drawRect(x,y,width,height,fill):
                     pygame.draw.rect(self.screen, pygame.Color(fill), pygame.Rect(x,y,width,height))
              def drawText(x, y, font, size, text, color, bGColor):
                     if(bGColor != None):
                            bGColor = pygame.Color(bGColor)
                     self.screen.blit(pygame.font.SysFont(font, size).render(text, True, pygame.Color(color), bGColor), (x,y))
              def drawWindow(w):
                     if(w.click):
                            drawRect(w.x+10, w.y-20, w.width-10, 20, '#00b300')
                     else:
                            drawRect(w.x+10, w.y-20, w.width-10, 20, '#00cd00')
                     drawText(w.x+25, w.y-20, 'Times', 17, w.title, '#ffffff', None)
                     drawRect(w.x, w.y, w.width, +w.height, '#5f5f5f')
                     drawRect(w.x, w.y-20, 10, 20, '#0000ff')

                     if(w.cBD):
                            drawRect(w.x+10, w.y-20, 10, 20, '#ff0000')

                     if(w == self.wAPC):
                            for i in range(0,5):
                                   if(len(self.playerHaracters) > i+5*self.wAPC["wAPCP"]):
                                          drawRect(self.wAPC.x, self.wAPC.y+20*i, w.width, 20, '#0000ff')
                                          drawText(self.wAPC.x, self.wAPC.y+20*i, "Times", 17, self.playerHaracters[i+5*self.wAPC["wAPCP"]].name, "#ffffff", "#0000ff")
                            drawRect(self.wAPC.x, self.wAPC.y+self.wAPC.height-20, 20, 20, '#ff0000')
                            drawRect(self.wAPC.x+self.wAPC.width-20, self.wAPC.y+self.wAPC.height-20, 20, 20, '#ff0000')
                     elif(w == self.wC):
                            for i, v in enumerate(self.console):
                                   drawText(w.x, w.y+20*i,"Times", 17, v, "#ffffff", None)
                            drawText(w.x, w.y+w.height-20,"Times", 17, self.cField+"|", "#ffffff", None)
                     elif(w["character"] != None):
                            for i, v in enumerate([attr for attr in dir(w["character"]) if not callable(getattr(w["character"], attr)) and not attr.startswith("__")]):
                                   drawText(w.x+1, w.y+20*i,"Times", 17, (v +" "+ w["character"][v]), "#ffffff", None)



              while(self.run):
                     self.screen.fill((0,0,0))
                     if(self.sC):
                            for w in reversed(self.windows):
                                   if(w.see):
                                          drawWindow(w)
                            for i in range(0,len(self.windows)):
                                   if(i%2==0):
                                          drawRect(i*self.width/len(self.windows), self.height-20, self.width/len(self.windows), 20, fill='#ff0000')
                                   else:
                                          drawRect(i*self.width/len(self.windows), self.height-20, self.width/len(self.windows), 20, fill='#aa0000')
                                   drawText(i*self.width/len(self.windows), self.height-20,"Times", 17, self.windows[i].title, "#ffffff", None)

                            pygame.display.flip()
                            self.sC = False
                            time.sleep(1/60)

       def B1Down(self, x, y):
              def end():
                     self.sC = True
                     print(self.sC)
                     return 0

              for ww in self.windows:
                                   ww.click = 0
              for w in self.windows:
                     if(x>w.x and x<w.x+10 and y>w.y-20 and y<w.y): #press see button
                            w.see = 0
                            return end()
                     elif(x>w.x+10 and x<w.x+20 and y>w.y-20 and y<w.y and w.cBD):
                            self.windows.remove(w)
                            return end()
                     elif(x>w.x and x<w.x+w.width and y>w.y-20 and y<w.y):
                            w.click = 1
                            w.move = 1
                            w.dx = x - w.x
                            w.dy = y - w.y
                            return end()
                     elif(x>w.x and x<w.x+w.width and y>w.y and y<w.y+w.height):
                            w.click = 1
                            if(w == self.wAPC):
                                   if(x>w.x and x<w.x+20 and y>w.y+w.height-20 and y<w.y+w.height):
                                          if(w["wAPCP"]>0):
                                                 w["wAPCP"]-=1
                                          return end()
                                   elif(x>w.x+w.width-20 and x<w.x+w.width and y>w.y+w.height-20 and y<w.y+w.height):
                                          if((w["wAPCP"]+1)*5<len(self.playerHaracters)):
                                                 w["wAPCP"]+=1
                                          return end()
                                   for i in range(0,5):
                                          if(len(self.playerHaracters) > i+5*w["wAPCP"] and y>w.y+20*i and y<w.y+20*(i+1)):
                                                 nW = Window(title=self.playerHaracters[w["wAPCP"]*5+i].name, width=200, height=200, cBD=1)
                                                 nW['character'] = self.playerHaracters[w["wAPCP"]*5+i]
                                                 tab = []
                                                 for i, k in enumerate([attr for attr in dir(self.playerHaracters[w["wAPCP"]*5+i]) if not callable(getattr(self.playerHaracters[w["wAPCP"]*5+i], attr)) and not attr.startswith("__")]):
                                                        tab.append([20*i,20*i,20,200,False,k])
                                                 nW['Box']=tab
                                                 self.windows.append(nW)
                                                 return end()
                            return end()
              return end()
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
