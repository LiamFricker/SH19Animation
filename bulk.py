import pygame, sys, random, string, math
from pygame.locals import *

pygame.init()
screen_width = 419
screen_height = 386

screen = pygame.display.set_mode([screen_width, screen_height])
fontObj0 = pygame.font.Font('freesansbold.ttf', 20)
fontObj1 = pygame.font.Font('freesansbold.ttf', 30)
fontObj = pygame.font.Font('freesansbold.ttf', 40)
font4 = pygame.font.Font('freesansbold.ttf', 96)
font0 = pygame.font.Font('freesansbold.ttf', 128)
font3 = pygame.font.Font('freesansbold.ttf', 200)
font1 = pygame.font.Font('freesansbold.ttf', 300)
font2 = pygame.font.Font('freesansbold.ttf', 450)
clock = pygame.time.Clock()
BLACK = (  0,   0,   0)
GRAY  = (211, 211, 211)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
RORANGE = (255, 100, 0)
DRED =  (205,  50,   0)
BLUE =  (  0,   0, 255)
SBLUE = (  0, 191, 255)
YELLOW = (255, 255,  0)
LIME  = (173, 255,  47)
GREEN = (  0, 255,   0)
ORANGE = (255, 165,  0)
PURPLE = (160, 32, 240)
MAGENTA = (255, 0, 255)
all_sprites_list = pygame.sprite.Group()
class Player(pygame.sprite.Sprite):
        def __init__(self, img):
        # Call the parent class (Sprite) constructor
            super().__init__()
            if img == "HoraceMann":
                self.image = pygame.image.load("Pictures/%s.jpg" % img).convert_alpha()
            elif img == "Betty":
                self.image = pygame.image.load("Pictures/%s.jpg" % img).convert_alpha()
            else:
                self.image = pygame.image.load("Pictures/%s.png" % img).convert_alpha()

            self.image.set_colorkey(WHITE)
            self.rect = self.image.get_rect()
            self.rect.x = 9999
            self.rect.y = 9999
            all_sprites_list.add(self)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


