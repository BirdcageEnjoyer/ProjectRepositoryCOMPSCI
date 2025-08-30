import pygame
import colours
import level1
import level2
import level3



class Character(pygame.sprite.Sprite):
    
    def __init__(self, width, height,centreXval, centreYval, currentLevel): # add more parameters later like difficulty, 
        super().__init__()
        self.playerImage = pygame.Surface((50, 50))
        self.playerImage.fill(colours.RED)
        self.rect = self.playerImage.get_rect(topleft=(50, 50))
        # self.centreX = centreXval
        # self.centreY = centreYval
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
        self.movingLeft = False
        self.movingRight = False
    
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

        collisionList = pygame.sprite.spritecollide(self, level1.level1platforms, False)

        
        for block in collisionList:
            if self.rect.colliderect(block.rect):
                if self.velX > 0:
                    self.rect.x = block.rect.left
                elif self.velX < 0:
                    self.rect.x = block.rect.right


    







    


    # def detectCollision(self, levelsplatforms):
    #     collisionsList = pygame.sprite.spritecollide(self, levelsplatforms, False)
    #     print(collisionsList)
















    
    def incrementLevel(self):
        self.level += 1
    
    # def drawPlayer(self, screen):
    #     pygame.draw.rect(screen, colours.RED, [self.centreX, self.centreY, self.width, self.height]) #DO


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



class MovingPlatformBlock(pygame.sprite.Sprite):
    def __init__(self, X, Y, lowerboundx,lowerboundy, upperboundx, upperboundy, length, height, colour, velX, velY):
        super.__init__()
        self.X = X
        self.Y = Y
        self.lowerx = lowerboundx
        self.lowery = lowerboundy
        self.upperx = upperboundx
        self.uppery = upperboundy
        self.length = length
        self.height = height
        self.colour = colour
        self.velX = velX
        self.velY = velY
        self.image = pygame.Surface((60, 40))
        self.image.fill(colours.PURPLE)
        self.rect = self.image.get_rect(topleft=(X,Y))
    
    def move(self):
        if self.X <= self.lowerx:
            self.X += self.velX
        if self.X >= self.upperx:
            self.X -= self.velX
        if self.Y <= self.lowery:
            self.Y += self.velY
        if self.Y >= self.uppery:
            self.Y -= self.velY
        

class Button(pygame.sprite.Sprite):
    def __init__(self, image, pos, textinput, font, colour, hovercolour):
        super().__init__()
        self.image = image
        self.posx = pos[0]
        self.posy = pos[1]
        self.font = font
        self.colour = 0