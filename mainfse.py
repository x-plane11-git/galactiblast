from pygame import *
import pygame
import sys
import tkinter
import random
import time
import tkinter
import math
from tkinter import messagebox as mb
from tkinter import*
Tk().wm_withdraw()  # to hide the main window
mixer.init()  # initialize music player
root = Tk()
root.withdraw()
# COLOURS
RED = (255, 0, 0)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
# INITIALIZATION
width, height = 1280, 720
screen = display.set_mode((width, height))#,pygame.FULLSCREEN)  # Defining display surface
display.set_caption('Invaders Based Game')  # Window Title
display.set_icon(image.load('assets/graphics/icon2.ico'))  # Window Icon
font.init()
running = True
x, y = 0, 0
OUTLINE = (150, 50, 30)
gameLogo = image.load("pics/gameLogo1.png")
bgPic = image.load("pics/bg1.jpg")
settings = image.load("pics/settings.png")
volumePic = image.load("pics/vol.png")
# RECT LOADING
startRect = Rect(480, 365, 320, 70)
charRect = Rect(480, 445, 320, 70)
rulesRect = Rect(480, 525, 320, 70)
storyRect = Rect(480, 605, 320, 70)
settingsRect = Rect(1130, 25, 60, 60)
musicRect = Rect(1200, 25, 60, 60)
buttonRect1 = Rect(480, 365, 320, 70)
buttonRect2 = Rect(480, 445, 320, 70)
buttonRect3 = Rect(480, 525, 320, 70)
buttonRect4 = Rect(480, 605, 320, 70)
borderRect = Rect(0, 0, 1280, 720)
levelRect1=Rect(210,165,550,180)
levelRect2=Rect(550,445,550,180)
levelRect11=Rect(210,165,550,180)
levelRect22=Rect(550,445,550,180)
# FONT LOADING
font = pygame.font.SysFont("tahoma", 40)
font1 = pygame.font.SysFont("tahoma", 20)
font3=pygame.font.SysFont("tahoma",150)
# GAME IMAGE LOADING
# Player Ship
playerVehicle = image.load(
    'assets/graphics/PNG/Spaceships/05/Spaceship_05_BLUE.png')