bus = Player("battlebus")
dman = Player("dman")
dman0 = Player("dman0")
dman1 = Player("dman")
dman2 = Player("dman")
'''
all_sprites_list.add(bus)
all_sprites_list.add(dman)
all_sprites_list.add(dman0)
'''
background = pygame.image.load("Pictures/portalcontrol.png").convert_alpha()
text0 = "Fortnite"
FPS = 60
rot1 = 0
rot2 = 0
sdura = 20
sspeed = 0
mspeed = 0
dm= [1,1,9,4,6,7]
clock = pygame.time.Clock()
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE =  (  0,   0, 255)
SBLUE = (  0, 191, 255)
YELLOW = ( 255, 255, 0)
LIME  = (173, 255,  47)
GREEN = (  0, 255,   0)
ORANGE = (255, 165,  0)
PURPLE = (160, 32, 240)
MAGENTA = (255, 0, 255)
rposx = 326
rposy = 70
rposx0 = 296
rposy0 = 182
rposx1 = 356
rposy1 = 180
red = 255
gre = 0
blu = 0
boop = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
red0 = 255
gre0 = 100
blu0 = 0
red1 = 205
gre1 = 50
blu1 = 0
kop = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
rpos0 = [255, 100, 0]
rpos1 = [205, 50, 0]
pos = [0, 0]
pos1 = [0, 0]
pos0 = [450, 0]
pos2 = [840, 0]
pos3 = [330, 75]
opos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
lpos = [460,75,390,75,42,75,-18,75,-78,75,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
top = 460
top0 = -78
wscene = 0
#opos = [9999, 9999]
scene = 69
bscene = 0
escene = 0

lscene = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bposx = -275
bposy = -100
bdman = pygame.image.load("Pictures/dman.png").convert_alpha()
bdman0 = pygame.image.load("Pictures/dman0.png").convert_alpha()
bdman1 = pygame.image.load("Pictures/dman0.png").convert_alpha()
bdman = pygame.transform.rotozoom(bdman, 0, 0.5)
bdman0 = pygame.transform.rotozoom(bdman0, 0, 0.5)

randpos = [random.randrange(400),random.randrange(370)]
def testtext(text1, text2):
    textSurfaceObj = fontObj.render(str(text1), True, BLACK)
    textSurfaceObj2 = fontObj.render(str(text2), True, RED)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (350, 250)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (350, 275)
    screen.blit(textSurfaceObj, textRectObj)
    screen.blit(textSurfaceObj2, textRectObj2)
def testtext0(text1, text2):
    textSurfaceObj = fontObj.render(str(text1), True, BLACK)
    textSurfaceObj2 = fontObj.render(str(text2), True, RED)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (350, 200)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (350, 225)
    screen.blit(textSurfaceObj, textRectObj)
    screen.blit(textSurfaceObj2, textRectObj2)
def text(text1, ttposx, ttposy, font, trans, color):
    textSurfaceObj = font.render(str(text1), True, color)
    textSurfaceObj = pygame.transform.rotate(textSurfaceObj, int(trans))
    textRectObj = textSurfaceObj.get_rect()

    textRectObj.center = (ttposx, ttposy)

    screen.blit(textSurfaceObj, textRectObj)

def progex(ttext, textspeed, imag, font):
        tfont = pygame.font.SysFont('%s' % font, 20)
        HEIGHT = 80
        WIDTH = 60
        tposx = 225
        tposy = 290
        tnum = 0
        ttnum = 0
        ttnumum = ""
        narr = 0
        i = 0
        done = False
        tlist = [None]


        #ttext = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq"
        if textspeed > len(ttext):
            textspeed = len(ttext)


        textvar = int(((textspeed - (int(textspeed) % 35)) / 35))

        profpic = pygame.image.load("Pictures/%s.png" % imag).convert_alpha()
        texbox = pygame.image.load("Pictures/textbox.png").convert_alpha()
        topbox = pygame.image.load("Pictures/topbox.png").convert_alpha()
        profect = profpic.get_rect()
        width = profect.width
        height = profect.height
        while round(height) != HEIGHT:
            if round(height) < HEIGHT:
                height *= 1.001
                width *= 1.001
            if round(height) > HEIGHT:
                height *= 0.999
                width *= 0.999
        profpic = pygame.transform.scale(profpic, (int(width), int(height)))
        profect = profpic.get_rect()



        screen.blit(texbox, (0, 260))
        if textspeed > 80:
            if textspeed < (len(ttext) - 20):
                tposy -= 0.5 * (textspeed - 80)
            else:
                tposy -= 0.5 * ((len(ttext) - 18) - 80)

        tformat = "{:.{precision}}"
        ttext = tformat.format(ttext, precision = textspeed)
        tlist = ["0"] * (textvar)

        if textvar > 0:
            for i in range(textvar):

                #ttext = tformat.format(ttext, precision = textspeed)
                #textvar = int(((textspeed - (int(textspeed) % 35)) / 35))
                tnum = 0
                ttnum = 0
                ttnumum = ""
                narr = 0




                if i == 0:
                    if len(ttext) > 25:
                        for j in range(35):
                            if ttext[(34 - j)].isspace():
                                tnum += 1
                        if tnum > 0:
                            arr = ttext.split()
                            for k in range(len(arr)):
                                narr += (len(arr[k]) + 1)
                                if narr >= 36:
                                    break
                            #print("narr." + str(narr))
                            ttnum = narr - 36
                            #ttnumum = "" * (ttnum)
                            #arr.insert(tnum, ttnumum)
                            arr[tnum - 1] += (" " * (len(arr[tnum]) - ttnum))

                            ttext = (" ".join(arr))

#Fix spacing

                    tlist[i] = "{:.35}".format(ttext)
                    tlist[i] = ttext.replace(tlist[i], "")
                    ttext = "{:.35}".format(ttext)
                    if len(tlist[i]) > 25:
                        if len(tlist) > 1:
                            tlist[i + 1] = tlist[i]


                        if len(tlist) > 1:
                            tnum = 0
                            ttnum = 0
                            ttnumum = ""
                            narr = 0
                            for j in range(35):
                                if tlist[i][(34 - j)].isspace():
                                    tnum += 1

                            if tnum > 0:
                                arr = tlist[i].split()
                                for k in range(len(arr)):

                                    narr += (len(arr[k]) + 1)

                                    if narr >= 36:

                                        break


                                if narr >= 36:
                                    ttnum = narr - 36
                                    #textspeed += ttnum
                                    #ttnumum = "" * (ttnum)
                                    #arr.insert(tnum, ttnumum)
                                    arr[tnum - 1] += (" " * (len(arr[tnum]) - ttnum))
                                    tlist[i] = (" ".join(arr))


                    tlist[i] = "{:.35}".format(tlist[i])


#1. Change textspeed and ttext length
#2. Fix code
#3. Make sure it's fine.
#4. Find out how you are going to make the text pan and scroll etc.


                else:
                    if len(tlist[i]) > 25:

                        for j in range(35):
                            if tlist[i][(34 - j)].isspace():
                                tnum += 1

                        if tnum > 0:
                            arr = tlist[i].split()
                            for k in range(len(arr)):

                                narr += (len(arr[k]) + 1)

                                if narr >= 36:

                                    break


                            if narr >= 36:
                                ttnum = narr - 36
                                #textspeed += ttnum
                                #ttnumum = "" * (ttnum)
                                #arr.insert(tnum, ttnumum)
                                arr[tnum - 1] += (" " * (len(arr[tnum]) - ttnum))
                                tlist[i] = (" ".join(arr))



                    tlist[i - 1] = "{:.35}".format(tlist[i])

                    tlist[i - 1] = tlist[i].replace(tlist[i - 1], "")
                    tlist[i] = "{:.35}".format(tlist[i - 1])

                    if len(tlist) > (i + 1):
                        tlist[i + 1] = tlist[i - 1]


                    #else:
                        #done = True


                '''
                if textspeed == 35 and (len(tlist)) != i:
               	    tlist.append(" ")
                else:
                    tlist.append(ttext.replace(tlist[i], ""))

                if ((textspeed - (int(textspeed) % 35)) - i) < 6:
                    text(tlist[i], tposx, tposy + (i * 10), tfont, 1, WHITE)
                '''
                #if tlist[i] != "0":
                if textspeed < ((i + 3) * 50):
                    text(tlist[i], tposx, tposy + ((i + 1) * 20), tfont, 0, WHITE)

                textvar = int(((textspeed - (int(textspeed) % 35)) / 35))



        if textspeed < 120:
            text(ttext, tposx, tposy, tfont, 0, WHITE)
        screen.blit(topbox, (0, 257))

        screen.blit(profpic, (30, 290))
        #return [text, tlist[0]]


def gettextsurf(text1, ttposx, ttposy, font, trans, color):
    textSurfaceObj = font.render(str(text1), True, color)
    textSurfaceObj = pygame.transform.rotate(textSurfaceObj, int(trans))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (ttposx, ttposy)
    return textRectObj

def sprpos0(name):
    name.rect.x = 9999
    name.rect.y = 9999
def sprpos(name, x, y):
    name.rect.x = x
    name.rect.y = y
    clock.tick(FPS)

def imag(spr, img):
    if img == "HoraceMann":
                spr.image = pygame.image.load("Pictures/%s.jpg" % img).convert_alpha()
    elif img == "Betty":
                spr.image = pygame.image.load("Pictures/%s.jpg" % img).convert_alpha()
    else:
                spr.image = pygame.image.load("Pictures/%s.png" % img).convert_alpha()
def trans(spr, rot):
    spr.image = pygame.transform.rotate(spr.image, int(rot))
def dilat(spr, wid, hei):
    spr.image = pygame.transform.scale(spr.image, (int(wid), int(hei)))
def trilat(spr, rot, scl):
    spr.image = pygame.transform.rotozoom(spr.image, rot, scl)
def flip(spr, x, y):
    spr.image = pygame.transform.flip(spr.image, x, y)
def explosion(escene, x, y, expand):
        explosion = pygame.image.load("Pictures/explosion.png").convert_alpha()
        explosion0 = pygame.image.load("Pictures/explosion(0).png").convert_alpha()
        explosion1 = pygame.image.load("Pictures/explosion(1).png").convert_alpha()
        explosion2 = pygame.image.load("Pictures/explosion(2).png").convert_alpha()
        explosion3 = pygame.image.load("Pictures/explosion(3).png").convert_alpha()
        explosion4 = pygame.image.load("Pictures/explosion(4).png").convert_alpha()
        explosion5 = pygame.image.load("Pictures/explosion(5).png").convert_alpha()
        explosion = pygame.transform.rotozoom(explosion, 0, expand)
        explosion0 = pygame.transform.rotozoom(explosion0, 0, expand)
        explosion1 = pygame.transform.rotozoom(explosion1, 0, expand)
        explosion2 = pygame.transform.rotozoom(explosion2, 0, expand)
        explosion3 = pygame.transform.rotozoom(explosion3, 0, expand)
        explosion4 = pygame.transform.rotozoom(explosion4, 0, expand)
        explosion5 = pygame.transform.rotozoom(explosion5, 0, expand)

        if escene % 7 == 0:
            screen.blit(explosion, (x, y))
        elif escene % 7 == 1:
            screen.blit(explosion0, (x, y))
        elif escene % 7 == 2:
            screen.blit(explosion1, (x, y))
        elif escene % 7 == 3:
            screen.blit(explosion2, (x, y))
        elif escene % 7 == 4:
            screen.blit(explosion3, (x, y))
        elif escene % 7 == 5:
            screen.blit(explosion4, (x, y))
        elif escene % 7 == 6:
            screen.blit(explosion5, (x, y))
def blast(escene, x, y, expand, rot):
        explosion = pygame.image.load("Pictures/blast.png").convert_alpha()
        explosion0 = pygame.image.load("Pictures/blast(0).png").convert_alpha()
        explosion1 = pygame.image.load("Pictures/blast(1).png").convert_alpha()
        explosion2 = pygame.image.load("Pictures/blast(2).png").convert_alpha()
        explosion3 = pygame.image.load("Pictures/blast(3).png").convert_alpha()
        explosion = pygame.transform.rotozoom(explosion, rot, expand)
        explosion0 = pygame.transform.rotozoom(explosion0, rot, expand)
        explosion1 = pygame.transform.rotozoom(explosion1, rot, expand)
        explosion2 = pygame.transform.rotozoom(explosion2, rot, expand)
        explosion3 = pygame.transform.rotozoom(explosion3, rot, expand)

        if escene % 10 == 0:
            screen.blit(explosion, (x, y))
        elif escene % 10 == 1:
            screen.blit(explosion0, (x, y))
        elif escene % 10 == 2:
            screen.blit(explosion1, (x, y))
        elif escene % 10 == 3:
            screen.blit(explosion1, (x, y))
        elif escene % 10 == 4:
            screen.blit(explosion0, (x, y))
        elif escene % 10 == 5:
            screen.blit(explosion2, (x, y))
        elif escene % 10 == 6:
            screen.blit(explosion3, (x, y))
        elif escene % 10 == 7:
            screen.blit(explosion2, (x, y))
        elif escene % 10 == 8:
            screen.blit(explosion3, (x, y))
        elif escene % 10 == 9:
            screen.blit(explosion, (x, y))
def smoke(escene, x, y, expand, rot):
    smoke = pygame.image.load("Pictures/smoke.png").convert_alpha()
    smoke = pygame.transform.rotozoom(smoke, 0, expand/4)
    escene %= 5
    for i in range(escene):

        if (rot >= 0 and rot < 22.5) or (rot <= 360 and rot > 337.5):
            screen.blit(smoke, (x, y))
            if i >= 1:
                screen.blit(smoke, (x, y + (15 * expand)))
            if i >= 2:
                screen.blit(smoke, (x, y + (15 * expand * 2)))
            if i >= 3:
                screen.blit(smoke, (x, y + (15 * expand * 3)))
            if i >= 4:
                screen.blit(smoke, (x, y + (15 * expand * 4)))
        if (rot < 67.5 and rot >= 22.5):
            screen.blit(smoke, (x, y))
            if i >= 1:
                screen.blit(smoke, (x + (15 * expand * math.sqrt(2) / 2), y + (15 * expand * math.sqrt(2) / 2)))
            if i >= 2:
                screen.blit(smoke, (x + (15 * expand * math.sqrt(2) / 2 * 2), y + (15 * expand * math.sqrt(2) / 2 * 2)))
            if i >= 3:
                screen.blit(smoke, (x + (15 * expand * math.sqrt(2) / 2 * 3), y + (15 * expand * math.sqrt(2) / 2 * 3)))
            if i >= 4:
                screen.blit(smoke, (x + (15 * expand * math.sqrt(2) / 2 * 3), y + (15 * expand * math.sqrt(2) / 2 * 3)))
        if (rot >= 67.5 and rot < 112.25):
            screen.blit(smoke, (x, y))
            if i >= 1:
                screen.blit(smoke, (x + (15 * expand), y))
            if i >= 2:
                screen.blit(smoke, (x + (15 * expand * 2), y))
            if i >= 3:
                screen.blit(smoke, (x + (15 * expand * 3), y))
            if i >= 4:
                screen.blit(smoke, (x + (15 * expand * 3), y))
        if (rot < 157.5 and rot >= 112.25):
            screen.blit(smoke, (x, y))
            if i >= 1:
                screen.blit(smoke, (x + (15 * expand * math.sqrt(2) / 2), y - (15 * expand * math.sqrt(2) / 2)))
            if i >= 2:
                screen.blit(smoke, (x + (15 * expand * math.sqrt(2) / 2 * 2), y - (15 * expand * math.sqrt(2) / 2 * 2)))
            if i >= 3:
                screen.blit(smoke, (x + (15 * expand * math.sqrt(2) / 2 * 3), y - (15 * expand * math.sqrt(2) / 2 * 3)))
            if i >= 4:
                screen.blit(smoke, (x + (15 * expand * math.sqrt(2) / 2 * 3), y - (15 * expand * math.sqrt(2) / 2 * 3)))
        if (rot >= 157.5 and rot < 202.5):
            screen.blit(smoke, (x, y))
            if i >= 1:
                screen.blit(smoke, (x, y - (15 * expand)))
            if i >= 2:
                screen.blit(smoke, (x, y - (15 * expand * 2)))
            if i >= 3:
                screen.blit(smoke, (x, y - (15 * expand * 3)))
            if i >= 4:
                screen.blit(smoke, (x, y - (15 * expand * 4)))
        if (rot < 247.5 and rot >= 202.5):
            screen.blit(smoke, (x, y))
            if i >= 1:
                screen.blit(smoke, (x - (15 * expand * math.sqrt(2) / 2), y - (15 * expand * math.sqrt(2) / 2)))
            if i >= 2:
                screen.blit(smoke, (x - (15 * expand * math.sqrt(2) / 2 * 2), y - (15 * expand * math.sqrt(2) / 2 * 2)))
            if i >= 3:
                screen.blit(smoke, (x - (15 * expand * math.sqrt(2) / 2 * 3), y - (15 * expand * math.sqrt(2) / 2 * 3)))
            if i >= 4:
                screen.blit(smoke, (x - (15 * expand * math.sqrt(2) / 2 * 3), y - (15 * expand * math.sqrt(2) / 2 * 3)))
        if (rot >= 247.5 and rot < 292.5):
            screen.blit(smoke, (x, y))
            if i >= 1:
                screen.blit(smoke, (x - (15 * expand), y))
            if i >= 2:
                screen.blit(smoke, (x - (15 * expand * 2), y))
            if i >= 3:
                screen.blit(smoke, (x - (15 * expand * 3), y))
            if i >= 4:
                screen.blit(smoke, (x - (15 * expand * 3), y))
        if (rot >= 337.5 and rot >= 292.5):
            screen.blit(smoke, (x, y))
            if i >= 1:
                screen.blit(smoke, (x - (15 * expand * math.sqrt(2) / 2), y + (15 * expand * math.sqrt(2) / 2)))
            if i >= 2:
                screen.blit(smoke, (x - (15 * expand * math.sqrt(2) / 2 * 2), y + (15 * expand * math.sqrt(2) / 2 * 2)))
            if i >= 3:
                screen.blit(smoke, (x - (15 * expand * math.sqrt(2) / 2 * 3), y + (15 * expand * math.sqrt(2) / 2 * 3)))
            if i >= 4:
                screen.blit(smoke, (x - (15 * expand * math.sqrt(2) / 2 * 3), y + (15 * expand * math.sqrt(2) / 2 * 3)))


def multi(speed, x, y, expand, rot):
    multi = pygame.image.load("Pictures/marrow.png").convert_alpha()
    multi = pygame.transform.rotozoom(multi, rot, expand)
    if speed <= 450:
        screen.blit(multi, (x + speed, y - (40 * expand)))
        screen.blit(multi, (x + speed, y - (20 * expand)))
        screen.blit(multi, (x + speed, y - (0 * expand)))
        screen.blit(multi, (x + speed, y + (20 * expand)))
        screen.blit(multi, (x + speed, y + (40 * expand)))

def scatter(dura, tspeed, speed, x, y, expand, rot):
    scatter = pygame.image.load("Pictures/sarrow.png").convert_alpha()
    multi = pygame.image.load("Pictures/marrow.png").convert_alpha()
    if flip == 1:
        scatter = pygame.transform.flip(scatter, True, False)

    scatter = pygame.transform.rotozoom(scatter, rot, expand)
    multi0 = pygame.transform.rotozoom(multi, 0, expand)
    multi1 = pygame.transform.rotozoom(multi, 0 + 40, expand)
    multi2 = pygame.transform.rotozoom(multi, 0 + 80, expand)
    multi3 = pygame.transform.rotozoom(multi, 0 + 120, expand)
    multi4 = pygame.transform.rotozoom(multi, 0 + 160, expand)
    multi5 = pygame.transform.rotozoom(multi, 0 + 200, expand)
    multi6 = pygame.transform.rotozoom(multi, 0 + 240, expand)
    multi7 = pygame.transform.rotozoom(multi, 0 + 280, expand)
    multi8 = pygame.transform.rotozoom(multi, 0 + 320, expand)

    scons = speed * 0.005 / (expand * 3)

    #get the pythag theorm of the speed away from mid
    if dura < 80:
        if dura <= 0 and speed < 1000:
            screen.blit(multi0, (x + tspeed + speed   * (expand/2) * scons, y))
            screen.blit(multi1, (x + tspeed + (speed   * (expand/2) * scons * math.sin((2 * math.pi)/9)), y - (speed   * (expand/2) * scons * math.cos((2 * math.pi)/(9)))))
            screen.blit(multi2, (x + tspeed + (speed   * (expand/2) * scons * math.cos(4 * math.pi/9)), y - (speed   * (expand/2) * scons * math.sin(4 * math.pi/9))))
            screen.blit(multi3, (x + tspeed - (speed   * (expand/2) * scons * 1/2), y - (speed   * (expand/2) * scons * math.sqrt(3)/2)))
            screen.blit(multi4, (x + tspeed - (speed   * (expand/2) * scons * math.sin((7* math.pi)/(18))), y - (speed   * (expand/2) * scons * math.cos((7* math.pi)/(18)))))
            screen.blit(multi5, (x + tspeed - (speed   * (expand/2) * scons * math.cos((1* math.pi)/(9))), y + (speed   * (expand/2) * scons * math.sin((1* math.pi)/(9)))))
            screen.blit(multi6, (x + tspeed - (speed   * (expand/2) * scons * 1/2), y + (speed   * (expand/2) * scons  * math.sqrt(3)/2)))
            screen.blit(multi7, (x + tspeed + (speed   * (expand/2) * scons * math.sin(math.pi/18)), y + (speed   * (expand/2) * scons * math.cos(math.pi/18))))
            screen.blit(multi8, (x + tspeed + (speed   * (expand/2) * scons * math.cos(5 * math.pi/18)), y + (speed   * (expand/2) * scons * math.sin(5 * math.pi/18))))
        elif dura > 0:
            screen.blit(scatter, (x + speed, y))


sprpos(dman2, -300, 150)
screen.blit(background, pos)
portal = pygame.image.load("Pictures/herno.png").convert_alpha()
screen.blit(portal, (306, 62))
while True:
    randpos = [random.randrange(400),random.randrange(300)]
    if scene == 0:
        screen.fill(WHITE)
        sprpos(bus, bposx, bposy)
        imag(bus, "battlebus")
        flip(bus, True, False)
        dilat(bus, 600, 450)
        trans(bus, -15)
        background = pygame.image.load("Pictures/sky.png").convert_alpha()
        #background = pygame.transform.flip(spr.image, x, y)
        screen.blit(background, pos)
        screen.blit(background, pos0)
        bposx += 1
        wscene += 1
        pos[0] -= 50
        pos0[0] -= 50
        if pos[0] <= -450:
            pos[0] = 450
        if pos0[0] <= -450:
            pos0[0] = 450
        all_sprites_list.draw(screen)
        testtext(wscene, None)
        if wscene >= 200:
            scene = 1
            pos = [0,0]
            sprpos0(bus)
            wscene = 0
    if scene == 1:
        screen.fill(WHITE)
        background = pygame.image.load("Pictures/binside.png").convert_alpha()


        flip(dman0, True, False)
        if wscene % 3 == 0:
            imag(dman, "dman")
            imag(dman0, "dman0(0)")
            if wscene <= 350:
                imag(dman1, "dman(0)")
            imag(dman2, "dman(1)")
        if wscene % 3 == 1:
            imag(dman, "dman(0)")
            imag(dman0, "dman0(1)")
            if wscene <= 350:
                imag(dman1, "dman(1)")
            imag(dman2, "dman")
        if wscene % 3 == 2:
            imag(dman, "dman(1)")
            imag(dman0, "dman0")
            if wscene <= 350:
                imag(dman1, "dman")
            imag(dman2, "dman(0)")
        if wscene >= 350:
            imag(dman1, "dman(1)")
        if wscene >= 400:
            imag(dman1, "dman")
        flip(dman0, True, False)
        flip(dman2, True, False)
        #flip(dman, True, False)
        ndman = pygame.image.load("Pictures/dman.png").convert_alpha()
        muscle = pygame.image.load("Pictures/muscle.png").convert_alpha()
        muscle0 = pygame.transform.flip(muscle, True, False)

        ndman0 = pygame.image.load("Pictures/dman0.png").convert_alpha()
        fdman = pygame.transform.flip(ndman, True, False)
        fdman0 = pygame.transform.flip(ndman0, True, False)
        ndman = pygame.transform.rotozoom(ndman, 0, 0.5)
        ndman0 = pygame.transform.rotozoom(ndman0, 0, 0.5)
        fdman = pygame.transform.rotozoom(fdman, 0, 0.5)
        fdman0 = pygame.transform.rotozoom(fdman0, 0, 0.5)





        if wscene >= 30 and wscene <= 239:
            pos[0] -= 2
            pos1[0] -= 2
            pos2[0] -= 2
        if wscene >= 300 and wscene < 550:
            background = pygame.transform.rotozoom(background, 0, 1.25)
            #background0 = pygame.transform.rotozoom(background0, 0, 1.25)
            trilat(dman1, 0, 1.25)
            trilat(dman2, 0, 1.25)
        if wscene == 300:
            opos[0] -= 20
            opos[1] += 20
            pos[0] -= 25
            pos[1] -= 25
            pos1[0] -= 145
            pos1[1] -= 40
            pos2[0] -= 145
            pos2[1] -= 40
        if pos1[0] <= -840:
            pos1[0] = 840
        if pos2[0] <= -840:
            pos2[0] = 840

        screen.blit(background, pos2)
        screen.blit(background, pos1)

        screen.blit(ndman0, (pos[0] + 75, pos[1] + 60))
        screen.blit(fdman, (pos[0] + 285, pos[1] + 60))
        if wscene >= 70:
            screen.blit(bdman0, (pos[0] + 75 + 419, pos[1] + 60))

        if wscene >= 165 and wscene < 300:
            bdman = pygame.transform.rotate(bdman, 1)
            screen.blit(bdman, (pos[0] + 285 + 419, pos[1] + 60))
        if wscene >= 200 and wscene < 300:
            bdman0 = pygame.transform.rotozoom(bdman0, -5, 0.95)
        if wscene >= 240:
            bdman1 = pygame.transform.scale(bdman1, (5, 5))
            screen.blit(bdman1, randpos)
            screen.blit(bdman1, randpos)


        wscene += 1
        if wscene % 3 == 0:
            if wscene >= 70:
                bdman0 = pygame.transform.flip(bdman0, True, False)
        if wscene % 6 == 0:
            if wscene >= 70:
                    bdman0 = pygame.transform.flip(bdman0, False, True)
        if wscene % 3 == 0:
            pos[0] += 3
            pos[1] += 2

            if wscene % 2 == 0:
                pos[0] -= 6

            if wscene % 2 == 0:
                pos[1] -= 4
        sprpos(dman, pos[0] + 60, pos[1] + 150)

        sprpos(dman0, pos[0] + 250, pos[1] + 150)

        '''
            screen.blit(muscle, (pos[0] + 250 - 40  + 419 + opos[1], pos[1] - 30 + 150))
            screen.blit(muscle0, (pos[0] + 250 + 80 + 419 + opos[1], pos[1] - 30 + 150))
            '''
        if wscene >= 415 and  wscene <= 420:
            opos[0] += 4

        sprpos(dman1, pos[0] + 60 + 419 + opos[0], pos[1] + 150)
        if wscene == 400:
            imag(dman1, "dman(2)")
        if wscene == 402:
            imag(dman1, "dman(3)")
        if wscene == 403:
            imag(dman1, "dman(2)")


        if wscene == 404:
            imag(dman1, "dman(3)")

        if wscene == 405:
            imag(dman1, "dman")
            trilat(dman1, 0, 1.25)
        if wscene == 407:
            imag(dman1, "dman(2)")
            trilat(dman1, 0, 1.25)

        if wscene == 407:
            imag(dman1, "dman(2)")
            trilat(dman1, 0, 1.25)
        if wscene == 408:
            imag(dman1, "dman(3)")
            trilat(dman1, 0, 1.25)
        if wscene == 409:
            imag(dman1, "dman(3)")
            trilat(dman1, 0, 1.25)
        if wscene >= 410 and wscene <= 550:
            imag(dman1, "dman(4)")
            trilat(dman1, 0, 1.25)
        if wscene >= 550:
            imag(dman1, "dman(4)")
            opos[1] += 100
        if wscene >= 550 and wscene < 552:
            rot1 -= 45

        if wscene >= 555:
            scene = 2
            pos = [0,0]
            sprpos0(dman0)
            sprpos0(dman1)
            sprpos0(dman)
            imag(dman2, "dman")
            sprpos(dman2, -300, 150)
            opos[2] = 0
            rot1 = 0
            wscene = 0
        if wscene >= 420 and wscene <= 422:
            rot1 -= 30

        if wscene >= 423 and wscene <= 433:
            rot1 += 9
            rot2 += 9
            opos[1] -= 16.5
            opos[2] -= 12
        if pos1[0] <= -840:
            pos1[0] = 840
        if pos2[0] <= -840:
            pos2[0] = 840
        if wscene >= 434 and wscene < 438:
            pos1[0] -= 5
            pos2[0] -= 5
        if wscene >= 438 and wscene < 441:
            pos1[0] -= 20
            pos2[0] -= 20
        if wscene >= 441 and wscene < 471:
            pos1[0] -= 40
            pos2[0] -= 40
        if wscene >= 471 and wscene < 550:
            pos1[0] -= 120
            pos2[0] -= 120

        if wscene == 550:
            opos[0] += 20
            opos[1] -= 20
            pos[0] += 25
            pos[1] += 25
            pos1[0] += 145
            pos1[1] += 40
            pos2[0] += 144
            pos2[1] += 40
            background = pygame.image.load("Pictures/portalcontrol.png").convert_alpha()
            screen.blit(background, pos)
            portal = pygame.image.load("Pictures/herno.png").convert_alpha()
            screen.blit(portal, (306, 62))

        trans(dman1, rot1)
        trans(dman2, rot2)


        sprpos(dman2, pos[0] + 250 + 419 + opos[1], pos[1] + 150 + opos[2])
        all_sprites_list.draw(screen)
        testtext(wscene, None)
    if scene == 2:
        background = pygame.image.load("Pictures/portalcontrol(0).png").convert_alpha()
        if wscene == 110:
            background = pygame.image.load("Pictures/portalcontrol.png").convert_alpha()
        if wscene >= 175:
            background = pygame.image.load("Pictures/portalcontrol(1).png").convert_alpha()
        broken = pygame.image.load("Pictures/break.png").convert_alpha()



        if wscene % 12 == 0:
            portal = pygame.image.load("Pictures/fort(1).png").convert_alpha()
        if wscene % 12 == 4:
            portal = pygame.image.load("Pictures/fort.png").convert_alpha()
        if wscene % 12 == 8:
            portal = pygame.image.load("Pictures/fort(0).png").convert_alpha()


        #306,62
        if wscene <= 175:
            if wscene % 210 >= 0 and wscene % 210 < 30:
                rposx -= 1
                rposy += 1

                if wscene % 210 >= 0 and wscene % 210 < 5:
                    rposx0 -= 1
                    rposy0 += 1
                rposx0 += 1
                rposy0 += 1
            if wscene % 210 >= 0 and wscene % 210 < 40:
                rposx1 -= 0
                rposy1 -= 2


            if wscene % 210 >= 30 and wscene % 210 < 75:
                rposy += 2

                if wscene % 210 >= 30 and wscene % 210 < 35:
                    rposx0 += 0
                    rposy0 += 2
                '''
                rposx0 += 1
                rposy0 -= 1
                '''
            if wscene % 210 >= 30 and wscene % 210 < 65:
                rposx0 += 1
                rposy0 -= 1
            if wscene % 210 >= 40 and wscene % 210 < 70:
                rposx1 -= 1
                rposy1 -= 1
                '''

            if wscene % 210 == 140:
                opos[4] = 1
                rposx1 = rposx
                rposy1 = rposy
                '''
            if wscene % 210 >= 75 and wscene % 210 < 105:
                rposx += 1
                rposy += 1
            if wscene % 210 >= 65 and wscene % 210 < 110:
                rposx0 -= 0
                rposy0 -= 2
            if wscene % 210 >= 70 and wscene % 210 < 100:
                rposx1 -= 1
                rposy1 += 1

                '''
                if wscene % 210 >= 75 and wscene % 210 < 80:
                    rposx0 -= 1
                    rposy0 += 3
                rposx0 -= 0
                rposy0 -= 2
                '''
            if wscene % 210 >= 105 and wscene % 210 < 135:

                rposx += 1
                rposy -= 1
            if wscene % 210 >= 110 and wscene % 210 < 140:

                rposx0 -= 1
                rposy0 -= 1
            if wscene % 210 >= 100 and wscene % 210 < 145:
                rposx1 -= 0
                rposy1 += 2
                '''
                if wscene % 210 >= 105 and wscene % 210 < 110:
                    rposx0 += 1
                    rposy0 -= 1
                rposx0 -= 1
                rposy0 -= 1
                '''
            if wscene % 210 >= 135 and wscene % 210 < 180:
                rposy -= 2
            if wscene % 210 >= 140 and wscene % 210 < 170:

                rposx0 -= 1
                rposy0 += 1
            if wscene % 210 >= 145 and wscene % 210 < 175:
                rposx1 += 1
                rposy1 += 1
                '''
                if wscene % 210 >= 135 and wscene % 210 < 140:
                    rposx0 += 0
                    rposy0 -= 2
                rposx0 -= 1
                rposy0 += 1
                '''
            if wscene % 210 >= 180 and wscene % 210 <= 209:
                rposx -= 1
                rposy -= 1
            if wscene % 210 >= 170 and wscene % 210 <= 209:

                rposx0 -= 0
                rposy0 += 2
            if wscene % 210 >= 175 and wscene % 210 < 205:
                rposx1 += 1
                rposy1 -= 1
            if wscene % 210 >= 205 and wscene % 210 <= 209:
                rposx1 += 0
                rposy1 -= 2
            #and wscene % 7 == 0:
            if wscene % 210 < 70:
                gre += 10/7
                gre0 -= 5/7
                red0 -= 5/7
                red1 += 5/7
                gre1 -= 5/7
                opos[5] += 1
            if wscene % 210 < 140 and wscene % 210 >= 70:
                gre1 += 10/7
                gre -= 5/7
                red -= 5/7
                red0 += 5/7
                gre0 -= 5/7
                opos[6] += 1
            if wscene % 210 < 210 and wscene % 210>= 140:
                gre0 += 10/7
                gre1 -= 5/7
                red1 -= 5/7
                red += 5/7
                gre -= 5/7
                opos[7] += 1
                '''
                if wscene % 210 >= 180 and wscene % 210 < 185:
                    rposx0 -= 1
                    rposy0 -= 1
                rposx0 -= 0
                rposy0 += 2
                '''


        imag(dman2, "dman")
        #15 * wscene % 360
        trilat(dman2, (30 * wscene % 360), 0.5)
        sprpos(dman2, -850  + opos[2], 275)
        if wscene <= 100:
            opos[2] += 10

        wscene += 1

        if wscene >= 100:
            sprpos0(dman2)
        if wscene >= 205:
            sprpos(bus, -400 + opos[3], 25)
            opos[3] += 15
            imag(bus, "battlebus")
            flip(bus, True, False)
            trilat(bus, 0, 0.5)
        if wscene >= 247:
            sprpos0(bus)
        if wscene >= 250:
            scene = 3
            wscene = 1




        screen.blit(background, pos)
        RED = (red, gre, blu)
        RORANGE = (red0, gre0, blu0)
        DRED = (red1, gre1, blu1)
        if wscene >= 110 and wscene <= 175:
            red = random.randrange(255)
            gre = random.randrange(255)
            blu = random.randrange(255)
            red0 = random.randrange(255)
            gre0 = random.randrange(255)
            blu0 = random.randrange(255)
            red1 = random.randrange(255)
            gre1 = random.randrange(255)
            blu1 = random.randrange(255)
        if opos[4] == 1:

            testtext(rposx1, rposy1)
        testtext(wscene, opos[3])
        if wscene >= 110 and wscene <= 175:
            text0 = id_generator()
        if wscene <= 175:
            text(text0, 300, 39, fontObj0, 0, BLACK)
        if wscene > 170:


            text0 = "Smash Herno"

            text(text0, 275, 39, fontObj0, 0, BLACK)





        #testtext(rpos[0], rpos[1])
        if wscene < 175:
            pygame.draw.circle(screen, RED, (rposx, rposy), 14, 0)
            pygame.draw.circle(screen, RORANGE, (rposx0, rposy0), 14, 0)
            pygame.draw.circle(screen, DRED, (rposx1, rposy1), 14, 0)
        if wscene >= 175:
            screen.blit(portal, (306, 62))
        if wscene > 100:
            screen.blit(broken, (-850  + opos[2], 275))
        #testtext(wscene, None)
        all_sprites_list.draw(screen)
    if scene == 3:
        background = pygame.image.load("Pictures/droppin.png").convert_alpha()


        bg = random.randrange(1,3)
        dm0 = pygame.image.load("Pictures/dman.png").convert_alpha()
        dm1 = pygame.image.load("Pictures/dman0.png").convert_alpha()
        dm0 =  pygame.transform.rotozoom(dm0, 0, .5)
        dm1 =  pygame.transform.rotozoom(dm1, 0, .5)
        dm2 =  pygame.transform.flip(dm0, True, False)
        dm3 =  pygame.transform.flip(dm1, True, False)
        if dm[0] <= 4:
            ldman = dm2
        if dm[0] > 4:
            ldman = dm3
        if dm[1] <= 4:
            ldman0 = dm2
        if dm[1]> 4:
            ldman0 = dm3
        if dm[2] <= 4:
            ldman1 = dm2
        if dm[2] > 4:
            ldman1 = dm3
        if dm[3] <= 4:
            ldman2 = dm0
        if dm[3] > 4:
            ldman2 = dm1
        if dm[4] <= 4:
            ldman3 = dm0
        if dm[4] > 4:
            ldman3 = dm1
        if dm[5] <= 4:
            ldman4 = dm0
        if dm[5] > 4:
            ldman4 = dm1

        screen.blit(background, pos)

        imag(dman, "dman")
        imag(dman1, "dman")
        imag(dman0, "dman0")
        trilat(dman, 0, 0.75)
        trilat(dman0, 0, 0.75)
        trilat(dman1, 0, 0.8)
        flip(dman1, True, False)
        sprpos(dman, 40, 220)
        sprpos(dman0, 160, 180)
        sprpos(dman1, 280, 200)
        bscene += 1

        pos3[0] -= 2

        if pos3[0] <= 360 and pos3[0] >= 345 and boop[0] == 0:
            lscene[0] += 1
            pos3[0] += 2
            boop[0] = 0
            if lscene[0] == 20:
                boop[0] = 1
                lscene[0] = 0



        if pos3[0] <= 330 and pos3[0] > 240:
            kop[0] *= 0.90
            ldman = pygame.transform.rotozoom(ldman, bscene * 5, kop[0])
            pos3[1] += bg
        if pos3[0] <= 240:
            pos3[0] = top
            kop[0] = 1
            pos3[1] = 75
            boop[0] = 0
            dm[0] = random.randrange(0,10)


        lpos[0] -= 2
        if lpos[0] <= 330 and lpos[0] > 240:
            kop[1] *= 0.90
            ldman0 = pygame.transform.rotozoom(ldman0, bscene * 5, kop[1])
            lpos[1] += bg
        if lpos[0] <= 240:
            lpos[1] = 75
            kop[1] = 1
            lpos[0] = top
            boop[1] = 0
            dm[1] = random.randrange(0,10)
        if lpos[0] <= 360 and lpos[0] >= 345 and boop[1] == 0:
            lscene[1] += 1
            lpos[0] += 2
            if lscene[1] == 20:
                boop[1] = 1
                lscene[1] = 0


        lpos[2] -= 2
        if lpos[2] <= 330 and lpos[2] > 240:
            kop[2] *= 0.90
            ldman1 = pygame.transform.rotozoom(ldman1, bscene * 5, kop[2])
            lpos[3] += bg
        if lpos[2] <= 240:
            lpos[3] = 75
            kop[2] = 1
            lpos[2] = top
            boop[2] = 0

            dm[2] = random.randrange(0,10)
        if lpos[2] <= 360 and lpos[2] >= 345 and boop[2] == 0:
            lscene[2] += 1
            lpos[2] += 2
            if lscene[2] == 20:
                boop[2] = 1
                lscene[2] = 0




        lpos[4] += 2
        if lpos[4] <= 160 and lpos[4] > 56:
            kop[3] *= 0.90
            ldman2 = pygame.transform.rotozoom(ldman2, bscene * 5, kop[3])
            lpos[5] += bg
            lpos[4] += 3
        if lpos[4] > 160:
            lpos[5] = 75
            kop[3] = 1
            lpos[4] = top0
            boop[3] = 0
            dm[3] = random.randrange(0,10)
        if lpos[4] >= 26 and lpos[4] <= 41 and boop[3] == 0:
            lscene[3] += 1
            lpos[4] -= 2
            if lscene[3] == 20:
                boop[3] = 1
                lscene[3] = 0

        lpos[6] += 2
        if lpos[6] >= 56 and lpos[6] < 160:
            kop[4] *= 0.90
            ldman3 = pygame.transform.rotozoom(ldman3, bscene * 5, kop[4])
            lpos[7] += bg
            lpos[6] += 3
        if lpos[6] >= 160:
            lpos[7] = 75
            kop[4] = 1
            lpos[6] = top0
            boop[4] = 0
            dm[4] = random.randrange(0,10)
        if lpos[6] >= 26 and lpos[6] <= 41 and boop[4] == 0:
            lscene[4] += 1
            lpos[6] -= 2
            if lscene[4] == 20:
                boop[4] = 1
                lscene[4] = 0

        lpos[8] += 2
        if lpos[8] >= 56 and lpos[8] < 160:
            kop[5] *= 0.90
            ldman4 = pygame.transform.rotozoom(ldman4, bscene * 5, kop[5])
            lpos[9] += bg
            lpos[8] += 3
        if lpos[8] >= 160:
            lpos[9] = 75
            kop[5] = 1
            lpos[8] = top0
            boop[5] = 0
            dm[5] = random.randrange(0,10)
        if lpos[8] >= 26 and lpos[8] <= 41 and boop[5] == 0:
            lscene[5] += 1
            lpos[8] -= 2
            if lscene[5] == 20:
                boop[5] = 1
                lscene[5] = 0




        screen.blit(ldman1, (lpos[2], lpos[3]))







        screen.blit(ldman, (pos3[0], pos3[1]))

        screen.blit(ldman0, (lpos[0], lpos[1]))
        screen.blit(ldman2, (lpos[4], lpos[5]))
        screen.blit(ldman3, (lpos[6], lpos[7]))
        screen.blit(ldman4, (lpos[8], lpos[9]))
        if bscene >= 300:
            scene = 4
            wscene = 0
            sprpos0(dman)
            sprpos0(dman0)
            sprpos0(dman1)
            opos[0] = 0
            opos[1] = 0
            opos[2] = 0
            opos[3] = 0
            opos[4] = 0
            opos[5] = 0
            opos[6] = 0
            opos[7] = 0
            opos[8] = 0
            pos = (0,0)

        all_sprites_list.draw(screen)
        testtext(bscene, pos3[0])
    if scene == 4:
        screen.fill(WHITE)
        if wscene == 0:
            opos[2] = 9

        background = pygame.image.load("Pictures/Scity.png").convert_alpha()
        bman = pygame.image.load("Pictures/bman.png").convert_alpha()
        bman = pygame.transform.scale(bman, (5, 5))
        bman = pygame.transform.rotate(bman, randpos[0])
        battlebus = pygame.image.load("Pictures/battlebus.png").convert_alpha()
        battlebus = pygame.transform.rotozoom(battlebus, 30, 0.10)
        imag(bus, "battlebus")
        trilat(bus, 30, 0.10)
        flip(bus, True, False)
        sprpos(bus, -100 + opos[0], opos[1]+10)

        opos[0] += 5
        if wscene == 300:
            scene = 5
            wscene = 0

            opos[0] = 0
            opos[1] = 0
            opos[2] = 0
            opos[3] = 0
            opos[4] = 0
            opos[5] = 0
            opos[6] = 0
            opos[7] = 0
            opos[8] = 0
            pos = (0,0)





        if wscene >= 150:
            opos[8] += 1.5
            opos[7] -= 6

        opos[1] -= 0.25
        wscene += 1
        opos[2] += 1.5
        screen.blit(background, (0, opos[1]))
        screen.blit(battlebus, (420 + opos[7], opos[1] + 10))
        if wscene % 3 == 0 and wscene >= 20:
            if opos[4] <= 27 or opos[4] >= 300:
                opos[4] += 1
            if opos[6] <= 29 and wscene % 300 >= 150:
                opos[6] += 1


        for opos[3] in range(opos[4]):
                screen.blit(bman, (10 + (14.5 * opos[3]), opos[1] + 10 + opos[2] - (4.5*opos[3])))
        for opos[5] in range(opos[6]):
            if wscene >= 150:
                screen.blit(bman, (429 - (14.5 * opos[5]), opos[1]+ 10 + opos[8] + 40 - (4.5*opos[5])))
        all_sprites_list.draw(screen)
    if scene == 5:
        screen.fill(WHITE)
        background = pygame.image.load("Pictures/Scity.png").convert_alpha()
        background = pygame.transform.rotozoom(background, 0, 4)
        sman = pygame.image.load("Pictures/sman.png").convert_alpha()
        bman = pygame.image.load("Pictures/bman.png").convert_alpha()
        if wscene == 0:
            opos[0] = 150
            opos[2] = 15
            opos[3] = -200
            opos[4]= 500
            opos[5] = -13
            opos[6] = -500
            opos[7] = 300
            opos[8] = 1
            sman0 = sman.get_rect()
            smany = sman0.bottomleft[1] - sman0.topleft[1]
            smanx = sman0.topright[0] - sman0.topleft[0]
        wscene += 1


        #sman = pygame.transform.rotozoom(sman, opos[1],1)
        sman = pygame.transform.rotate(sman, opos[1])
        sman = pygame.transform.scale(sman, (smanx, smany))
        web = pygame.image.load("Pictures/web.png").convert_alpha()
        web = pygame.transform.rotate(web, opos[5])
        web = pygame.transform.scale(web, (50, opos[4]))
        if wscene <= 9:
            opos[5] += 10
        if wscene >= 25:
            opos[6] += 100
        if wscene >= 29 and wscene < 32:
            smany = 5
            opos[7] += 100
        if wscene >= 45:
            scene = 6

            wscene = 0

            opos[0] = 0
            opos[1] = 0
            opos[2] = 0
            opos[3] = 0
            opos[4] = 0
            opos[5] = 0
            opos[6] = 0
            opos[7] = 0
            opos[8] = 0
            pos = (0,0)


        if wscene <= 30:
            opos[2] += 3.5
        #opos[6] *= 0.99
            opos[3] -= 20
            opos[1] += 1
            if wscene >= 9:
                opos[0] -= 30
                opos[1] += 4
                opos[3] -= 15
                opos[7] -= 2

        '''
        opos[4] += 5
        opos[0] += 10
        opos[1] += 1
        opos[2] += 10
        opos[3] -= 25
        opos[5] += 1
        '''
        screen.blit(background, (opos[3],-1150))
        screen.blit(sman, (opos[2], opos[7]))
        screen.blit(bman, (opos[2], opos[7] + opos[6]))
        screen.blit(web, (opos[0], -100))
        testtext(wscene, smany)
    if scene == 6:
        screen.fill(WHITE)

        background = pygame.image.load("Pictures/scity1.png")
        background0 = pygame.image.load("Pictures/scity1.png")
        background = pygame.transform.rotozoom(background, 0, 5)
        background0 = pygame.transform.rotozoom(background0, 0, 5)
        sman = pygame.image.load("Pictures/sman.png").convert_alpha()
        bman = pygame.image.load("Pictures/bman.png").convert_alpha()

        if wscene == 0:
            opos[0] = 500
            opos[1] = 0
            opos[2] = 200
            opos[3] = 200
            opos[4] = -1000
            opos[5] = 200
            opos[7] = 200
            bman0 = bman.get_rect()
            bmany = bman0.bottomleft[1] - bman0.topleft[1]
            bmanx = bman0.topright[0] - bman0.topleft[0]
            bmanx0 = bmanx
            bmany0 = bmany
            sman0 = sman.get_rect()
            smany = sman0.bottomleft[1] - sman0.topleft[1]
            smany = 5
            smanx = sman0.topright[0] - sman0.topleft[0]
            smanx = 350

        sman = pygame.transform.scale(sman, (int(1/2 * smanx), int(0.5 * smany)))
        bman0 = pygame.transform.scale(bman, (int(0.5 * bmanx0), int(0.5 * bmany0)))
        bman = pygame.transform.scale(bman, (int(0.5 * bmanx), int(0.5 * bmany)))

        screen.blit(background, (0, opos[0]))
        screen.blit(background0, (0, opos[1]))
        if opos[0] == -500:
            opos[0] = 500
        if opos[1] == -500:
            opos[1] = 500
        wscene += 1
        opos[7] += 0.1
        opos[4] += 0.1
        opos[7] += 0.1
        opos[0] -= 25
        opos[1] -= 25
        if wscene < 53:
            opos[4] += 25
        if wscene == 53:
            bmany = 5
            opos[7] += 25
            opos[5] += 25
            opos[7] += 85
            #opos[3] -= 50
        screen.blit(sman, (opos[2] - 50, opos[5]))
        screen.blit(bman, (opos[3], opos[7] - 85))
        screen.blit(bman0, (opos[2], opos[4] - 85))

        testtext(wscene, opos[4])
    if scene == 8:
        screen.fill(WHITE)
        if wscene == 0:


            opos[1] = 30
            opos[2] = 180
            opos[3] = False
            opos[4] = False
            opos[5] = 0
            opos[6] = 300
            opos[7] = 150
            opos[8] = 9000
            opos[9] = 9000
            opos[10] = 170
            opos[11] = -500
            lscene[0]= 0
            lscene[1]= 0
            lscene[2]= 0
            lscene[3]= 0
            wscene = 640

            #2 more opos a lot of lscene
            bscene = 2

            foxtxt = "0"
            metatxt = "0"
            baetxt = "0"
            pikatxt = "0"
        if wscene % 2 == 0:
            randnum0 = random.randrange(2, 5)
            randnum1 = [random.randrange(0, 20), random.randrange(15, 100)]
            randnum10 = [random.randrange(0, 20), random.randrange(15, 100)]
            randnum11 = [random.randrange(0, 20), random.randrange(15, 100)]
            randnum12 = [random.randrange(0, 20), random.randrange(15, 100)]
            randnum13 = [random.randrange(0, 20), random.randrange(15, 100)]
            randnum3 = random.randrange(25, 75)
            randnum30 = random.randrange(25, 75)
            randnum31 = random.randrange(25, 75)
            randnum32 = random.randrange(25, 75)
            randnum33 = random.randrange(25, 75)

        background = pygame.image.load("Pictures/dreamland.png").convert_alpha()
        smoke = pygame.image.load("Pictures/smoke.png").convert_alpha()
        botcar = pygame.image.load("Pictures/botcar(2).png").convert_alpha()
        botcar = pygame.transform.rotate(botcar, 90)
        botcar0 = pygame.image.load("Pictures/botcar(3).png").convert_alpha()
        botcar0 = pygame.transform.rotate(botcar0, 90)
        metaknight = pygame.image.load("Pictures/metaknight.png").convert_alpha()
        metasword = pygame.image.load("Pictures/metasword.png").convert_alpha()
        metablm = pygame.image.load("Pictures/metaknight emblem.png").convert_alpha()
        bayonetta = pygame.image.load("Pictures/bayonetta.png").convert_alpha()
        fox = pygame.image.load("Pictures/fox.png").convert_alpha()
        strip = pygame.image.load("Pictures/smoketrip.png").convert_alpha()
        fox = pygame.transform.flip(fox, opos[3], opos[4])
        fox = pygame.transform.rotate(fox, opos[5])
        pikachu = pygame.image.load("Pictures/pika.png").convert_alpha()
        metaknight = pygame.transform.rotozoom(metaknight, 0, 0.9)
        metasword = pygame.transform.rotate(metasword, opos[0])
        bayonetta = pygame.transform.rotozoom(bayonetta, 0, 0.75)
        fox = pygame.transform.rotozoom(fox, 0, 0.95)
        pikachu = pygame.transform.rotozoom(pikachu, 0, 0.5)
        pikaball = pygame.image.load("Pictures/pikaball.png").convert_alpha()
        pikaball = pygame.transform.rotozoom(pikaball, 0, 0.5)
        pikaball0 = pygame.transform.rotozoom(pikaball, 0, randnum3 / 100)
        pikaball1 = pygame.transform.rotozoom(pikaball, 0, randnum30 / 100)
        pikaball2 = pygame.transform.rotozoom(pikaball, 0, randnum31 / 100)
        pikaball3 = pygame.transform.rotozoom(pikaball, 0, randnum32 / 100)
        pikaball4 = pygame.transform.rotozoom(pikaball, 0, randnum33 / 100)

        pikablm = pygame.image.load("Pictures/pikachu emblem.png").convert_alpha()
        foxblm = pygame.image.load("Pictures/foxemblem.png").convert_alpha()
        baeblm = pygame.image.load("Pictures/bayonettaemblem.png").convert_alpha()
        pikablm = pygame.transform.rotozoom(pikablm, 0, 0.75)
        baeblm = pygame.transform.rotozoom(baeblm, 0, 1.5)
        foxblm = pygame.transform.rotozoom(foxblm, 0, 1.1)
        opos[0] += 25
        wscene += 1
        if wscene <= 900:
            if wscene % 8 <= 3 and bscene >= 1:
                opos[3] = False
                opos[1] += 6
            if wscene % 8 > 3 and bscene >= 1:
                opos[3] = True
                opos[1] -= 6
            if wscene % 40 >= 0 and wscene % 40 < 10 and bscene > 1:
                if wscene % 40 >= 5:
                    opos[2] -= 12
            if wscene % 40 >= 30 and wscene % 40 < 40 and bscene > 1:
                if wscene % 40 >= 35:
                    opos[2] += 12
            if wscene % 320 >= 210:
                bscene = 1
                if wscene % 320 + 20 < 230 + 20:
                    if wscene % 4 <= 1:
                        fox = pygame.image.load("Pictures/fox(0).png").convert_alpha()
                elif wscene % 320 + 20 < 240 + 20:
                    opos[2] -= 8
                    opos[1] -= 8
                    fox = pygame.image.load("Pictures/fox(1).png").convert_alpha()
                    fox = pygame.transform.flip(fox, True, opos[4])
                elif wscene % 320 + 20 < 280 + 20:
                    opos[2] += 4
                    if wscene % 4 <= 1:
                        fox = pygame.image.load("Pictures/fox(2).png").convert_alpha()
                elif wscene % 320 < 320:
                    opos[5] -= 36
                    if wscene % 320 < 300:
                        opos[2] -= 3
                        opos[1] += 2
                        if wscene % 320 < 290:
                            opos[2] -= 5
                        if wscene % 320 >= 290:
                            opos[2] += 3
                    elif wscene % 320 < 320:
                        if wscene % 320 < 320:
                            opos[2] += 3
                        if wscene % 320 >= 320:
                            opos[2] -= 5
                            #135.5
                        opos[1] += 2
            if wscene % 320 == 0:
                bscene = 2
        '''
        if wscene % 40 == 0:

        if wscene % 40 == 10:

        if wscene % 40 == 20:

        if wscene % 40 == 30:
        '''
        if wscene % 40 < 10:

            opos[6] = 325
            opos[7] = 150
            opos[8] = 300
            opos[9] = 150
            pikachu = pygame.transform.rotate(pikachu, 0)

        if wscene % 40 < 20 and wscene % 40 >= 10:
            opos[8] = opos[6]
            opos[9] = opos[7]
            opos[6] = 375
            opos[7] = 160
            opos[8] = 375
            opos[9] = 135
            pikachu = pygame.transform.rotate(pikachu, -90)
        if wscene % 40 < 30 and wscene % 40 >= 20:
            opos[8] = opos[6]
            opos[9] = opos[7]
            opos[6] = 300
            opos[7] = 220
            opos[8] = 400
            opos[9] = 220
            pikachu = pygame.transform.rotate(pikachu, -180)
        if wscene % 40 <= 39 and wscene % 40 >= 30:
            opos[8] = opos[6]
            opos[9] = opos[7]
            opos[6] = 300
            opos[7] = 120
            opos[8] = 300
            opos[9] = 215
            pikachu = pygame.transform.rotate(pikachu, -270)
        if wscene >= 800:
            opos[11] += 20
        if wscene == 833:
            opos[11] += 1000









        screen.blit(background, pos)
        screen.blit(metaknight, (100, 250))
        screen.blit(metasword, (115, 240))
        screen.blit(bayonetta, (200, 250))
        screen.blit(fox, (opos[1], opos[2]))
        screen.blit(pikachu, (opos[6], opos[7]))
        screen.blit(pikaball, (opos[8], opos[9]))
        if wscene % 40 < 10:
            if randnum0 >= 2:
                screen.blit(pikaball0, (opos[8] + randnum1[1], opos[9] + 15 - randnum1[0]))
                screen.blit(pikaball1, (opos[8] + randnum10[1], opos[9] + 15 - randnum10[0]))
                screen.blit(pikaball4, (opos[8] + randnum13[1], opos[9] + 15 - randnum13[0]))
            if randnum0 >= 3:
                screen.blit(pikaball2, (opos[8] + randnum11[1], opos[9] + 15  - randnum11[0]))

            if randnum0 >= 4:
                screen.blit(pikaball3, (opos[8] + randnum12[1], opos[9] + 15 - randnum12[0]))
        if wscene % 40 < 20 and wscene % 40 >= 10:
            if randnum0 >= 2:
                screen.blit(pikaball0, (opos[8] + 0 + randnum1[0], opos[9] + randnum1[1]))
                screen.blit(pikaball1, (opos[8] + 0 + randnum10[0], opos[9] + randnum10[1]))
                screen.blit(pikaball4, (opos[8] + 0 + randnum13[0], opos[9] + randnum13[1]))

            if randnum0 >= 3:
                screen.blit(pikaball2, (opos[8] + 0 + randnum11[0], opos[9] + randnum11[1]))
            if randnum0 >= 4:
                screen.blit(pikaball3, (opos[8] + 0 + randnum12[0], opos[9] + randnum12[1]))
        if wscene % 40 < 30 and wscene % 40 >= 20:
            if randnum0 >= 2:
                screen.blit(pikaball0, (opos[8] + 15 -  randnum1[1], opos[9] + 15 - randnum1[0]))
                screen.blit(pikaball1, (opos[8] + 15 - randnum10[1], opos[9] + 15 - randnum10[0]))
                screen.blit(pikaball4, (opos[8] + 15 - randnum13[1], opos[9] + 15 - randnum13[0]))
            if randnum0 >= 3:
                screen.blit(pikaball2, (opos[8] + 15 - randnum11[1], opos[9] + 15  - randnum11[0]))
            if randnum0 >= 4:
                screen.blit(pikaball3, (opos[8] + 15 - randnum12[1], opos[9] + 15 - randnum12[0]))
        if wscene % 40 <= 39 and wscene % 40 >= 30:
            if randnum0 >= 2:
                screen.blit(pikaball0, (opos[8] + 0 + randnum1[0], opos[9] + 15  - randnum1[1]))
                screen.blit(pikaball1, (opos[8] + 0 + randnum10[0], opos[9] + 15 - randnum10[1]))
                screen.blit(pikaball4, (opos[8] + 0 + randnum13[0], opos[9] + 15 - randnum13[1]))
            if randnum0 >= 3:
                screen.blit(pikaball2, (opos[8] + 0 + randnum11[0], opos[9] + 15 - randnum11[1]))
            if randnum0 >= 4:
                screen.blit(pikaball3, (opos[8] + 0 + randnum12[0], opos[9] + 15 - randnum12[1]))
        if wscene % 1 == 0:
            screen.blit(botcar0, (opos[10], opos[11]))
        else:
                screen.blit(botcar, (opos[10], opos[11]))
        if wscene >= 835:
                if wscene <= 840:
                    lscene[0] += 3
                for i in range(lscene[0]):
                    i += 1
                    smoke = pygame.image.load("Pictures/smoke.png").convert_alpha()
                    smoke = pygame.transform.rotozoom(smoke, 0, i/2.5)
                    lscene[1] = i * 16

                screen.blit(smoke, (200 - lscene[1], 180 - lscene[1]))
                if wscene >= 845 and wscene < 900:
                    screen.blit(strip, (opos[1]+30, opos[2]+20))
                if wscene == 900:
                    lscene[2] = 0

            #Look into python layers and shapes. Find one tht can increase transparency.
        if wscene >= 833 and wscene <= 840:
            baetxt = "999"

            explosion(wscene, 0, 0, 4)



        screen.blit(foxblm, (20, 300))
        screen.blit(metablm, (120, 290))
        screen.blit(pikablm, (310, 290))
        screen.blit(baeblm, (215, 300))

        text(foxtxt + "%", 95, 335, fontObj, 0, WHITE)
        text(metatxt + "%", 205, 335,  fontObj, 0, WHITE)
        if wscene < 836:
            if wscene < 833:
                text(baetxt + "%", 290, 335, fontObj, 0, WHITE)
            if wscene >= 833:
                text(baetxt + "%", 290, 335, fontObj, 0, DRED)

        text(pikatxt + "%", 385, 335, fontObj, 0, WHITE)
        if wscene >= 836:
            if wscene < 842:
                explosion(lscene[2], 240, 275, 0.75)
                lscene[2]+= 1
        if wscene < 848 and wscene >= 838:
                blast(lscene[3], 180, -40, 0.75, -150)
                lscene[3] += 1

        if wscene >= 900 and wscene < 907:
            explosion(lscene[2], opos[1], opos[2], 1)
            lscene[2] += 1
        elif wscene >= 907:
            opos[1] += 20
            opos[2] += 20
        if wscene >= 910:
            scene = 9
            opos[1] = 30
            opos[2] = 180
            opos[3] = False
            opos[4] = False
            opos[5] = 0
            opos[6] = 300
            opos[7] = 150
            opos[8] = 9000
            opos[9] = 9000
            opos[10] = 170
            opos[11] = -500
            lscene[0]= 0
            lscene[1]= 0
            lscene[2]= 0
            lscene[3]= 0
            wscene = 0
        testtext(wscene, opos[2])
    if scene == 9:
        if wscene == 0:
            opos[1] = 300
            opos[2] = 200
            opos[3] = -(1257 *1)
            opos[4] = (-1158 *1)
            opos[6] = 0
        screen.fill(WHITE)
        background = pygame.image.load("Pictures/sky.png").convert_alpha()
        background = pygame.transform.rotozoom(background, 0, 4)
        fox = pygame.image.load("Pictures/fox.png").convert_alpha()
        '''
        smoke = pygame.image.load("Pictures/smoke.png").convert_alpha()
        '''
        fox = pygame.transform.rotozoom(fox, 45, 2)
        '''
        smoke = pygame.transform.rotozoom(smoke, 0, 0.5)
        '''
        wscene += 1
        opos[1] -= 8
        opos[2] -= 8
        opos[3] += 20
        opos[4] += 20
        opos[6] += 1



        screen.blit(background, (opos[3], opos[4]))

        screen.blit(fox, (opos[1], opos[2]))
        '''
        for opos[5] in range(opos[6]):

            screen.blit(smoke, (opos[1] + 180 + (opos[5] * opos[5] * 10), opos[2] + 180  + (opos[5] * opos[5] * 10)))
        '''
        smoke(opos[6], opos[1] + 170, opos[2] + 180, 2, 45)
        testtext(wscene, opos[2])
        if wscene >= 50:
            scene = 10
            opos[0] = 2
            opos[1] = 400
            opos[2] = 600
            opos[3] = 4
            opos[4] = 45
            opos[5] = 0.05
            opos[6] = -200
            opos[7] = -200
            lscene[0] = 0
            wscene = 0
    if scene == 10:
        stop = 0

        if wscene == 0:
            wscene = 0
            opos[0] = 2
            opos[1] = 400
            opos[2] = 600
            opos[3] = 4
            opos[4] = 45
            opos[5] = 0.05
            opos[6] = -200
            opos[7] = -200
            opos[8] = 225
            opos[9] = -550
            opos[11] = 580
            opos[12] = 475
            opos[13] = -89.5
            opos[14] = 0
            opos[17] = 450
            opos[18] = 0

            temppos1 = opos[11]
            temppos2 = opos[12]
            sdura = 15
            sspeed = 0
            mspeed = 0
            scons = 5
            topos6 = opos[6]
            topos7 = opos[7]
            topos9 = opos[9]
            topos13 = opos[13]
            topos3 = opos[3]
            topos11 = opos[11]
            topos12 = opos[12]
            #298, 291

            lscene[0] = 0
            lscene[1] = 0
            lscene[2] = 5
            lscene[3] = 0
            lscene[4] = 0
            lscene[6] = 0
            opos[10] = 400


        if lscene[0] == 0:
            wscene += 1

        screen.fill(SBLUE)
        if lscene[1] > 510:
            screen.fill(BLACK)
        topos1 = opos[1]
        topos2 = opos[2]



        background = pygame.image.load("Pictures/skyislands.png").convert_alpha()
        if lscene[1] < 460:
            background0 = background
        background = pygame.transform.rotozoom(background, 0, opos[3])
        blaster = pygame.image.load("Pictures/blaster.png").convert_alpha()
        blaster = pygame.transform.rotozoom(blaster, opos[18], opos[0])

        if lscene[1] <= 120:
            hood = pygame.image.load("Pictures/hood(3).png").convert_alpha()
        else:
            hood = pygame.image.load("Pictures/hood(0).png").convert_alpha()
        fox = pygame.image.load("Pictures/fox.png").convert_alpha()
        background1 = pygame.image.load("Pictures/cfox.png").convert_alpha()
        fox = pygame.transform.rotozoom(fox, opos[4], opos[0])
        #hood = pygame.transform.rotozoom(hood, 0, opos[0]/1.1)
        if stop == 0:
            if wscene <= 80:
                topos3 = opos[3]
            topos6 /= topos3
            topos9 /= topos3
            opos[6] /= topos3
            opos[9] /= topos3

            if lscene[1] < 125:
                if opos[6] >= (437):
                    opos[6] = (-447)
                if opos[9] >= (437):
                    opos[9] = (-447)
            if lscene[1] >= 125:
                if topos6 >= 448:
                    topos6 = -450
                if topos9 >= 448:
                    topos9 = -450
            opos[6] *= opos[3]
            opos[9] *= opos[3]
            topos6 *= opos[3]
            topos9 *= opos[3]


            if wscene <= 80: # and wscene % 3 == 0
                opos[3] -= opos[5]
                opos[0] -= opos[5]/1.5
                opos[5] *= 0.99
                opos[6] *= 0.99
                opos[7] *= 0.99
                opos[1] -= 1


                if wscene == 80:
                    #opos[7] = 0
                    opos[9] += opos[6]
            if lscene[0] == 0:
                opos[1] -= 0.5
            if wscene > 80 and lscene[1] <= 5:

                opos[6] += 2.24
                opos[9] += 2.24
            if wscene > 80:
                    if lscene[1] < 465:
                        background0 = background
                    topos3 = opos[3]
                    opos[7] = opos[13]

            if lscene[0] > 0 and lscene[1] <= 20:
                if wscene % 4 <= 1:
                    fox = pygame.image.load("Pictures/fox(0).png").convert_alpha()
                    fox = pygame.transform.rotozoom(fox, opos[4], opos[0])
                opos[2] += 0.5
            elif lscene[0] > 0 and lscene[1] <= 40:
                        opos[2] -= 2
                        opos[1] += 2
                        fox = pygame.image.load("Pictures/fox(1).png").convert_alpha()
                        fox = pygame.transform.flip(fox, False, False)
                        fox = pygame.transform.rotozoom(fox, opos[4], opos[0])
            elif lscene[0] > 0 and lscene[1] <= 80:
                        opos[2] = 0.005 * (opos[10] - 178) * (opos[10] - 178) + 200
                        opos[10] += 10
                        opos[1] += 3
                        opos[4] += 24
                        opos[3] *= 1.02
                        opos[6] -= 5
                        opos[9] -= 5
                        opos[13] -= 5
                        opos[0] *= 1.05
                        if lscene[1] % 15 == 0:
                            opos[10] = 124.5
                        if lscene[1] >= 75:
                            #298, 291
                            opos[11] -= 50
                            opos[12] -= 50
            elif lscene[0] > 0 and lscene[1] <= 2290:
                fox = pygame.image.load("Pictures/fox(3).png").convert_alpha()


                if lscene[1] <= 95 and lscene[1] > 85:
                    opos[1] -= 40
                    opos[2] -= 15

                    temppos1 = opos[11]
                    temppos2 = opos[12]
                    opos[10] = 200
                    hood = pygame.image.load("Pictures/hood(4).png").convert_alpha()
                    #hood = pygame.transform.rotozoom(hood, opos[14], opos[0])
                if lscene[1] > 95 and lscene[1] <= 120:
                        opos[12] = 0.001 * (opos[10]-330)*(opos[10]-330)+130
                        opos[11] += 1
                        opos[10] += 20
                        opos[3] *= 0.998
                        opos[0] *= 0.98
                        opos[13] -= 10
                        opos[6] -= 12
                        opos[9] -= 12
                        if lscene[1] <= 105:
                            opos[14] += 36
                        if lscene[1] % 121 < 95:
                            hood = pygame.image.load("Pictures/hood(0).png").convert_alpha()

                        elif lscene[1] % 121 < 100:
                            hood = pygame.image.load("Pictures/hood(1).png").convert_alpha()
                        elif lscene[1] % 121 < 105:
                            hood = pygame.image.load("Pictures/hood(2).png").convert_alpha()
                        else:
                            hood = pygame.image.load("Pictures/hood.png").convert_alpha()
                        #opos[6] = 0
                        #opos[7] = 0
                        #opos[9] = 0
                        #opos[13] = 0
                        topos11 = opos[11]
                        topos12 = opos[12]
                        mspeed = 0



                elif lscene[1] > 120:

                    if lscene[1] > 125:
                        mspeed -= 20



                        if lscene[4] == 3:
                            sdura -= 1
                            sspeed -= 10
                        if lscene[1] >= 465:
                            sspeed += 30
                        if lscene[1] >= 466 and lscene[1] < 471:
                            opos[12] -= 6
                            opos[14] += 72
                        elif lscene[1] >= 471 and lscene[1] < 476:
                            opos[12] += 6

                    if lscene[1] == 121:
                        opos[10] = 305

                        #opos[8] = 252.5 * opos[3]
                        opos[8] = 1
                        opos[15] = 0.005 / opos[3]
                        opos[16] = 386
                        topos6 = opos[6] - (419 - (450 * opos[3]))
                        topos7 = opos[7] - (386 - (386 * opos[3]))
                        topos9 = opos[9] - (419 - (450 * opos[3]))
                        topos13 = opos[13] -(386 - (386 * opos[3]))
                        #topos6 = 0
                        #topos7 = 0
                        #topos9 = 0
                        #topos13 = 0
                        opos[1] = opos[11] - 419
                        opos[2] = opos[12] - 50






                    if lscene[4] >= 2:
                            background = pygame.image.load("Pictures/skyislands(0).png").convert_alpha()
                            background = pygame.transform.rotozoom(background, 0, opos[3])
                    if lscene[1] >= 360 and lscene[1] < 500:
                        fox = pygame.image.load("Pictures/fox.png").convert_alpha()
                        opos[4] = 0
                    if lscene[1] >= 465 and lscene[1] < 468:
                            fox = pygame.image.load("Pictures/fox(2).png").convert_alpha()

                    if lscene[1] > 125 and lscene[4] < 3:

                        '''
                        if lscene[1] % 120 == 6:
                            opos[0] += 0.15
                        if lscene[1] % 120 == 96:
                            opos[0] -= 0.15
                        '''
                        if lscene[1] % 120 < 6:
                            hood = pygame.image.load("Pictures/hood(0).png").convert_alpha()
                        elif lscene[1] % 120 <= 10:
                            hood = pygame.image.load("Pictures/hoodfp(0).png").convert_alpha()
                        elif lscene[1] % 120 < 16:
                            hood = pygame.image.load("Pictures/hoodfp(0.5).png").convert_alpha()
                        elif lscene[1] % 120 <= 21:
                            hood = pygame.image.load("Pictures/hoodfp(1).png").convert_alpha()
                        elif lscene[1] % 120 <= 71:
                            hood = pygame.image.load("Pictures/hoodfp(2).png").convert_alpha()
                            opos[14] -= 1.8
                        elif lscene[1] % 120 <= 91:
                            hood = pygame.image.load("Pictures/hoodfp(3).png").convert_alpha()
                            opos[14] -= 31.5
                        elif lscene[1] % 120 <= 96:

                            hood = pygame.image.load("Pictures/hood(1).png").convert_alpha()
                        elif lscene[1] % 120 <= 98:
                            hood = pygame.image.load("Pictures/hood(2).png").convert_alpha()
                        elif lscene[1] % 120 <= 100:
                            hood = pygame.image.load("Pictures/hood.png").convert_alpha()
                        else:
                            hood = pygame.image.load("Pictures/hood(0).png").convert_alpha()
                        if opos[3] >= 1.2367:
                            opos[3] *= 0.998
                            opos[0] *= 0.998
                        if opos[16] < 406:
                            opos[16] += 0.1


                        if lscene[1] < 351 and lscene[1] >= 329:
                                opos[1] += 10
                                opos[2] += 5
                                fox = pygame.image.load("Pictures/fox.png").convert_alpha()
                                opos[4] = 0
                        elif lscene[1] >= 351 and lscene[1] < 360:
                                opos[1] -= 25
                                opos[2] -= 5
                                mspeed += 900
                                fox = pygame.image.load("Pictures/fox(3).png").convert_alpha()
                                opos[4] = -90

                        if lscene[1] == 360:
                            opos[1] = -250
                            opos[2] = 330.80075


                        if (lscene[1]) % 120 >= 6 and (lscene[1]) % 120 < 48:
                            #opos[3] *= 0.9975
                            #opos[0] *= 0.9975
                            #topos7 += 2
                            #topos13 += 2
                            opos[12] = ((opos[15] * opos[3]) * ((opos[10]) - (725)) * (opos[10]-(305))) + (252.5 * opos[8])
                            if lscene[4] == 0:
                                if lscene[1] % 120 < 27:
                                    topos6 += (12/1.0835 * 0.4)
                                    topos9 += (12/1.0835 * 0.4)
                                else:
                                    topos6 += (12/1.0835 * 1.2)
                                    topos9 += (12/1.0835 * 1.2)
                            if lscene[4] == 1:
                                if lscene[1] % 120 < 27:
                                    topos6 += (12/1.425 * 0.4)
                                    topos9 += (12/1.425 * 0.4)
                                else:
                                    topos6 += (12/1.425 * 1.2)
                                    topos9 += (12/1.425 * 1.2)

                            if lscene[4] == 2:
                                if lscene[1] % 120 < 27:
                                    topos6 += (12/2.2 * 0.4)
                                    topos9 += (12/2.2 * 0.4)
                                    if lscene[1] >= 360:
                                        opos[1] += (12/2.2 * 0.4)
                                else:
                                    topos6 += (12/2.2 * 1.2)
                                    topos9 += (12/2.2 * 1.2)
                                    opos[1] += (12/2.2 * 1.2)



                            #topos7 -= (1/opos[3])
                            #topos13 -= (1/opos[3])
                            if lscene[1] % 120 < 27:
                                opos[10] += 2
                                opos[12] += 1
                            else:
                                opos[10] += 6
                                opos[12] -= (1/3)
                            #opos[11] -= 1
                            topos6 += 1
                            topos9 += 1
                            opos[8] *= 1.001

                        elif (lscene[1]) % 120 <= 90 and lscene[1] % 120 > 6:
                            #opos[3] *= 1.0025
                            #opos[0] *= 1.0025
                            #topos7 -= 2
                            #topos13 -= 2
                            opos[12] = ((opos[15] * opos[3]) * ((opos[10]) - (725)) * (opos[10]-(305))) + (252.5 * opos[8])
                            if lscene[4] == 0:
                                topos6 += (12/1.0835 * 1.2)
                                topos9 += (12/1.0835 * 1.2)
                            if lscene[4] == 1:
                                topos6 += (12/1.3 * 1.2)
                                topos9 += (12/1.3 * 1.2)
                            if lscene[4] == 2:
                                topos6 += (12/2 * 1.2)
                                topos9 += (12/2 * 1.2)
                                opos[1] += (12/2 * 1.2)

                            #topos7 -= (1/opos[3])
                            #topos13 -= (1/opos[3])
                            opos[10] += 6
                            #opos[11] -= 1
                            topos6 += 1
                            topos9 += 1
                            topos11 = opos[11]
                            topos12 = opos[12]
                            opos[8] *= 1.001
                            opos[12] -= (1/3)
                        elif lscene[1] % 120 == 100:
                            mspeed = 0
                            sspeed = 0
                            if lscene[4] == 2:
                                mspeed = 10000
                            opos[10] = 305

                            lscene[4] += 1







                        #Get ready to zoom in for the final battle.



                        #213







                        #opos[13] = -0.001 * (opos[10]-530) * (opos[10]-530) + 550
                        #1157 (o7 and o13)
                        #1295 o6
                        #1849 o9
                        #305 o11
                        #252.5 o12
                    #opos[6] += 5
                    #opos[9] += 5

                    opos[6] = (419 - (450 * opos[3])) + topos6
                    opos[7] = (386 - (opos[16] * opos[3])) + topos7
                    opos[9] = (419 - (450 * opos[3])) + topos9
                    opos[13] = (386 - (opos[16] * opos[3])) + topos13
                if lscene[1] >= 465:

                    sspeed += 10
                    if lscene[1] == 465:
                        opos[2] = opos[12] - 5
                    background = pygame.image.load("Pictures/skyislands(0).png").convert_alpha()
                    if lscene[1] == 495:
                        opos[3] = 1
                        topos7 -= 300
                        topos6 -= 250
                        #opos[11] -= 75
                        #opos[12] -= 60

    #Make Fox hits Hood down.
    #Hood gets up
    #Fox uses lazor, Omae wa
    #Hood stops time
    #Fox scurries about
    #Fox kicks Hood in the nuts
    #Hood reveals trap card
    #Everything goes to hell.








                    if lscene[1] >= 495:
                        background = pygame.image.load("Pictures/skyislands(2).png").convert_alpha()
                        #if lscene[1] < 525:
                            #opos[11] += 2
                            #opos[12] -= 2
                    background = pygame.transform.rotozoom(background, 0, opos[3])
                    if lscene[1] <= 510:
                        opos[0] *= 1.035
                        opos[3] *= 1.035
                        opos[11] -= 1.5
                        opos[1] -= 1.5
                        opos[12] -= 2.25
                        opos[2] -= 2.25
                        opos[17] -= 1.6
                        opos[16] -= 2.2
                        topos6 += 0
                        topos7 += 0
                        if lscene[1] > 493:
                            opos[11] += 3
                            opos[1] += 3
                            opos[12] += 4.5
                            opos[2] += 2.5
                            opos[17] += 2.5
                            opos[16] += 3.4
                            if lscene[1] < 510:
                                opos[11] -= 1.5
                                opos[1] -= 1.5
                                opos[12] -= 2
                                opos[2] -= 2
                                opos[17] += 0.5
                                opos[16] -= 1
                                if lscene[1] > 505:
                                    opos[11] -= 1
                                    opos[1] -= 1
                                    opos[12] -= 1
                                    opos[2] -= 1
                                    opos[17] += 0.5
                                    opos[16] -= 1

                    if lscene[1] < 510 and lscene[1] >= 475:
                        opos[16] += 0.15
                    if lscene[1] < 510 and lscene[1] >= 485:
                        opos[16] += 0.35
                    if lscene[1] < 510 and lscene[1] >= 495:
                        opos[16] += 0.50
                    #if lscene[1] < 510 and lscene[1] >= 505:
                        #opos[16] += 0.65

                    '''
                    elif lscene[1] < 510 and lscene[1] >= 500:
                        opos[0] *= 1.05
                        opos[3] *= 1.05
                        opos[11] -= 3
                        opos[12] -= 4.5
                        opos[17] -= 14
                        opos[16] -= 18
                    '''



                    #if lscene[1] == 515:
                        #topos7 -= 10
                    #if lscene[1] == 540:
                        #topos6 -= 50
                        #topos7 -= 40
                        #Fix the zooming in.
                    #if lscene[1] < 485:
                        #opos[1] -= 0.2
                        #opos[2] -= 0.65
                    if lscene[1] >= 485:
                        fox = pygame.image.load("Pictures/afox.png").convert_alpha()
                        fox = pygame.transform.flip(fox, True, False)
                        if lscene[1] == 485:
                            opos[1] = opos[11] + 5
                    if lscene[1] >= 492 and lscene[1] < 497:
                        if lscene[1] < 493:
                            fox = pygame.image.load("Pictures/afox(1).png").convert_alpha()
                        elif lscene[1] < 495:
                            fox = pygame.image.load("Pictures/afox(2).png").convert_alpha()
                        elif lscene[1] < 496:
                            fox = pygame.image.load("Pictures/afox(1).png").convert_alpha()
                        elif lscene[1] < 497:
                            fox = pygame.image.load("Pictures/afox(3).png").convert_alpha()


                        fox = pygame.transform.flip(fox, True, False)
                    if lscene[1] >= 489 and lscene[1] <= 492:
                            opos[1] += 2.5
                    if lscene[1] >= 495:
                        hood = pygame.image.load("Pictures/hoodf.png").convert_alpha()
                        if lscene[1] == 495:
                            opos[14] = 25
                        #elif lscene[1] < 501:
                         #   hood = pygame.image.load("Pictures/hoodf(2).png").convert_alpha()
                        if lscene[1] < 498:
                            opos[14] -= 30
                            opos[12] += 0
                            opos[11] -= 50
                        if lscene[1] > 496 and lscene[1] < 510:
                            opos[1] -= 1





    #Get rid of lag




                    if lscene[1] <= 490 and lscene[1] >= 480:
                        if lscene[1] % 2 == 0:
                            fox = pygame.image.load("Pictures/null.png").convert_alpha()
                    if lscene[1] < 528 and lscene[1] >= 518:
                    	opos[18] += 144
                    #if lscene[1] == 509:
                        #print("o6. " + str(opos[6]))
                        #print("o7. " + str(opos[7]))
                        #print("t6. " + str(topos6))
                        #print("t7. " + str(topos7))
                    #if lscene[1] == 510:
                        #topos6 += 0
                        #print("o6. " + str(opos[6]))
                        #print("o7. " + str(opos[7]))
                        #print("t6. " + str(topos6))
                        #print("t7. " + str(topos7))
                    if lscene[1] == 511:
                        topos7 += 400
                        topos6 += 0
                        #print("o6. " + str(opos[6]))
                        #print("o7. " + str(opos[7]))
                        #print("t6. " + str(topos6))
                        #print("t7. " + str(topos7))
                    if lscene[1] == 512:
                        topos6 -= 39

                        #print("o6. " + str(opos[6]))
                        #print("o7. " + str(opos[7]))
                        #print("t6. " + str(topos6))
                    if lscene[1] > 510:
                        #print(opos[3])
                        opos[3] = 1
                        background = pygame.image.load("Pictures/skyislands(1).png").convert_alpha()
                        background = pygame.transform.rotozoom(background, 0, 1)

                    if lscene[1] > 535:

                        #Make it a really small one.

                        fox = pygame.image.load("Pictures/afox(0).png").convert_alpha()
                        fox = pygame.transform.flip(fox, True, False)
                        hood = pygame.image.load("Pictures/hoodf(0).png").convert_alpha()

                    if lscene[1] > 600 and lscene[1] < 680:

                        fox = pygame.image.load("Pictures/afox.png").convert_alpha()
                        fox = pygame.transform.flip(fox, True, False)
                    if lscene[1] > 538:
                        hood = pygame.image.load("Pictures/hoodf(1).png").convert_alpha()
                    if lscene[1] > 540 and lscene[1] <= 553:
                        stop = 1
                    elif lscene[1] > 553 and lscene[1] <= 559:
                        hood = pygame.image.load("Pictures/hoodf(2).png").convert_alpha()
                        if lscene[1] <= 557:
                            fox = pygame.image.load("Pictures/afoxk.png").convert_alpha()
                            fox = pygame.transform.flip(fox, True, False)
                        else:

                            fox = pygame.image.load("Pictures/afoxk(0).png").convert_alpha()
                            fox = pygame.transform.flip(fox, True, False)
                    elif lscene[1] > 559 and lscene[1] <= 598:
                        hood = pygame.image.load("Pictures/hoodf(2).png").convert_alpha()
                        if lscene[1] == 560:
                            fox = pygame.image.load("Pictures/afoxk.png").convert_alpha()
                            fox = pygame.transform.flip(fox, True, False)
                        elif lscene[1] > 560:
                            if lscene[1] % 10 >= 5:
                                fox = pygame.image.load("Pictures/afoxk(0).png").convert_alpha()
                            else:
                                fox = pygame.image.load("Pictures/afoxk.png").convert_alpha()
                            fox = pygame.transform.flip(fox, True, False)
                            if lscene[1] > 572:
                                fox = pygame.image.load("Pictures/afoxk(1).png").convert_alpha()
                                fox = pygame.transform.flip(fox, True, False)
                            if lscene[1] <= 583 and lscene[1] > 580:

                                opos[4] -= 50
                                opos[2] -= 5
                    if lscene[1] >= 561 and lscene[1] < 568:
                        stop = 2







                    opos[6] = (419 - (opos[17] * opos[3])) + topos6
                    opos[7] = (386 - (opos[16] * opos[3])) + topos7
                    opos[9] = (419 - (opos[17] * opos[3])) + topos9
                    opos[13] = (386 - (opos[16] * opos[3])) + topos13

#Just make it zoom in...




                fox = pygame.transform.rotozoom(fox, opos[4], (opos[0] * 1.2))















        if lscene[0] == 0:
            if wscene % 353 <= 352:
                #opos[1] -= 10 * opos[0]
                #opos[2] -= 10 * opos[0]

                opos[4] += (17/18)
                opos[2] = 0.01 * (opos[10]-opos[8]) * (opos[10]-opos[8])
                opos[10] -= 1
                opos[1] -= 0
                if wscene % 353 == 352:
                    opos[8] = opos[10] - 175
        if lscene[1] >= 568 and lscene[1] <= 572:
                background = pygame.transform.rotozoom(background, (lscene[6]) * 5, 2)
                background = pygame.transform.rotozoom(background, (lscene[6]) * 1/5, 1/2)
                background = pygame.transform.rotozoom(background, (lscene[6]) * 5, 2)
                background = pygame.transform.rotozoom(background, (lscene[6]) * 1/5, 1/2)
        screen.blit(background, (opos[6], opos[7]))
        if lscene[1] < 465:
            screen.blit(background0, (opos[9], opos[13]))
        else:
            background0 = pygame.image.load("Pictures/null.png")
            screen.blit(background0, (opos[9], opos[13]))









#Test the zoom in function in 69
#Internet Test












        hood = pygame.transform.rotozoom(hood, opos[14], opos[0]/1.1)
        hood = pygame.transform.flip(hood, True, False)

        if lscene[1] < 480:
            screen.blit(hood, (opos[11], opos[12]))
        if lscene[1] >= 568 and lscene[1] <= 572:
                fox = pygame.transform.rotozoom(fox, (lscene[6]) * 5, 2)
                fox = pygame.transform.rotozoom(fox, (lscene[6]) * 1/5, 1/2)
                fox = pygame.transform.rotozoom(fox, (lscene[6]) * 5, 2)
                fox = pygame.transform.rotozoom(fox, (lscene[6]) * 1/5, 1/2)
        screen.blit(fox, (opos[1], opos[2]))
        if lscene[1] >= 480 and lscene[1] <= 572:
            if lscene[1] >= 568:
                hood = pygame.transform.rotozoom(hood, (lscene[6]) * 5, 2)
                hood = pygame.transform.rotozoom(hood, (lscene[6]) * 1/5, 1/2)
                hood = pygame.transform.rotozoom(hood, (lscene[6]) * 5, 2)
                hood = pygame.transform.rotozoom(hood, (lscene[6]) * 1/5, 1/2)
            screen.blit(hood, (opos[11], opos[12]))

        if lscene[1] >= 508:
            blaster = pygame.transform.flip(blaster, False, False)
            screen.blit(blaster, (opos[11] + 182, opos[12] + 30))
        if lscene[1] >= 554 and lscene[1] <= 572:
            garrow = pygame.image.load("Pictures/garrow.png").convert_alpha()
            garrow = pygame.transform.rotozoom(garrow, 160, opos[0])
            if lscene[1] >= 568:
                garrow = pygame.transform.rotozoom(garrow, (lscene[6]) * 5, 2)
                garrow = pygame.transform.rotozoom(garrow, (lscene[6]) * 1/5, 1/2)
                garrow = pygame.transform.rotozoom(garrow, (lscene[6]) * 5, 2)
                garrow = pygame.transform.rotozoom(garrow, (lscene[6]) * 1/5, 1/2)
            screen.blit(garrow, (opos[11] + 132, opos[12] + 47))
            gravity = pygame.image.load("Pictures/gravity.png").convert_alpha()
            gravity = pygame.transform.rotozoom(gravity, (lscene[6]) * 5, (lscene[6]) * 0.5)
            #Implement gravity before the kick starts.

            '''
            if lscene[1] == 582:
                gravity = pygame.transform.rotozoom(gravity, (lscene[6]) * 5, 2)
                gravity = pygame.transform.rotozoom(gravity, (lscene[6]) * 1/5, 1/2)
                gravity = pygame.transform.rotozoom(gravity, (lscene[6]) * 5, 2)
                gravity = pygame.transform.rotozoom(gravity, (lscene[6]) * 1/5, 1/2)
                '''
            screen.blit(gravity, (opos[11] + 210 - (lscene[6] * 50), opos[12] + 100 - (lscene[6] * 50)))
        if lscene[1] > 80 and lscene[1] <= 85:
            screen.fill(BLACK)
            screen.blit(background1, (0, + 40))
        '''
        if lscene[1] > 85 and lscene[1] <= 90:
            smoke((lscene[1] - 1), opos[1] + 80, opos[2] + 30, (opos[0] * 1), 90)
        '''
        if lscene[1] > 351 and lscene[1] < 360:
            smoke((lscene[1] - 2), opos[1] + 50, opos[2] + 12.5, (opos[0] * 1), 270)
        if lscene[1] > 125:
            multi(mspeed, topos11, topos12 + (35 * opos[0]), opos[0]/1.1, 180)
        if sdura > 0:
            tsspeed = sspeed
        if lscene[4] == 3:
            scatter(sdura, tsspeed, sspeed, topos11, topos12 + (35 * opos[0]), opos[0]/1.1, 180)
        '''
        lscene[2] += 1
        if lscene[2] % 5 == 0:
            lscene[2] = 0
        for i in range(lscene[2]):
            smoke = pygame.image.load("Pictures/smoke.png").convert_alpha()
            smoke = pygame.transform.rotozoom(smoke, 0, opos[0]/10)
            lscene[3] = i * 16
            if opos[1] > topos1 and opos[2] > topos2:
                screen.blit(smoke, (opos[1] + lscene[3], opos[2] + lscene[3]))
            if opos[1] > topos1 and opos[2] == topos2:
                screen.blit(smoke, (opos[1] + lscene[3], opos[2] + 0))
            if opos[1] > topos1 and opos[2] < topos2:
                screen.blit(smoke, (opos[1] + lscene[3], opos[2] - lscene[3]))
            if opos[1] == topos1 and opos[2] < topos2:
                screen.blit(smoke, (opos[1] + 0, opos[2] - lscene[3]))
            if opos[1] < topos1 and opos[2] < topos2:
                screen.blit(smoke, (opos[1] - lscene[3], opos[2] - lscene[3]))
            if opos[1] < topos1 and opos[2] == topos2:
                screen.blit(smoke, (opos[1] - lscene[3], opos[2] + 0))
            if opos[1] < topos1 and opos[2] > topos2:
                screen.blit(smoke, (opos[1] - lscene[3], opos[2] + lscene[3]))
            if opos[1] == topos1 and opos[2] > topos2:
                screen.blit(smoke, (opos[1] + lscene[3], opos[2] + lscene[3]))
            # do this with 8 directions.
        '''



        if stop == 1:
            lscene[6] += 2
            progex("Stay down.", lscene[6], "tfox", "bahnschrift")
            if lscene[6] == 26:
                lscene[6] = 0
                stop = 0
        if stop == 2:
            lscene[6] += 10




#pause at 364, and fire up and have hood combo fox back

        if wscene == 364:
            lscene[0] = 1
            if lscene[1] == 0:
                opos[10] = 124.5
            lscene[1] += 1
        testtext0(lscene[1],lscene[6])
        testtext(opos[7], stop)




#topos6: -2460.2703
#topos7: -1156.82965
#topos9: -1295.4327
#topos7: -1156.82965
#opos[0]: 0.673
#opos[3]: 2.5993
#opos[6]: 1709.5855
#opos[9]: 544.74785
#opos[7]: -539.5
#opos[13]: -539.5
#opos[11]: 305
#opos[12]: 252.5



    if scene == 69:
#think about how much space the screen takes up

        if wscene == 0:
            wscene = 0
            opos[0] = 0.673
            opos[3] = 1
            opos[6] = 1709.5855
            opos[9] = 544.74785
            opos[7] = -539.5
            opos[13] = -539.5
            opos[11] = 305
            opos[12] = 252.5
            topos3 = opos[3]
            topos6 = -2460.2703
            topos7 = -1156.82965
            topos9 = -1295.4327
            topos13 = -1156.82965
            sdura = 10
            sspeed = 0
            background = pygame.image.load("Pictures/hood.png").convert_alpha()

        screen.fill(WHITE)
        '''
        background = pygame.image.load("Pictures/skyislands(0).png").convert_alpha()

        hood =
        if wscene % 120 <= 5:
            hood = pygame.image.load("Pictures/hoodfp(0).png").convert_alpha()
        elif lscene[1] % 120 <= 15:
            hood = pygame.image.load("Pictures/hoodfp(0).png").convert_alpha()
        elif wscene % 120 <= 40:
            hood = pygame.image.load("Pictures/hoodfp(1).png").convert_alpha()
        elif wscene % 120 <= 60:
            hood = pygame.image.load("Pictures/hoodfp(2).png").convert_alpha()
            opos[4] -= 4.5
        elif wscene % 120 <= 80:
            hood = pygame.image.load("Pictures/hoodfp(3).png").convert_alpha()
            opos[4] -= 31.5
        elif wscene % 120 <= 84:
            hood = pygame.image.load("Pictures/hood(1).png").convert_alpha()
        elif wscene % 120 <= 88:
            hood = pygame.image.load("Pictures/hood(2).png").convert_alpha()
        elif wscene % 120 <= 110:
            hood = pygame.image.load("Pictures/hood.png").convert_alpha()
        else:
            hood = pygame.image.load("Pictures/hood(0).png").convert_alpha()

        if wscene % 120 >= 110:
            background = pygame.image.load("Pictures/skyislands(0).png").convert_alpha()
        '''

        background = pygame.transform.rotozoom(background, 0, 1)
        background0 = pygame.image.load("Pictures/null.png")

        opos[6] /= topos3
        opos[9] /= topos3
        if opos[6] >= (450):
            opos[6] = -450
        if opos[9] >= (450):
            opos[9] = -450

        sdura -= 1
        sspeed += 20
        opos[6] *= opos[3]
        opos[9] *= opos[3]
        '''
        topos6 = (419 - (450 * opos[3])) + opos[6]
        topos7 = (386 - (386 * opos[3])) + opos[7]
        topos9 = (419 - (450 * opos[3])) + opos[9]
        topos13 = (386 - (386 * opos[3])) + opos[13]
        '''
        '''
        opos[6] = 0
        opos[7] = 0
        '''
        #topos6 += (5 * opos[3])
        #topos9 += (5 * opos[3])
        wscene += 1

        background = pygame.transform.scale(background, (523, 421))



        screen.blit(background, (0, 100))
        screen.blit(background0, (opos[9], opos[13]))
        #screen.blit(hood, (opos[11], opos[12]))
        if wscene == 1:
            print(pygame.font.get_fonts())
        progex("Hey this is a long test text", wscene, "hood", "bahnschrift")
        #make a testtext0 for extra variables cause you don;t use normal debugging

        testtext(wscene, wscene)
        testtext0(opos[9], opos[13])
        if sdura > 0:
            tsspeed = sspeed
        scatter(sdura, tsspeed, sspeed, -50, 200, 1, 0)

    pygame.display.flip()
    clock.tick(FPS)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
