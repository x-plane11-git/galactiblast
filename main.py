#sideShooter.py
from pygame import *
from random import *

width,height=800,600
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
rapid=20

def drawScene(screen,g,bull,targ):
    screen.fill((255,255,0))
    
    for b in bull:
        brect=Rect(b[0],b[1],10,10)#bullets size is 10x10
        draw.rect(screen,(0,0,255),brect)
    for t in targ:
        draw.rect(screen,(0,0,255),t)
    draw.circle(screen,(255,0,0),(50,g[1]),20)
    display.flip()


def moveBullets(bull):
    for b in bull:
        b[0]+=b[2]#horizontal movement
        b[1]+=b[3]#vertical movement
        if b[0]>800:#off-screen
            bull.remove(b)

def checkHits(bull,targ):
    for b in bull:#go through each bullet
        for t in targ:
            brect=Rect(b[0],b[1],10,10)
            if brect.colliderect(t):
                targ.remove(t)
                bull.remove(b)
                break
    
v=[5,0] #5 is the horizontal speed, 0 is vertical speed    

guy=[50,300]
targets=[]
##bullets=[[170,45,5,1],[400,528,1,-4]]
bullets=[]
#creating enemies at random locations
for i in range(5):
    targets.append(Rect(randint(400,750),randint(100,500),40,40))

#print(targets)

running=True
myClock=time.Clock()
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
                       
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    keys=key.get_pressed()


    guy[1]=my

    if rapid<20:
        rapid+=1
    print(bullets)
    
    drawScene(screen,guy,bullets,targets)
    moveBullets(bullets)
    checkHits(bullets,targets)

    if keys[32] and rapid==20:
        bullets.append([70,guy[1],v[0],v[1]])
        rapid=0

    myClock.tick(60)       
quit()
