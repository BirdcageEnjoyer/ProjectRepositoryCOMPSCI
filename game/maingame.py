#all modules
import pygame
import level1
import level2
import level3
import colours
import classes

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





setOfMovements = {pygame.K_w: "movingUp", pygame.K_s: "movingDown", pygame.K_a: "movingLeft", pygame.K_d: "movingRight"}
    # use later for movements instead of if statements


levelBeginningX = 50 #set to the beginning value for each level later, add a beginning value for each level
levelBeginningY = 250

allSpritesList = pygame.sprite.Group()

player = classes.Character(700 , 500, levelBeginningX, levelBeginningY, 1) #50, 50
allSpritesList.add(player)


level1PlatformList = level1.level1platforms

isInMenuState = False








#initialise pygame
pygame.init()
#screen dimensions and setup

size = (1400, 1000)
screen = pygame.display.set_mode(size)

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
        level2.drawLevel(screen, GREEN, RED, YELLOW, BLACK) # parameters for these 2 levels for now are just placeholders. EDIT, OUTDATED
        #levelBeginningX = level2.startPositionX
        #levelBeginningY = level2.startPositionY
    if player.level == 3:
        level3.drawLevel(screen, GREEN, RED)
        #levelBeginningX = level3.startPositionX
        #levelBeginningY = level3.startPositionY
    
    
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()























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
        #levelBeginningX = level3.startPositionX
        #levelBeginningY = level3.startPositionY
    
    
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()


