import pygame

camera = pygame.Rect(0,0,0,0)

def makeScreen(length, height, name):
    
    pygame.display.set_caption(name)
    screen = pygame.display.set_mode((length, height))

    camera.width = length
    camera.height = height

    return screen