import pygame
import colours
#top, bottom or left, right
boundaryPlatform1_Y = [600, 900]
boundaryPlatform2_Y = [600, 900]
boundaryPlatform1_X = [0, 500]
boundaryPlatform2_X = [600, 1200]
boundaryLavaBlock1_x = [500, 600]
boundaryLavaBlock1_Y = [850, 900]
boundaryEndBlock1_X = []
boundaryEndBlock1_Y = []

startPositionX = 15
startPositionY = 600

def drawLevel(givenScreen, platformColour, killBlockColour, endBlockColour, damageBlockColour): #rectangles 3rd parameter follow x, y, xlength, ylength, also draws from the position given, towards the right, and down
    pygame.draw.rect(givenScreen, platformColour, [0, 600, 500, 300]) #Platform1
    pygame.draw.rect(givenScreen, platformColour, [600, 600, 600, 300]) #Platform2
    pygame.draw.rect(givenScreen, damageBlockColour, [500, 850, 100, 50]) #LavaBlock1
    pygame.draw.rect(givenScreen, endBlockColour, [1120, 400, 50, 150])

    
