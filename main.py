import pygame
import random
import time 

width,height = 1280,780
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Invaders Based Game')
pygame.display.set_icon(pygame.image.load('assets/graphics/pygameicon.png'))
#loading all the images
#Player Ship
playerShip = pygame.image.load('assets/graphics/PNG/Spaceships/05/Spaceship_05_BLUE.png')
#Enemy Ship
EnemyShip1 = pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
EnemyShip2 = pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
EnemyShip3 = pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
EnemyShip4 = pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png')
#Lasers
redLaser = pygame.image.load('assets/graphics/PNG/redLaser.png')
blueLaser = pygame.image.load('assets/graphics/PNG/blueLaser.png')

#Background
bg = pygame.image.load('assets/graphics/PNG/Space Background.png').convert_alpha()
screen.blit(bg,(0,0))
#Functions
def main():
    run = True
    FPS = 60 #for pygame clock
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
#pygame.display.flip()
#quit()
