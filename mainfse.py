from select import select
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
from pygame import mixer
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
# ,pygame.FULLSCREEN)  # Defining display surface
screen = display.set_mode((width, height))
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
levelRect1 = Rect(210, 165, 550, 180)
levelRect2 = Rect(550, 445, 550, 180)
levelRect11 = Rect(210, 165, 550, 180)
levelRect22 = Rect(550, 445, 550, 180)
# FONT LOADING
font = pygame.font.SysFont("tahoma", 40)
font1 = pygame.font.SysFont("tahoma", 20)
font3 = pygame.font.SysFont("tahoma", 150)
#BGM
mixer.music.load('pics/bgm.wav')
mixer.music.play(-1)
# GAME IMAGE LOADING
# Player Ship
blueShip = image.load(
    'assets/graphics/PNG/Spaceships/05/Spaceship_05_BLUE.png')
global playerVehicle
playerVehicle = image.load(
    'assets/graphics/PNG/Spaceships/05/Spaceship_05_BLUE.png')
greenShip = image.load(
    'assets/graphics/PNG/Spaceships/05/Spaceship_05_GREEN.png')
# Enemy Ship
EnemyShip1 = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
numEnemies = int(6)
for i in range(numEnemies):
    EnemyShip1.append(image.load(
        'assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png'))
    enemyX.append(random.randint(5, 1100))
    enemyY.append(random.randint(50, 150))
    enemyXchange.append(1)
    enemyYchange.append(150)
# Lasers
redLaser = image.load('assets/graphics/PNG/redLaser.png')
blueLaser = image.load('assets/graphics/PNG/blueLaser.png')
bullx = 0
bully = 595
bullxChange = 0
bullyChange = 0.7
bullState = 'ready'
# Background
level1bg = image.load(
    'assets/graphics/PNG/Space Background.png').convert_alpha()
lev2bg = image.load('assets/graphics/PNG/bg2.jpg').convert_alpha()
storybg = image.load('pics/storyPic.jpg').convert_alpha()
levelbg = image.load("pics/bg2.jpg").convert_alpha()
# Extra Variables (local):
score = 0


def sound():
    pass


# def settings():
#    pass
def levels():
    run = True
    screen.blit(levelbg, (0, 0))
    while run:
        for evt in event.get():
            if evt.type == QUIT:
                sys.exit()

        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()

        draw.rect(screen, BLACK, levelRect1, 0, 10)
        draw.rect(screen, BLACK, levelRect2, 0, 10)
        draw.rect(screen, WHITE, levelRect11, 10, 10)
        draw.rect(screen, WHITE, levelRect22, 10, 10)

        screen.blit(font3.render("Level 1", True, WHITE), (250, 170))
        screen.blit(font3.render("Level 2", True, WHITE), (590, 445))

        if mb[0]:
            if levelRect1.collidepoint(mx, my):
                return 'lev1'
            if levelRect2.collidepoint(mx, my):
                return 'lev2'
        display.flip()


def instructions():
    run = True
    instructions = image.load('pics/instructions.jpg').convert_alpha()
    screen.blit(instructions, (0, 0))
    while run:
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        for evt in event.get():
            if evt.type == QUIT:
                res = mb.askquestion(
                    "Game Warning", "Are you sure you want to quit?")
                if res == 'yes':
                    sys.exit()
                else:
                    pass
            keys = key.get_pressed()  # check what keys are pressed'
            screen.blit(font1.render("Click here to return to menu",
                        False, WHITE), (1000, 685))
        if mb[0]:
            if Rect(1000,685,280,35).collidepoint(mx,my):
                return 'menu'
        display.flip()


def story():
    run = True
    screen.blit(storybg, (0, 0))
    while run:
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        for evt in event.get():
            if evt.type == QUIT:
                res = mb.askquestion(
                    "Game Warning", "Are you sure you want to quit?")
                if res == 'yes':
                    sys.exit()
                else:
                    pass
            keys = key.get_pressed()  # check what keys are pressed
        screen.blit(font1.render("Press here to return to menu",
                    False, WHITE), (1000, 685))
        if mb[0]:
            if Rect(1000,685,280,35).collidepoint(mx,my):
                return 'menu'
        display.flip()


px = 600
py = 600

def settings():
    
def enemy(x, y, i):
    screen.blit(EnemyShip1[i], (x-50, y-20))


def fireBullet(x, y):
    global bullState
    global px
    global py
    bullState = 'fire'
    screen.blit(blueLaser, (bullx+20, y))


def collided(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) +
                         (math.pow(enemyY-bulletY, 2)))
    if distance < 100:
        return True
    else:
        return False


