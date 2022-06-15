import pygame
import random
import time 
from functionsClasses import Vehicle, Player, Enemy, Bullets #Imports the vehicle and player class from the ship file in the main.py directory
#Defining Colours
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
width,height = 1280,720
screen = pygame.display.set_mode((width,height)) #Defining display surface
pygame.display.set_caption('Invaders Based Game') #Window Title
pygame.display.set_icon(pygame.image.load('assets/graphics/icon2.ico')) #Windo w Icon
#loading all the images
'''
#Player Ship
playerVehicle = pygame.image.load('assets/graphics/PNG/Spaceships/05/Spaceship_05_BLUE.png')
#Enemy Ship
EnemyShip1 = pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
EnemyShip2 = pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
EnemyShip3 = pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
EnemyShip4 = pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
#Lasers
redLaser = pygame.image.load('assets/graphics/PNG/redLaser.png')
blueLaser = pygame.image.load('assets/graphics/PNG/blueLaser.png')
'''
#Background
bg = pygame.image.load('assets/graphics/PNG/Space Background.png').convert_alpha()
screen.blit(bg,(0,0))
#Initiate Fonts
pygame.font.init()
#Functions
def mainGame(): #Main game function to seperate game from menu etc.
    run = True
    frameRate = 60 #Ticks per second
    playerLives = 3 #Number of player lives
    playerLevel = 0 #Level (more to be added soon)
    sysFont = pygame.font.SysFont("tahoma",20) #Font type for system wide game use
    player = Player(200,200) #Test Location
    speed = 3 #Move 5 pixels L/R/U/D depending on keypress
    enemies = []
    waves = 5
    enemySpeed = 1
    laserSpeed = 2
    clock = pygame.time.Clock() #Define Clock
    lost = False
    displayTime = 0
    def drawScene(): #This function can only be run within the main game function
        screen.blit(bg,(0,0))
        #player info
        playerLives_text = sysFont.render(f'Lives Remaining: {playerLives}',1,WHITE) #lives remaning text format
        playerLevel_text = sysFont.render(f'Level: {playerLevel}',1,WHITE) #player level text
        screen.blit(playerLives_text,(20,20))
        screen.blit(playerLevel_text,(20,40))
        for enemy in enemies:
            enemy.blitSprite(screen)
        player.blitSprite(screen) #draws player ship
        if lost:
            lostText = sysFont.render("Ship Destroyed:(", 1, WHITE)
            screen.blit(lostText, (width/2 - lostText.get_width()/2, 360))
        pygame.display.update() #update display every 60 frames a second
    while run:
        clock.tick(frameRate) #ticks framerate
        drawScene() #draws all objects in drawScene function
        if playerLives <= 0 or player.hp <=0:
            lost = True
            displayTime += 1
        if lost:
            if displayTime > frameRate*5:
                run = False
        else:
            continue
        if len(enemies) == 0:
            playerLevel += 1
            waves += 5
            for i in range(waves): 
                enemy = Enemy(random.randrange(50, width-100), random.randrange(-1525, -100))
                enemies.append(enemy)
        for evt in pygame.event.get(): #quitter
            if evt.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed() #check what keys are pressed
        if keys[pygame.K_UP] and player.y - speed > 0: #moving player up
            player.y -= speed
        if keys[pygame.K_LEFT] and player.x - speed > 0: #moving player left
            player.x -= speed
        if keys[pygame.K_RIGHT] and player.x + speed +player.getw() < width: #moving player right
            player.x += speed
        if keys[pygame.K_DOWN] and player.y + speed + player.geth() < height: #moving player down
            player.y += speed
        if keys[pygame.K_SPACE]:
            player.shoot()
        for enemy in enemies[:]:
            enemy.move(enemySpeed)#move enemy downwards
            enemy.moveLasers(laserSpeed, player)
            if enemy.y + enemy.geth() > height:
                playerLives -= 1
                enemies.remove(enemy)
        player.moveLasers(laserSpeed, enemies)

mainGame() #runs main game function (soon to be replaced with startscreen