import pygame
import sys

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




def playGame():

    pygame.display.set_caption("yeahyeah")

    while not done:

        playerMousePosition = pygame.mouse.get_pos()
        screen.fill("black") #possibly not needed

        returnButton = classes.generalpurposeButton(image=None, position=(1300, 0), textinput="Return", font=pygameGetFont(25), colour="Green", 
        collisioncolour="Red")

        returnButton.colourSwapOnHover(playerMousePosition)
        returnButton.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if returnButton.detectMouseInput(playerMousePosition):
                    menu()
        
        pygame.display.update()
        



def settings():
    while not done:
        
        settingsMouseButton = pygame.mouse.get_pos()
        settingsText = pygameGetFont(50).render("skibidi", True, "Green")
        settingsRect = settingsText.get_rect(center=(700, 200))
        screen.blit(settingsText, settingsRect)

        settingsReturnButton = classes.generalpurposeButton(image=None, position=(1300,100), textinput="Return", font=pygameGetFont(25),
        colour="Black", collisioncolour="Red")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if settingsReturnButton.detectMouseInput(settingsMouseButton):
                    menu()
        
        pygame.display.update()




def menu():

    pygame.display.set_caption("i want to playtest this game")

    while not done:
        screen.blit(mainMenuBackground, (0,0))

        mousePosition = pygame.mouse.get_pos()

        menuTitleText = pygameGetFont(50).render("Main menu", True, "#964B00")
        menuRect = menuTitleText.get_rect(center=(700, 200))

        startGameButton = classes.generalpurposeButton(image=pygame.image.load("Button rectangle.png"), position=(700, 300), textinput="Begin", 
        font=pygameGetFont(50), colour="#964B00", collisioncolour="Red")

        settingsButton = classes.generalpurposeButton(image=pygame.image.load("Button rectangle.png"), position=(700, 400), textinput="Settings",
        font=pygameGetFont(50), colour="#964B00", collisioncolour="Red")

        closeButton = classes.generalpurposeButton(image=pygame.image.load("Button rectangle.png"), position=(700, 500), textinput="Close",
        font=pygameGetFont(50), colour="#964B00", collisioncolour="Red")


        screen.blit(menuTitleText, menuRect)
        for i in range(3):
            buttons = [startGameButton, settingsButton, closeButton]
            buttons[i].colourSwapOnHover(mousePosition)
            buttons[i].update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startGameButton.detectMouseInput(mousePosition):
                    playGame()
                elif settingsButton.detectMouseInput(mousePosition):
                    pass #put settings() here once it has been made
                elif closeButton.detectMouseInput(mousePosition):
                    pygame.quit()
        
        pygame.display.update()
        

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

mainMenuBackground = pygame.image.load("Screenshot 2023-04-08 190551.png").convert()
# bglevel1 = pygame.image.load("Backgroundtest.png").convert_alpha()
# bglevel2 = pygame.image.load("").convert()
# bglevel3 = pygame.image.load("").convert()
# bgwidth = bglevel1.get_width()
# bgrect = bglevel1.get_rect()

def pygameGetFont(size):
    return pygame.font.Font("CedarvilleCursive-Regular.ttf", size)


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
        if event.type == pygame.QUIT or player.lives <= 0:
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
    
    if player.rect.y > 3000:
        player.rect.x = levelBeginningX
        player.rect.y = levelBeginningY
        player.lives -= 1
        print(player.lives)



    

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


# def menu():

#     pygame.display.set_caption("i want to playtest this game")

#     while not done:
#         screen.blit(mainMenuBackground, (0,0))

#         mousePosition = pygame.mouse.get_pos()

#         menuTitleText = pygameGetFont(50).render("Main menu", True, "#964B00")
#         menuRect = menuTitleText.get_rect(center=(700, 200))

#         startGameButton = classes.generalpurposeButton(image=pygame.image.load("Button rectangle.png"), position=(700, 300), textinput="Begin", 
#         font=pygameGetFont(50), colour="#964B00", collisioncolour="Red")

#         settingsButton = classes.generalpurposeButton(image=pygame.image.load("Button rectangle.png"), position=(700, 400), textinput="Settings",
#         font=pygameGetFont(50), colour="#964B00", collisioncolour="Red")

#         closeButton = classes.generalpurposeButton(image=pygame.image.load("Button rectangle.png"), position=(700, 500), textinput="Close",
#         font=pygameGetFont(50), colour="#964B00", collisioncolour="Red")


#         screen.blit(menuTitleText, menuRect)
#         for i in range(3):
#             buttons = [startGameButton, settingsButton, closeButton]
#             buttons[i].colourSwapOnHover(mousePosition)
#             buttons[i].update(screen)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if startGameButton.detectMouseInput(mousePosition):
#                     playGame()
#                 elif settingsButton.detectMouseInput(mousePosition):
#                     pass #put settings() here once it has been made
#                 elif closeButton.detectMouseInput(mousePosition):
#                     pygame.quit()
        
#         pygame.display.update()
                    
                    

        
        

# def settings():
#     while not done:
        
#         settingsMouseButton = pygame.mouse.get_pos()
#         settingsText = pygameGetFont(50).render("skibidi", True, "Green")
#         settingsRect = settingsText.get_rect(center=(700, 200))
#         screen.blit(settingsText, settingsRect)

#         settingsReturnButton = classes.generalpurposeButton(image=None, position=(1300,100), textinput="Return", font=pygameGetFont(25),
#         colour="Black", collisioncolour="Red")

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if settingsReturnButton.detectMouseInput(settingsMouseButton):
#                     menu()
        
#         pygame.display.update()



# def playGame():

#     pygame.display.set_caption("yeahyeah")

#     while not done:

#         playerMousePosition = pygame.mouse.get_pos()
#         screen.fill("black") #possibly not needed

#         returnButton = classes.generalpurposeButton(image=None, position=(1300, 0), textinput="Return", font=pygameGetFont(25), colour="Green", 
#         collisioncolour="Red")

#         returnButton.colourSwapOnHover(playerMousePosition)
#         returnButton.update(screen)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if returnButton.detectMouseInput(playerMousePosition):
#                     menu()
        
#         pygame.display.update()
        

        


    
#     pygame.display.flip()
 
#     clock.tick(15)
    
# pygame.quit()


