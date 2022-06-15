from pygame import *
import pygame
import random
import time
#COLOURS
RED=(255,0,0)
GREY=(127,127,127)
BLACK=(0,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
YELLOW=(255,255,0)
WHITE=(255,255,255)
#INITIALIZATION
width,height = 1280,720
screen = display.set_mode((width,height)) #Defining display surface
display.set_caption('Invaders Based Game') #Window Title
display.set_icon(image.load('assets/graphics/icon2.ico')) #Window Icon
font.init()
screen = pygame.display.set_mode((1280, 720))
running = True
x,y = 0,0
OUTLINE = (150,50,30)
gameLogo=image.load("pics/gameLogo1.png")
bgPic=image.load("pics/bg1.jpg")
settings=image.load("pics/settings.png")
volumePic=image.load("pics/vol.png")
#RECT LOADING
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
#FONT LOADING
font=pygame.font.SysFont("tahoma",40)
font1=pygame.font.SysFont("tahoma",20)
#GAME IMAGE LOADING
#Player Ship
playerVehicle = image.load('assets/graphics/PNG/Spaceships/05/Spaceship_05_BLUE.png')
#Enemy Ship
EnemyShip1 = pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
EnemyShip2 = pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
EnemyShip3 = pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
EnemyShip4 = pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
#Lasers
redLaser = image.load('assets/graphics/PNG/redLaser.png')
blueLaser = image.load('assets/graphics/PNG/blueLaser.png')
#Background
bg = image.load('assets/graphics/PNG/Space Background.png').convert_alpha()
#sprite rect assign
playerRect = Rect(30, 30, 358,276)
def sound():
        pass
def settings():
        pass
def mainGame():
        run = True
        screen.blit(bg,(0,0))
        while run:
                print("aaa")
                for evt in event.get():
                    if evt.type==QUIT:
                        run=False
                draw.rect(screen,RED,playerRect)
                display.flip()
def start():
    run = True
    while run:
        print("bbb")
        for evt in event.get():
            if evt.type==QUIT:
                run=False
                        
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
      
        screen.blit(bgPic,(0,0))
        draw.rect(screen,BLACK,buttonRect1,0,10)
        draw.rect(screen,BLACK,buttonRect2,0,10)
        draw.rect(screen,BLACK,buttonRect3,0,10)
        draw.rect(screen,BLACK,buttonRect4,0,10)
        draw.rect(screen,WHITE,startRect,10,10)
        draw.rect(screen,WHITE,charRect,10,10)
        draw.rect(screen,WHITE,rulesRect,10,10)
        draw.rect(screen,WHITE,storyRect,10,10)
        draw.rect(screen,WHITE,settingsRect,0,10)
        draw.rect(screen,WHITE,musicRect,0,10)
        draw.rect(screen,BLACK,borderRect,10,0)
        #screen.blit(settings,(1200,25))
        screen.blit(volumePic,(1130,25))
        screen.blit(gameLogo,(35,-350))
        screen.blit(font.render("Start Game",True,WHITE),(545,375))
        screen.blit(font.render("Select Spaceship",True,WHITE),(495,450))
        screen.blit(font.render("Instructions",True,WHITE),(545,530))
        screen.blit(font.render("Story",True,WHITE),(595,610))
        screen.blit(font1.render("©HyperUlt Games and Mahir",True,WHITE),(1000,685))

        if mb[0]:
            if startRect.collidepoint(mx,my):
                return "lev1"
            if charRect.collidepoint(mx,my):
                button="Character Select"
            if rulesRect.collidepoint(mx,my):
                button="Instructions"
            if storyRect.collidepoint(mx,my):
                button="Story"
            if settingsRect.collidepoint(mx,my):
                button="Settings"
            if musicRect.collidepoint(mx,my):
                button="Music"
        display.flip()
    return "exit"
page = "menu"
while page != "exit":
    if page == "menu":
        page = start()
    if page == "lev1":
        page = mainGame()
  
quit()
