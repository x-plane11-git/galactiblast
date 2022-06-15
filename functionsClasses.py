from email.mime import image
import pygame
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
width,height = 1280,720
#RELOADING REQUIRED ASSETS
#Player Vehicle
playerVehicle = pygame.transform.scale(pygame.image.load('assets/graphics/PNG/Spaceships/05/Spaceship_05_BLUE.png'),(179,128))
#Enemy Vehicle
EnemyShip1 = pygame.transform.scale(pygame.image.load('assets/graphics/PNG/Spaceships/01/Spaceship_01_RED.png'),(179,128))
#Lasers
redLaser = pygame.image.load('assets/graphics/PNG/redLaser.png')
blueLaser = pygame.image.load('assets/graphics/PNG/blueLaser.png')
#Class concept: https://www.w3schools.com/python/python_classes.asp#
#LISTED BELOW ARE RESOURCES USED TO CREATE THE CLASSES:
#https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object
#https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods
#https://kidscancode.org/blog/2016/08/pygame_1-2_working-with-sprites/#
class Vehicle: #Vehicle class which will be used by both enemy and player
    coolDown = 30
    def __init__(self, x, y, hp = 100):
        self.x = x #x pos
        self.y = y #y pos
        self.hp = hp #health
        self.shipImage = None #image to blit
        self.lasers = [] #list for lasers (ammo)
        self.cooldown = 0 #cooldown after shot
        self.laserImage = None #laser image
        
        
    def blitSprite(self,displayScreen):
        displayScreen.blit(self.shipImage, (self.x, self.y))
        for laser in self.lasers:
            laser.spawnLaser(displayScreen)
    def moveLasers(self, laserSpeed, object):
        self.cooldown()
        for laser in self.lasers:
            laser.move(laserSpeed)
            if laser.screenDetect(height):
                self.lasers.remove(laser)
            elif laser.collision(object):
                object.hp -=10
                self.lasers.remove(laser)
    def cooldown(self):
        if self.cooldown >= self.coolDown:
            self.cooldown = 0
        elif self.cooldown > 0:
            self.cooldown += 1
    def shoot(self):
        if self.cooldown == 0:
            laser = Bullets(self.x, self.y, self.laserImage)
            self.lasers.append(laser)
            self.cooldown = 1
    def getw(self):
        return self.shipImage.get_width()
    def geth(self):
        return self.shipImage.get_height()
class Player(Vehicle): #Player class for player
    def __init__(self, x, y, hp = 100):
        super().__init__(x, y, hp) #applying variables from Vehicle class
        self.shipImage = playerVehicle #assigning ship image
        self.laserImage = blueLaser #assinging laser image
        self.mask = pygame.mask.from_surface(self.shipImage) #create a mask for the surface (player), documentation here: https://www.pygame.org/docs/ref/mask.html
        self.maxhp = hp
    def moveLasers(self, laserSpeed, objects):
        self.cooldown()
        for laser in self.lasers:
            laser.move(laserSpeed)
            if laser.screenDetect(height):
                self.lasers.remove(laser)
            else: 
                for object in objects:
                    if laser.collision(object):
                        objects.remove(object)
                        self.lasers.remove(laser)
class Enemy(Vehicle): #Enemy Class
    def __init__(self, x, y, hp=100):
        super().__init__(x, y, hp) #apply variables from Vehicle Class
        self.shipImage, self.laserImage = EnemyShip1, redLaser #Assigning images to enemy sprites
        self.mask = pygame.mask.from_surface(self.shipImage) #create a mask for the surface (enemy), documentation here: https://www.pygame.org/docs/ref/mask.html

    def move(self, enemySpeed): #movement of an enemy
        self.y += enemySpeed #always in the downwards direction
class Bullets:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
    def blitBullet(self, drawingSurf):
        drawingSurf.blit(self.img, (self.x, self.y))
    def move(self, speed):
        self.y += speed
    def outOfScreen(self, height):
        return self.y <= height and self.y >= 0
    def collision(self, object):
        return collide(object, self)
def collide(firstObject, secondObject):
    xOffset = secondObject.x - firstObject.x
    yOffset = secondObject.y - firstObject.y
    # IF MASKS ARE OVERLAPPING, NOT RECTS.
    #DOCUMENTATION (highlighted): https://www.pygame.org/docs/ref/mask.html?highlight=overlap#pygame.mask.Mask.overlap
    return firstObject.mask.overlap(secondObject, (xOffset, yOffset)) != None #(x,y) so none lets nothing be returned
