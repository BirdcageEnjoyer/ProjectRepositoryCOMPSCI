
import pygame
import json


class Spritesheet():
    def __init__(self, sheetFileName):
        self.filename = sheetFileName
        self.spriteSheet = pygame.image.load(sheetFileName).convert()
        self.metaData = self.filename.replace('png', 'json')
        with open(self.metaData):
            self.data = json.load(self.metaData)
        self.metaData.close()

    def getSprite(self, x, y, width, height):
        sprite = pygame.Surface((width, height))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.spriteSheet, (0,0), (x, y, width, height))
        return sprite
    
    def splitSprite(self, name):
        sprite = self.data['frames'][name]['frame']
        x = sprite["x"]
        y = sprite["y"]
        width = sprite["w"]
        height = sprite["h"]
        image = self.getSprite(x, y, width, height)
        return image