def selectShip():
    width, height = 1280, 720
    screen = display.set_mode((width, height))
    RED = (255, 0, 0)
    GREY = (127, 127, 127)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    global playerVehicle
    levelRect1 = Rect(20, 200, 620, 500)
    levelRect2 = Rect(650, 200, 620, 500)
    levelRect11 = Rect(20, 200, 620, 500)
    levelRect22 = Rect(650, 200, 620, 500)
    returnRect = Rect(1000, 50, 200, 100)
    font3 = pygame.font.SysFont("Aharoni", 150)
    font4 = pygame.font.SysFont("Aharoni", 36)
    running = True
    button = ""
    while running:
        for evt in event.get():
            if evt.type == QUIT:
                return 'menu'
        keys = key.get_pressed()             
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        draw.rect(screen, RED, levelRect1, 0, 10)
        draw.rect(screen, RED, levelRect2, 0, 10)
        draw.rect(screen, WHITE, levelRect11, 10, 10)
        draw.rect(screen, WHITE, levelRect22, 10, 10)
        draw.rect(screen, WHITE, returnRect, 10, 10)
        screen.blit(font3.render("Select Your Ship", True, WHITE), (50, 50))
        screen.blit(font4.render("Go Back", True, WHITE), (1024, 85))
        if mb[0]:
            if levelRect1.collidepoint(mx, my):
                draw.rect(screen, GREEN, levelRect11, 10, 10)
                playerVehicle = blueShip
            if levelRect2.collidepoint(mx, my):
                draw.rect(screen, GREEN, levelRect22, 10, 10)
                playerVehicle = greenShip
            if returnRect.collidepoint(mx, my):
                return 'menu'
        screen.blit(blueShip,(230,380))
        screen.blit(greenShip,(860,380))
        display.flip()


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
    global bullyChange
    global enemyXchange
    global enemyX
    global enemyY
    global enemyYchange
    global score
    global playerVehicle
    bullyChange = 2
    psize = 40
    xMove = 0
    yMove = 0
    run = True
    speed = 2
    player = Rect(px, py, psize, psize)
    image_rect = playerVehicle.get_rect(center=player.center)
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
            if bullState == 'ready':
                bullx = px
                fireBullet(bullx, bully)
        player = Rect(px, py, psize, psize)
        image_rect = playerVehicle.get_rect(center=player.center)
        screen.blit(playerVehicle, image_rect)
        # bullets
        if bully <= 0:
            bully = 595
            bullState = 'ready'
        if bullState == 'fire':
            fireBullet(bullx, bully)
            bully -= bullyChange
        # enemy movement
        for i in range(numEnemies):
            enemyX[i] += enemyXchange[i]
            if enemyX[i] <= 0:
                enemyXchange[i] = 1
                enemyY[i] += enemyYchange[i]
            elif enemyX[i] >= 1100:
                enemyXchange[i] = -1
                enemyY[i] += enemyYchange[i]
            # collision
            collision = collided(enemyX[i], enemyY[i], bullx, bully)
            if collision:
                bully = 595
                bullState = 'ready'
                score += 1
                enemyX[i] = random.randint(5, 1100)
                enemyY[i] = random.randint(50, 100)
            enemy(enemyX[i], enemyY[i],i)
        px = px + xMove
        py = py + yMove
        screen.blit(font1.render("Score:"+str(score), False, WHITE), (20, 650))
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
    global bullyChange
    global enemyXchange
    global enemyX
    global enemyY
    global enemyYchange
    global score
    global playerVehicle
    global numEnemies
    bullyChange = 0.7
    psize = 40
    xMove = 0
    yMove = 0
    run = True
    speed = 0.5
    player = Rect(px, py, psize, psize)
    image_rect = playerVehicle.get_rect(center=player.center)
    if cooldown < 20:
        cooldown += 1
    while run:
        screen.blit(levelbg, (0, 0))
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
        player = Rect(px, py, psize, psize)
        image_rect = playerVehicle.get_rect(center=player.center)
        screen.blit(playerVehicle, image_rect)
        # bullets
        if bully <= 0:
            bully = 595
            bullState = 'ready'
        if bullState == 'fire':
            fireBullet(bullx, bully)
            bully -= bullyChange
        # enemy movement
        for i in range(numEnemies):
            enemyX[i] += enemyXchange[i]
            if enemyX[i] <= 0:
                enemyXchange[i] = 0.3
                enemyY[i] += enemyYchange[i]
            elif enemyX[i] >= 1100:
                enemyXchange[i] = -0.3
                enemyY[i] += enemyYchange[i]
            # collision
            collision = collided(enemyX[i], enemyY[i], bullx, bully)
            if collision:
                bully = 595
                bullState = 'ready'
                score += 1
                enemyX[i] = random.randint(5, 1100)
                enemyY[i] = random.randint(50, 100)
            enemy(enemyX[i], enemyY[i],i)
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
        draw.rect(screen, WHITE, musicRect, 0, 10)
        draw.rect(screen, BLACK, borderRect, 10, 0)
        screen.blit(gameLogo, (35, -350))
        screen.blit(settings,(1200,25))
        screen.blit(font.render("Start Game", True, WHITE), (545, 375))
        screen.blit(font.render("Select Spaceship", True, WHITE), (495, 450))
        screen.blit(font.render("Instructions", True, WHITE), (545, 530))
        screen.blit(font.render("Story", True, WHITE), (595, 610))
        screen.blit(font1.render(
            "©HyperUlt Games and Mahir", True, WHITE), (1000, 675))
        screen.blit(font1.render("Press escape to quit", True, WHITE), (20,675))
        keys = key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        if mb[0]:
            if startRect.collidepoint(mx, my):
                return "levels"
            if charRect.collidepoint(mx, my):
                return 'charselect'
            if rulesRect.collidepoint(mx, my):
                return 'instructions'
            if storyRect.collidepoint(mx, my):
                return 'story'
            if musicRect.collidepoint(mx, my):
                return 'settings'
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
        page = instructions()
    if page == 'charselect':
        page = selectShip()
    if page == 'settings':
        page = settings()

quit()