# Enemy Ship
EnemyShip1 = image.load(
    'assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
enemyX = random.randint(5, 1100)
enemyY = random.randint(50, 150)
enemyXchange = 0.3
enemyYchange = 150
EnemyShip2 = image.load(
    'assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
EnemyShip3 = image.load(
    'assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
EnemyShip4 = image.load(
    'assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
# Lasers
redLaser = image.load('assets/graphics/PNG/redLaser.png')
blueLaser = image.load('assets/graphics/PNG/blueLaser.png')
bullx = 0
bully = 595
bullxChange = 0
bullyChange = 0.7
bullState = 'ready'
# Background
level1bg = image.load('assets/graphics/PNG/Space Background.png').convert_alpha()
lev2bg = image.load('assets/graphics/PNG/bg2.jpg').convert_alpha()
storybg = image.load('pics/storyPic.jpg').convert_alpha()
levelbg = image.load("pics/bg2.jpg").convert_alpha()
#Extra Variables (local):
score = 0
def sound():
    pass


def settings():
    pass
def levels():
    run = True
    screen.blit(levelbg,(0,0))
    while run:
        for evt in event.get():
            if evt.type==QUIT:
                sys.exit()
                        
        mx,my=mouse.get_pos()
        mb=mouse.get_pressed()
        
        draw.rect(screen,BLACK,levelRect1,0,10)
        draw.rect(screen,BLACK,levelRect2,0,10)
        draw.rect(screen,WHITE,levelRect11,10,10)
        draw.rect(screen,WHITE,levelRect22,10,10)

        screen.blit(font3.render("Level 1",True,WHITE),(250,170))
        screen.blit(font3.render("Level 2",True,WHITE),(590,445))


        if mb[0]:
            if levelRect1.collidepoint(mx,my):
                return 'lev1'
            if levelRect2.collidepoint(mx,my):
                return 'lev2'
        display.flip()
def instructions():
    run = True
    instructions = image.load('pics/instructions.jpg').convert_alpha()
    screen.blit(instructions, (0, 0))
    while run:
        for evt in event.get():
            if evt.type == QUIT:
                res = mb.askquestion(
                    "Game Warning", "Are you sure you want to quit?")
                if res == 'yes':
                    sys.exit()
                else:
                    pass
            keys = key.get_pressed()  # check what keys are pressed
            if keys[K_ESCAPE] or keys[K_BACKSPACE]:  # return to menu
                return 'menu'
        screen.blit(font1.render("Press esc to return to menu",
                    False, WHITE), (1000, 685))

        display.flip()


def story():
    run = True
    screen.blit(storybg, (0, 0))
    while run:
        for evt in event.get():
            if evt.type == QUIT:
                res = mb.askquestion(
                    "Game Warning", "Are you sure you want to quit?")
                if res == 'yes':
                    sys.exit()
                else:
                    pass
            keys = key.get_pressed()  # check what keys are pressed
            if keys[K_ESCAPE] or keys[K_BACKSPACE]:  # return to menu
                return 'menu'
        screen.blit(font1.render("Press esc to return to menu",
                    False, WHITE), (1000, 685))

        display.flip()


px = 600
py = 600


def enemy(x, y):
    screen.blit(EnemyShip1, (x-50, y-20))


def fireBullet(x, y):
    global bullState
    global px
    global py
    bullState = 'fire'
    screen.blit(blueLaser, (bullx+20, y))


def collided(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 100:
        return True
    else:
        return False


def lev1():
    # sprite rect assign
    fpsClock = pygame.time.Clock()
    targets = []
    bullets = []
    cooldown = 20
    global px
    global py
    global bullx
    global bully
    global bullState
    global enemyXchange
    global enemyX
    global enemyY
    global enemyYchange
    global score
    psize = 40
    xMove = 0
    yMove = 0
    run = True
    speed = 0.5
    if cooldown < 20:
        cooldown += 1
    while run:
        screen.blit(level1bg, (0, 0))
        keys = key.get_pressed()
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        for evt in event.get():
            if evt.type == QUIT:
                return 'menu'
        keys = key.get_pressed()  # check what keys are pressed
        if keys[K_LEFT]:  # and px - speed > 0: #moving player left
            px -= speed
        if keys[K_RIGHT]:  # and px + speed: #moving player right
            px += speed
        if keys[K_SPACE]:
            bullx = px
            fireBullet(bullx, bully)
        player = draw.rect(screen, RED, [px, py, psize, psize])
        enemy(enemyX, enemyY)
        # bullets
        if bully <= 0:
            bully = 595
            bullState = 'ready'
        if bullState == 'fire':
            fireBullet(bullx, bully)
            bully -= bullyChange
        # enemy movement
        enemyX += enemyXchange
        if enemyX <= 0:
            enemyXchange = 0.3
            enemyY += enemyYchange
        elif enemyX >= 1100:
            enemyXchange = -0.3
            enemyY += enemyYchange
        #collision
        collision = collided(enemyX,enemyY,bullx,bully)
        if collision:
            bully = 595
            bullState = 'ready'
            score += 1
            enemyX = random.randint(5, 1100)
            enemyY = random.randint(50, 100)
        px = px + xMove
        py = py + yMove
        screen.blit(font1.render("Score:"+str(score), False, WHITE), (1000, 685))
        display.flip()
    fpsClock.tick(60)

def lev2():
    # sprite rect assign
    fpsClock = pygame.time.Clock()
    targets = []
    bullets = []
    cooldown = 20
    global px
    global py
    global bullx
    global bully
    global bullState
    global enemyXchange
    global enemyX
    global enemyY
    global enemyYchange
    global score
    enemyXchange = 0.5
    psize = 40
    xMove = 0
    yMove = 0
    run = True
    speed = 0.5
    if cooldown < 20:
        cooldown += 1
    while run:
        screen.blit(lev2bg, (0, 0))
        keys = key.get_pressed()
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        for evt in event.get():
            if evt.type == QUIT:
                return 'menu'
        keys = key.get_pressed()  # check what keys are pressed
        if keys[K_LEFT]:  # and px - speed > 0: #moving player left
            px -= speed
        if keys[K_RIGHT]:  # and px + speed: #moving player right
            px += speed
        if keys[K_SPACE]:
            bullx = px
            fireBullet(bullx, bully)
        player = draw.rect(screen, RED, [px, py, psize, psize])
        enemy(enemyX, enemyY)
        # bullets
        if bully <= 0:
            bully = 595
            bullState = 'ready'
        if bullState == 'fire':
            fireBullet(bullx, bully)
            bully -= bullyChange
        # enemy movement
        enemyX += enemyXchange
        if enemyX <= 0:
            enemyXchange = 0.5
            enemyY += enemyYchange
        elif enemyX >= 1100:
            enemyXchange = -0.5
            enemyY += enemyYchange
        #collision
        collision = collided(enemyX,enemyY,bullx,bully)
        if collision:
            bully = 595
            bullState = 'ready'
            score += 1
            enemyX = random.randint(5, 1100)
            enemyY = random.randint(50, 100)
        px = px + xMove
        py = py + yMove
        screen.blit(font1.render("Score:"+str(score), False, WHITE), (1000, 685))
        display.flip()
    fpsClock.tick(60)

def start():
    run = True
    while run:
        for evt in event.get():
            if evt.type == QUIT:
                run = False

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        screen.blit(bgPic, (0, 0))
        draw.rect(screen, BLACK, buttonRect1, 0, 10)
        draw.rect(screen, BLACK, buttonRect2, 0, 10)
        draw.rect(screen, BLACK, buttonRect3, 0, 10)
        draw.rect(screen, BLACK, buttonRect4, 0, 10)
        draw.rect(screen, WHITE, startRect, 10, 10)
        draw.rect(screen, WHITE, charRect, 10, 10)
        draw.rect(screen, WHITE, rulesRect, 10, 10)
        draw.rect(screen, WHITE, storyRect, 10, 10)
        draw.rect(screen, WHITE, settingsRect, 0, 10)
        draw.rect(screen, WHITE, musicRect, 0, 10)
        draw.rect(screen, BLACK, borderRect, 10, 0)
        # screen.blit(settings,(1200,25))
        screen.blit(volumePic, (1130, 25))
        screen.blit(gameLogo, (35, -350))
        screen.blit(font.render("Start Game", True, WHITE), (545, 375))
        screen.blit(font.render("Select Spaceship", True, WHITE), (495, 450))
        screen.blit(font.render("Instructions", True, WHITE), (545, 530))
        screen.blit(font.render("Story", True, WHITE), (595, 610))
        screen.blit(font1.render(
            "©HyperUlt Games and Mahir", True, WHITE), (1000, 685))

        if mb[0]:
            if startRect.collidepoint(mx, my):
                return "levels"
            if charRect.collidepoint(mx, my):
                button = "Character Select"
            if rulesRect.collidepoint(mx, my):
                return 'instructions'
            if storyRect.collidepoint(mx, my):
                return 'story'
            if settingsRect.collidepoint(mx, my):
                button = "Settings"
            if musicRect.collidepoint(mx, my):
                button = "Music"
        display.flip()
    return "exit"


page = "menu"
while page != "exit":
    if page == "menu":
        page = start()
    if page == "levels":
        page = levels()
    if page == 'lev1':
        page = lev1()
    if page == 'lev2':
        page = lev2()
    if page == 'story':
        page = story()
    if page == 'instructions':
        instructions()

quit()
