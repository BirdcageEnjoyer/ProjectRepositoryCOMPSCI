import pygame
import colours



startPositionX = 0 
startPositionY = 0

def drawLevel(givenScreen, givenColour, killBlockColour):
    pygame.draw.rect(givenScreen, givenColour, [300, 400, 500, 200])