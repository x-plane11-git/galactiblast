#StartUp.py

from pygame import *
import pygame
font.init()

##def instructions():
##    running = True
##    inst=image.load("pics/instructions.png")
##    screen.blit(inst,(0,0))
##    while running:
##        print("instructions")
##        for evnt in event.get():          
##            if evnt.type==QUIT:
##                running=False
##        if key.get_pressed()[27]:
##            running=False
##        display.flip()
##
##def menu(): 
##    running = True
##    myClock = time.Clock()
##    while running:
##        print("main menu")
##        for evnt in event.get():            
##            if evnt.type == QUIT:
##                return "exit"
##        
##        mx,my=mouse.get_pos()
##        mb=mouse.get_pressed()
##        for b in buttons:
##            draw.rect(screen,WHITE,startRect,10,10)
##            draw.rect(screen,WHITE,charRect,10,10)
##            draw.rect(screen,WHITE,rulesRect,10,10)
##            draw.rect(screen,WHITE,storyRect,10,10)
##            draw.rect(screen,WHITE,settingsRect,0,10)
##            draw.rect(screen,WHITE,musicRect,0,10)
##
##        if mb[0]==1:
####            if buttons[0].collidepoint(mx,my):
####                return "lev1"
####            if buttons[1].collidepoint(mx,my):
####                return "lev2"
##            if rulesRect.collidepoint(mx,my):
##                return "instructions"
####            if buttons[3].collidepoint(mx,my):
####                return "story"
        
width,height=1280,720
screen=display.set_mode((width,height))
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)

gameLogo=image.load("pics/gameLogo1.png")
bgPic=image.load("pics/bg1.jpg")
settings=image.load("pics/settings.png")
volumePic=image.load("pics/vol.png")

startRect=Rect(480,365,320,70)
charRect=Rect(480,445,320,70)
rulesRect=Rect(480,525,320,70)
storyRect=Rect(480,605,320,70)
settingsRect=Rect(1130,25,60,60)
musicRect=Rect(1200,25,60,60)
buttonRect1=Rect(480,365,320,70)
buttonRect2=Rect(480,445,320,70)
buttonRect3=Rect(480,525,320,70)
buttonRect4=Rect(480,605,320,70)
borderRect=Rect(0,0,1280,720)

font=pygame.font.SysFont("Aharoni",40)
font1=pygame.font.SysFont("Aharoni",20)


running=True
##page = "menu"
##while page != "exit":
##    if page == "menu":
##        page = menu()
####    if page == "lev1":
####        page = level1()
####    if page == "lev2":
####        page = level2() 
##    if page == "instructions":
##        page = instructions()    
####    if page == "story":
####        page = story() 
button=""
##myClock=time.Clock()
##    myClock.tick(60)
            
quit()
