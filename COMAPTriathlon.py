"""
COMAOPtriathlon.py
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset
from ggame import ImageAsset, PolygonAsset, Frame, Sound, SoundAsset, TextAsset
import time
import random

"""
sl=int(input("Length of swim (in kilometers)"))
bl=int(input("Length of bike (in kilometers)"))
rl=int(input("Length of run (in kilometers)"))
fprostart=int(input("Time female pros start (in minutes after male pro start)"))
mprestart=int(input("Time male premiere start (in minutes after male pro start)"))
fprestart=int(input("Time female premiere start (in minutes after male pro start)"))
mopenstart=int(input("Time male open start (in minutes after male pro start)"))
fopenstart=int(input("Time female open start (in minutes after male pro start)"))
clystart=int(input("Time Clydsedale start (in minutes after male pro start)"))
athstart=int(input("Time Athena start (in minutes after male pro start)"))
"""
#average swim speeds
mpros=0
fpros=0
mpres=0
fpres=0
mos=0
fos=0
cyls=0
aths=0
#average t1 times
mprot1=0
fprot1=0
mpret1=0
fpret1=0
mot1=0
fot1=0
cylt1=0
atht1=0
#average bike speeds
mprob=0
fprob=0
mpreb=0
fpreb=0
mob=0
fob=0
cylb=0
athb=0
#average t2 times
mprot2=0
fprot2=0
mpret2=0
fpret2=0
mot2=0
fot2=0
cylt2=0
atht2=0
#average run speeds
mpror=0
fpror=0
mprer=0
fprer=0
mor=0
for1=0
cylr=0
athr=0


# colors
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xffa500, 1.0)
skin =Color(0xFCD15B, 1.0)
wall=Color(0xE8E8E8, 1.0)
orange=Color(0xFFa500,1.0)
platc=Color(0xB9BDBB,1.0)
gooy=Color(0xCDF238,1.0)
white=Color(0xFFFFFF,1.0)
darkblue=Color(0x052099,1.0)

# lines
thinline= LineStyle(1, black)
thickline= LineStyle(5, black)
thickliner= LineStyle(5, red)
thicklineb= LineStyle(5, blue)
thickishline= LineStyle(2.5, black)
noline= LineStyle(0, black)
portalline= LineStyle(1, blue)
portalline2= LineStyle(1, orange)

class start(Sprite):
    asset = RectangleAsset(.5,100,thinline,black)
    def __init__(self, position):
        super().__init__(start.asset, position)
        self.vx=0
        self.vy=0
        self.setImage(0)
        
class finish(Sprite):
    asset = RectangleAsset(.5,100,thinline,black)
    def __init__(self, position):
        super().__init__(finish.asset, position)
        self.vx=0
        self.vy=0
        self.setImage(1)


class mpro(Sprite):
    asset = RectangleAsset(1,1,thicklineb,black)
    def __init__(self, position):
        super().__init__(mpro.asset, position)
        self.vx=0
        self.vy=0
    def step(self):
        self.x += 0
        self.y += 0
        
class fpro(Sprite):
    asset = RectangleAsset(1,1,thickliner,black)
    def __init__(self, position):
        super().__init__(fpro.asset, position)
        self.vx=0
        self.vy=0
    def step(self):
        self.x += 0
        self.y += 0
        
class triathlon(App):
    asset = ImageAsset("images/spritesforathletes.jpg", Frame(0,0,55,50), 8, 'horizontal')
    def __init__(self, width, height):
        super().__init__(width, height)
        mpro((0,0))
        fpro((0,0))
        start((100,0))
        finish((500,0))
    def step(self):
        for mp in self.getSpritesbyClass(mpro):
            mp.step()
        for fp in self.getSpritesbyClass(fpro):
            fp.step()
            
myapp = triathlon(1000,750)
myapp.run()
