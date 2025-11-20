import pygame

pygame.init()

size = (1400, 1000)
screen = pygame.display.set_mode(size)
#all modules
# import pygame
import level1
import level2
import level3
import colours
import classes
import math

#w
#W
#variables defined here
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SKY = (149, 186, 245)

isTouchingGround = True #when player first spawns in, always set to true to begin with, the player wont start falling from the air


scrollThreshold = 0

# backgroundMenuImage = pygame.image.


# bglevel1 = pygame.image.load("Backgroundtest.png").convert_alpha()
# bglevel2 = pygame.image.load("").convert()
# bglevel3 = pygame.image.load("").convert()
# bgwidth = bglevel1.get_width()
# bgrect = bglevel1.get_rect()



setOfMovements = {pygame.K_w: "movingUp", pygame.K_s: "movingDown", pygame.K_a: "movingLeft", pygame.K_d: "movingRight"}
    # use later for movements instead of if statements


levelBeginningX = 50 #set to the beginning value for each level later, add a beginning value for each level
levelBeginningY = 250

allSpritesList = pygame.sprite.Group()

player = classes.Character(700 , 500, levelBeginningX, levelBeginningY, 1) #50, 50
allSpritesList.add(player)


level1PlatformList = level1.level1platforms

isInMenuState = False


# backgroundupdate = math.ceil(1400/bgwidth) + 1
# bgscroll = 0





#initialise pygame
# pygame.init()
#screen dimensions and setup

# size = (1400, 1000)
# screen = pygame.display.set_mode(size)


bglevel1 = pygame.image.load("level1bgmountains.jpg").convert()
bgwidth = bglevel1.get_width()
bgrect = bglevel1.get_rect()

backgroundupdate = math.ceil(1400/bgwidth) + 1
bgscroll = 0 # make a new variable that checks old x position, if it is not the same as the current then the scroll works otherwise it stays in place
# if it is still equal to old x because thatm eans we

pygame.display.set_caption("you don't want to see me infuriated")

done = False

clock = pygame.time.Clock()
 
while not done:

 

    screen.fill(colours.BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN: # later on, make variables for the keys so that the player can change the keys for movement, then replace k_...
            #with the variables so that depending on which key the player sets to as move up left right down, it will move accordingly ...
            if event.key == pygame.K_SPACE:
                player.jumpControl()
            if event.key == pygame.K_a:
                player.movingLeft = True
                player.velX = -5
            if event.key == pygame.K_d:
                player.movingRight = True
                player.velX = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
               player.movingLeft = False
               player.velX = 0
            if event.key == pygame.K_d:
                player.movingRight = False
                player.velX = 0
    
   



    

    if player.level == 1:
        player.update(level1PlatformList)
        # level1.movingPlatform1.move() #possible configuration
    # if player.level == 2:
    #     player.update()
    # if player.level == 3:
    #     player.update()


    cameraXoffset = (player.rect.centerx - 700)
    cameraYoffset = (player.rect.centery - 500)


       

    



    screen.fill(SKY)
    #drawing code below

    # for i in range(backgroundupdate):
    #     if player.level == 1:
    #         screen.blit(bglevel1, (i * bgwidth + bgscroll, 0))
      

    if player.movingRight:
        bgscroll += 5
    elif player.movingLeft:
        bgscroll -= 5  
        # use this for implemntation, issue was bg picture constantly moving to left, but i wanted it to only move relative to player movement
        # therefore added conditionals
    # if abs(bgscroll) > bgwidth:
    #     bgscroll = 0
    bgscroll = bgscroll % bgwidth
    # if bgscroll <= -bgwidth:
    #     bgscroll += bgwidth
    # elif bgscroll >= bgwidth:
    #     bgscroll -= bgwidth
    for i in range(backgroundupdate):
        if player.level == 1:
            # screen.blit(bglevel1, (i * bgwidth + bgscroll, 0))
            screen.blit(bglevel1, (-(bgscroll) + bgwidth, 0))
            screen.blit(bglevel1, (-(bgscroll), 0))
            
# second issue is ^ that if moving to left from spawn, picture would stop refreshing
    #reason is because this line since i did absolute value is above bgwidth, and using > i will be only accounting for it when player moves to right
    # i needed to make the wrap logic for going left as well.


    # level1PlatformList.draw(screen)
    screen.blit(player.playerImage, (player.rect.x - cameraXoffset, player.rect.y - cameraYoffset))
   
    
    if player.level == 1:
        
        level1.drawLevel(screen, cameraXoffset, cameraYoffset)
        # levelBeginningX = level1.startPositionX
        # levelBeginningY = level1.startPositionY
    if player.level == 2:
        level2.drawLevel(screen, GREEN, RED, YELLOW, BLACK) # parameters for these 2 levels for now are just placeholders. EDIT, OUTDATED
        #levelBeginningX = level2.startPositionX
        #levelBeginningY = level2.startPositionY
    if player.level == 3:
        level3.drawLevel(screen, GREEN, RED)
        #levelBeginningX = level3.startPositionX
        #levelBeginningY = level3.startPositionY

    

    # for i in range(backgroundupdate):
    #     if player.level == 1:
    #         screen.blit(bglevel1, (i * bgwidth + bgscroll, 0))
    #         bgrect.x = i * bgwidth + bgscroll
  
    
    # bgscroll -= 5
    # if abs(bgscroll) > bgwidth:
    #     bgscroll = 0
    
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()




















#game states    


def menu():
    while not done:
        screen.fill(colours.BLACK)
        screen.blit() # blit settings gui




def settings():
    while not done:
        screen.fill(colours.BLACK)
        screen.blit()#blit setting gui





def playGame():


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jumpControl()
            if event.key == pygame.K_a:
                player.movingLeft = True
                player.velX = -5
            if event.key == pygame.K_d:
                player.movingRight = True
                player.velX = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
               player.movingLeft = False
               player.velX = 0
            if event.key == pygame.K_d:
                player.movingRight = False
                player.velX = 0
    
   



    

    if player.level == 1:
        player.update(level1PlatformList)
    # if player.level == 2:
    #     player.update()
    # if player.level == 3:
    #     player.update()


    cameraXoffset = (player.rect.centerx - 700)
    cameraYoffset = (player.rect.centery - 500)


       

    



    screen.fill(SKY)
    #drawing code below




    # level1PlatformList.draw(screen)
    screen.blit(player.playerImage, (player.rect.x - cameraXoffset, player.rect.y - cameraYoffset))
   
    
    if player.level == 1:
        
        level1.drawLevel(screen, cameraXoffset, cameraYoffset)
        # levelBeginningX = level1.startPositionX
        # levelBeginningY = level1.startPositionY
    if player.level == 2:
        level2.drawLevel(screen, GREEN, RED, YELLOW, BLACK)
        #levelBeginningX = level2.startPositionX
        #levelBeginningY = level2.startPositionY
    if player.level == 3:
        level3.drawLevel(screen, GREEN, RED)
        #levelBeginningX = level3.st artPositionX
        #levelBeginningY = level3.startPositionY
    
    
    pygame.display.flip()
 
    clock.tick(15)
 
pygame.quit()


