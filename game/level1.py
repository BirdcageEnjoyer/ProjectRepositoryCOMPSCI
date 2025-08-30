import pygame
import colours
import classes

#top, bottom or left, right
boundaryPlatform1_Y = [600, 900]
boundaryPlatform2_Y = [600, 900]
boundaryPlatform1_X = [0, 500]
boundaryPlatform2_X = [600, 1200]
boundaryLavaBlock1_x = [500, 600]
boundaryLavaBlock1_Y = [850, 900]
boundaryEndBlock1_X = [1120, 1170]
boundaryEndBlock1_Y = [400, 550]

startPositionX = 15
startPositionY = 600





# platform1 = classes.PlatformBlock(0, 600, 500, 300, colours.GREEN)
platform2 = classes.PlatformBlock(600, 600, 600, 300, colours.GREEN)
platform3 = classes.PlatformBlock(500, 850, 100, 50, colours.BLACK)
platform4 = classes.PlatformBlock(1120, 400, 50, 150, colours.YELLOW)
# movingPlatform1 = classes.MovingPlatformBlock(250, 250, 100, 100, 900, 500, 100, 50, colours.PURPLE, 5, 5)



level1platforms = pygame.sprite.Group()
# level1platforms.add(platform1)
level1platforms.add(platform2)
level1platforms.add(platform3)
level1platforms.add(platform4)
# level1platforms.add(movingPlatform1)




def drawLevel(givenScreen): #rectangles 3rd parameter follow x, y, xlength, ylength, also draws from the position given, towards the right, and down
    # pygame.draw.rect(givenScreen, platformColour, [0, 600, 500, 300]) #Platform1
    # pygame.draw.rect(givenScreen, platformColour, [600, 600, 600, 300]) #Platform2
    # pygame.draw.rect(givenScreen, damageBlockColour, [500, 850, 100, 50]) #LavaBlock1
    # pygame.draw.rect(givenScreen, endBlockColour, [1120, 400, 50, 150])
    
    # platform1.drawPlatform(givenScreen)
    platform2.drawPlatform(givenScreen)
    platform3.drawPlatform(givenScreen)
    platform4.drawPlatform(givenScreen)
    
    
