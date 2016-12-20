"""
MMRadar.py
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset
from ggame import ImageAsset, PolygonAsset, Frame, Sound, SoundAsset, TextAsset
import time
import random
import math

SCREEN_WINDOWX = 1000
SCREEN_WINDOWY = 1000


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
thinliner= LineStyle(1, red)
thin1line=LineStyle(2,black)
thickline= LineStyle(5, black)
thickliner= LineStyle(5, red)
thicklineb= LineStyle(5, blue)
thickishline= LineStyle(2.5, black)
noline= LineStyle(0, black)
portalline= LineStyle(1, blue)
portalline2= LineStyle(1, orange)

class dish(Sprite):
    asset = EllipseAsset(50,5,thin1line,white)
    def __init__(self, position):
        super().__init__(dish.asset, position)
        self.vx=0
        self.vy=0
        self.rotation=-1
        
class signal(Sprite):
    asset = EllipseAsset(50,5,thinliner,white)
    def __init__(self, position):
        super().__init__(signal.asset, position)
        self.vx=0
        self.vy=0
        self.rotation=-1
    def step(self):
        self.x += 2
        self.y -= 1.5
        
class plane(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')
    def __init__(self, position):
        super().__init__(plane.asset, position)
        self.vx=0
        self.rotation= math.pi/2
        
class radar(App):
    asset = ImageAsset("images/spritesforathletes.jpg", Frame(0,0,55,50), 8, 'horizontal')
    def __init__(self, width, height):
        super().__init__(width, height)
        dish((100,450))
        signal((102,450))
        plane((900,100))
        Sprite(LineAsset(1000,1,thinline),(0,500))
    def step(self):
        for sig in self.getSpritesbyClass(signal):
            sig.step()
       
myapp = radar(SCREEN_WINDOWX,SCREEN_WINDOWY)
myapp.run()
