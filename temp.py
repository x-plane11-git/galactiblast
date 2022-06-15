
#from functionsClasses import Vehicle, Player, Enemy, Bullets #Imports the vehicle and player class from the ship file in the main.py directory
#Defining Colours

#loading all the images


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



'''

'''

#Initiate Fonts
pygame.font.init()
#Functions
def mainGame(): #Main game function to seperate game from menu etc.
        print("ccc")
##    run = True
##    frameRate = 60 #Ticks per second
##    playerLives = 3 #Number of player lives
##    playerLevel = 0 #Level (more to be added soon)
##    sysFont = pygame.font.SysFont("tahoma",20) #Font type for system wide game use
##    player = Player(200,200) #Test Location
##    speed = 3 #Move 5 pixels L/R/U/D depending on keypress
##    enemies = []
##    waves = 5
##    enemySpeed = 1
##    laserSpeed = 2
##    clock = pygame.time.Clock() #Define Clock
##    lost = False
##    displayTime = 0
##    
##    while run:
##        clock.tick(frameRate) #ticks framerate
##        drawScene() #draws all objects in drawScene function
##        if playerLives <= 0 or player.hp <=0:
##            lost = True
##            displayTime += 1
##        if lost:
##            if displayTime > frameRate*5:
##                run = False
##        else:
##            continue
##        if len(enemies) == 0:
##            playerLevel += 1
##            waves += 5
##            for i in range(waves): 
##                enemy = Enemy(random.randrange(50, width-100), random.randrange(-1525, -100))
##                enemies.append(enemy)
##        for evt in pygame.event.get(): #quitter
##            if evt.type == pygame.QUIT:
##                run = False
##        keys = pygame.key.get_pressed() #check what keys are pressed
##        if keys[pygame.K_UP] and player.y - speed > 0: #moving player up
##            player.y -= speed
##        if keys[pygame.K_LEFT] and player.x - speed > 0: #moving player left
##            player.x -= speed
##        if keys[pygame.K_RIGHT] and player.x + speed +player.getw() < width: #moving player right
##            player.x += speed
##        if keys[pygame.K_DOWN] and player.y + speed + player.geth() < height: #moving player down
##            player.y += speed
##        if keys[pygame.K_SPACE]:
##            player.shoot()
##        for enemy in enemies[:]:
##            enemy.move(enemySpeed)#move enemy downwards
##            enemy.moveLasers(laserSpeed, player)
##            if enemy.y + enemy.geth() > height:
##                playerLives -= 1
##                enemies.remove(enemy)
##        player.moveLasers(laserSpeed, enemies)

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




print('aaaaa')


