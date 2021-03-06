"""
MMRadar.py
"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, LineAsset
from ggame import ImageAsset, PolygonAsset, Frame, Sound, SoundAsset, TextAsset
import time
import random
import math

'''
weather = int(input("Any weather? (1 for custom, 0 for none)"))
if weather == 1:
    rainny = int(input("Rain? (1 for rain, 0 for none)"))
    if rainny == 1:
        ar = .2
    else:
        ar = 0
    foggy = int(input("Fog? (1 for fog, 0 for none)"))
    if foggy == 1:
        af = .2
    else:
        af = 0
    snowy = int(input("Snow? (1 for snow, 0 for none)"))
    if snowy == 1:
        afs = .2
    else:
        afs = 0

else:
    rainny = 0
    ar = 0
    foggy = 0
    af = 0
    snowy = 0
    afs = 0

ss = 0-(int(input("Signal Strength (whole numbers only)")))
cpx = int(input("X Location of Plane (100-1000)"))
cpy = int(input("Y Location of Plane (0-450)"))
#numplanes = int(input("Number of planes in air? (for future use)"))
'''

rainny = 0
foggy = 0
snowy = 0
cpx = 750
cpy = 100
ss = 0
ar = 0
af = 0
afs = 0

SCREEN_WINDOWX = 1000
SCREEN_WINDOWY = 1000
speed = 3
precipitation = 1


# colors
red = Color(0xff0000, 1.0)
red9 = Color(0xff0000, 0.9)
red8 = Color(0xff0000, 0.8)
red7 = Color(0xff0000, 0.7)
red6 = Color(0xff0000, 0.6)
red5 = Color(0xff0000, 0.5)
red4 = Color(0xff0000, 0.4)
red3 = Color(0xff0000, 0.3)
red2 = Color(0xff0000, 0.2)
red1 = Color(0xff0000, 0.1)


green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
skyblue = Color(0x87CEEB, 1.0)
black = Color(0x000000, 1.0)
orange = Color(0xffa500, 1.0)
sun = Color(0xFFCC33,1.0)
skin =Color(0xFCD15B, 1.0)
wall=Color(0xE8E8E8, 1.0)
orange=Color(0xFFa500,1.0)
platc=Color(0xB9BDBB,1.0)
gooy=Color(0xCDF238,1.0)
white=Color(0xFFFFFF,1.0)
fog=Color(0xFFFFFF,0.4)
darkblue=Color(0x052099,1.0)

# lines
thinline= LineStyle(1, black)
thinliner= LineStyle(1, red)
thinlinesb=LineStyle(1, skyblue)
thinlinedb=LineStyle(1, darkblue)
thinlinewa=LineStyle(1, wall)
thinlinew= LineStyle(1, white)
thinlinesun = LineStyle(2, sun)
thin1line=LineStyle(2,black)
thickline= LineStyle(5, black)
thickliner= LineStyle(5, red)
thicklineb= LineStyle(5, blue)
thickishline= LineStyle(2.5, black)
noline= LineStyle(0, black)
portalline= LineStyle(1, blue)
portalline2= LineStyle(1, orange)

class dish(Sprite):
    asset = EllipseAsset(5,50,thin1line,white)
    def __init__(self, position):
        super().__init__(dish.asset, position)
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.vx=0
        self.vy=0
        self.rotation = math.atan2(450-cpy,cpx-100)
        
class rain(Sprite):
    asset = RectangleAsset(1,1,thinlinedb,darkblue)
    def __init__(self, position):
        super().__init__(rain.asset, position)
        self.vx=0
        self.vy=0
        self.rotation=0
    def step(self):
        if self.y <= 500:
            self.y += random.randrange(2,7)
        if self.y >= 500:
            self.y = 0

class snow(Sprite):
    asset = RectangleAsset(1,1,thinlinew,white)
    def __init__(self, position):
        super().__init__(snow.asset, position)
        self.vx=0
        self.vy=0
        self.rotation=0
    def step(self):
        if self.y <= 500:
            self.y += random.randrange(2,7)
        if self.y >= 500:
            self.y = 0
            
class fog(Sprite):
    asset = RectangleAsset(500,500,thinlinewa,wall)
    def __init__(self, position):
        super().__init__(fog.asset, position)
        self.vx=0
        self.vy=0
            
class signal(Sprite):
    #asset = EllipseAsset(50,5,thinliner,red)
    asset = ImageAsset("images/Signalstrength-1.png", Frame(0,0,(959/29),300), 29, 'horizontal')
    def __init__(self, position):
        super().__init__(signal.asset, position)
        self.scale = .35
        #self.rotation=.55
        self.rotation = math.atan2(450-cpy,cpx-100)
        self.a = 0
        self.i = ss
        self.s = 0
        self.t = 0
        self.g = 0
        self.fxcenter= .5
        self.fycenter = 0.5
        self.speed = 2
        #self.distance = math.sqrt(((cpx-100)^2)+((450-cpy)^2))
    def step(self):
        if self.a == 0:
            self.i += .2 + afs + af + ar
            if self.i >= 0:
                self.setImage((self.i))
            else:
                self.setImage(0)
            #self.x += 3*speed
            #self.y -= 1.5*speed
            self.x += ((cpx-100)/100)*(self.speed)
            self.y -= ((450-cpy)/100)*(self.speed)
            if self.x >= cpx:
                self.a = 1
                if self.i >= 0:
                    self.i *= 2
                else:
                    self.i = ss - self.i
            if self.i >= 28:
                self.setImage(28)
                self.a = 2
                Sprite(TextAsset(text="Signal Is Not Strong Enough", width = 200, align = 'center', style = '30px Arial', fill=black),(350,350))
                print(self.t)
        if self.a == 1:
            self.i += 0.2 - afs - af - ar
            if self.i >= 0:
                self.setImage((self.i))
            else:
                self.setImage(0)
            self.x -= ((cpx-100)/100)*(self.speed)
            self.y += ((450-cpy)/100)*(self.speed)
            if self.x <= 100 and self.i <= 28:
                self.a = 2
                self.s = 1
            if self.i >= 28:
                self.setImage(28)
                self.a = 2
                Sprite(TextAsset(text="Signal Is Not Strong Enough", width = 200, align = 'center', style = '30px Arial', fill=black),(350,350))
                print(self.t)
        if self.a == 2:
            #Sprite(TextAsset(text = "Time Elapsed:", width = 200, align = 'center', style = '30px Arial', fill=black),(350,150))
            #Sprite(TextAsset(text= self.t, width = 200, align = 'center', style = '30px Arial', fill=black),(550,150))
            self.x = 72
            self.y = 415
            self.setImage(28)
            if self.s == 1:
                Sprite(TextAsset(text="Signal Is Strong Enough", width = 200, align = 'center', style = '30px Arial', fill=black),(350,350))
                print(self.t)

class plane(Sprite):
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", Frame(227,0,292-227,125), 1, 'vertical')
    #asset = ImageAsset("https://github.com/averywallis/Radar/blob/master/images/plane.png")
    def __init__(self, position):
        super().__init__(plane.asset, position)
        self.rotation = math.pi/2
        self.fxcenter = 0.5
        self.fycenter = 0.5
class plane1(Sprite):
    asset = CircleAsset(5,thinline,black)
    def __init__(self, position):
        super().__init__(plane1.asset, position)
        
class radar(App):
    asset = ImageAsset("images/spritesforathletes.jpg", Frame(0,0,55,50), 8, 'horizontal')
    def __init__(self, width, height):
        super().__init__(width, height)
        dishtxt = TextAsset(text="Radar Dish", width = 200, align = 'center', style = '10px Arial', fill=black)
        signaltxt = TextAsset(text="Signal (moving)", width = 200, align = 'center', style = '10px Arial', fill=red)
        #suntxt = TextAsset(text="Random Sun", width = 200, align = 'center', style = '10px Arial', fill=black)
        #planetxt = TextAsset(text="Plane (will idealy move)", width = 200, align = 'center', style = '10px Arial', fill=black)
        Sprite(RectangleAsset(1000,500,thinlinesb,skyblue),(0,0))
        dish((100,450))
        Sprite(dishtxt,(45,450))
        signal((100,450))
        Sprite(signaltxt,(75,375))
        plane((cpx,cpy))
        #plane1((cpx,cpy))
        #plane((900,72))
        #Sprite(planetxt,(865,25))
        if rainny == 1:
            for x in range(0,31):
                rain((random.randrange(400,800),random.randrange(0,500)))
        if snowy == 1:
            for x in range(0,31):
                snow((random.randrange(400,800),random.randrange(0,500)))
        if foggy == 1:
            fog((200,0))
                
        Sprite(LineAsset(1000,1,thinline),(0,500))
        Sprite(CircleAsset(20,thinlinesun,sun),(200,100))
        #Sprite(suntxt,(170,90))
    def step(self):
        for sig in self.getSpritesbyClass(signal):
            sig.step()
        for rain1 in self.getSpritesbyClass(rain):
            rain1.step()
        for snow1 in self.getSpritesbyClass(snow):
            snow1.step()
       
myapp = radar(SCREEN_WINDOWX,SCREEN_WINDOWY)
myapp.run()
