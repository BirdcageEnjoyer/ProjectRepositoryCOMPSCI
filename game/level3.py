import pygame
import colours

def drawLevel(givenScreen, givenColour, killBlockColour):
    pygame.draw.rect(givenScreen, givenColour, [300, 400, 500, 200])