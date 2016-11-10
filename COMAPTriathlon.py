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
        
class finish(Sprite):
    asset = RectangleAsset(.5,100,thinline,black)
    def __init__(self, position):
        super().__init__(finish.asset, position)
        self.vx=0
        self.vy=0

class mpro(Sprite):
    asset = RectangleAsset(1,1,thicklineb,black)
    def __init__(self, position):
        super().__init__(mpro.asset, position)
        self.vx=0
        self.vy=0
    def step(self):
        self.x += 1
        self.y += 2
        
class fpro(Sprite):
    asset = RectangleAsset(1,1,thickliner,black)
    def __init__(self, position):
        super().__init__(fpro.asset, position)
        self.vx=0
        self.vy=0
    def step(self):
        self.x += 1
        self.y += 1
        
class triathlon(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        mpro((0,0))
        fpro((0,0))
        start((100,0))
        finish((1000,0))
    def step(self):
        for mp in self.getSpritesbyClass(mpro):
            mp.step()
        for fp in self.getSpritesbyClass(fpro):
            fp.step()
            
myapp = triathlon(1000,750)
myapp.run()
