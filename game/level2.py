import pygame
import colours

def drawLevel(givenScreen, platformColour, killBlockColour, endBlockColour, damageBlockColour):
    pygame.draw.rect(givenScreen, platformColour, [0, 600, 500, 300])