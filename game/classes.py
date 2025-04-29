import pygame
import colours
import level1
import level2
import level3



class Character(pygame.sprite.Sprite):
    
    def __init__(self, width, height,centreXval, centreYval, currentLevel): # add more parameters later like difficulty, 
        super().__init__()
        self.playerImage = pygame.Surface([50, 50])
        self.playerImage.fill(colours.RED)
        self.rect = self.playerImage.get_rect(topleft=(50, 50))
        self.centreX = centreXval
        self.centreY = centreYval
        self.level = currentLevel
        self.width = width
        self.height = height
        self.health = 100
        self.lives = 10
        self.velX = 0
        self.velY = 0
        self.gravity = 0
        self.isTouchingGround = True #by default starts as true because player will be spawning on a block
        #self. multipliers, difficulty etc later on
    
    def addGravity(self):
        self.gravity += 1
        self.velY = self.gravity

    def jumpControl(self):
        if self.isTouchingGround == True:
            self.gravity = -16 #make it so that when jumping, once you collide and are on something, then you can jump again, put if statement here
            # self.isTouchingGround = False    # uncomment when collisions are added
            
    def update(self):
        self.addGravity()
        self.rect.y += self.velY

        collisionBetweenBlockList = pygame.sprite.spritecollide(self, level1.level1platforms, False)
        for platform in collisionBetweenBlockList:
            if self.velY > 0:
                self.rect.bottom = platform.rect.top
                self.velY
    
    def incrementLevel(self):
        self.level += 1
    
    def drawPlayer(self, screen):
        pygame.draw.rect(screen, colours.RED, [self.centreX, self.centreY, self.width, self.height]) #DO


class PlatformBlock(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, length, height, colour):
        super().__init__()
        self.xPosition = xPos
        self.yPosition = yPos
        self.length = length
        self.height = height
        self.colour = colour
        self.blockImage = pygame.Surface([length, height])
        self.rect = self.blockImage.get_rect(topleft=(xPos, yPos)) #gets the topleft corner of the block

    def drawPlatform(self, givenScreen):
        pygame.draw.rect(givenScreen, self.colour, [self.xPosition, self.yPosition, self.length, self.height])


testPlatform = PlatformBlock(24, 48, 123, 445, colours.BLACK)


