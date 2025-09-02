import pygame
import colours

platform1 = 0
platform2 = 0
platform3 = 0
#...

def drawLevel(givenScreen, platformColour, killBlockColour, endBlockColour, damageBlockColour):
    pygame.draw.rect(givenScreen, platformColour, [0, 600, 500, 300])
