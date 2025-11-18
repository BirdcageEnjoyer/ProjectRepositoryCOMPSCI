import pygame
import colours
import level1
import level2
import level3



class Character(pygame.sprite.Sprite):
    
    def __init__(self, width, height, X, Y, currentLevel): # add more parameters later like difficulty, 
        super().__init__()
        self.playerImage = pygame.Surface((100, 50))
        self.playerImage.fill(colours.RED)
        self.rect = self.playerImage.get_rect(topleft=(700, 500)) #50 50
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
            self.gravity = -22.3 #make it so that when jumping, once you collide and are on something, then you can jump again, put if statement here
            # self.isTouchingGround = False    # uncomment when collisions are added
            
    def update(self, platformList):

        self.rect.x += self.velX
    

        collisionList = pygame.sprite.spritecollide(self, platformList, False) # this variable is a list of objects from the group of sprites that
        #include the platforms of the level the character is on that can be stood on that my character has collided with

       
    
        for block in collisionList:
            if self.rect.colliderect(block.rect):
        
                if self.movingLeft == True:
                    self.rect.left = block.rect.right
                elif self.movingRight == True:
                    self.rect.right = block.rect.left
        # the for loop goes through every object that we have collided with and then the nested if statement checks for collision of my player's
        # rectangular hitbox against the object's rectangular hitbox, the method i choose to use here is colliderect which uses rectangles to check
        # for collisions
        # if a collision is detected, if i am moving to the right, then that has to mean im on the left side of a platform, so it stops me from going
        # through the left side, and vice versa if i am coming in from the right


        self.addGravity() #applies gravity before updating vertical velocity
        if self.velY > 20: 
            self.velY = 20
        self.rect.y += self.velY

        collisionList = pygame.sprite.spritecollide(self, platformList, False) #refreshes collisionList as it is now stale, if we used the
        #collisionList from before, the variable is detecting collision from the previous position, after self.rect.x has been updated via self.velx
        #

        self.isTouchingGround = False
        
        for block in collisionList:
            
            if self.rect.colliderect(block.rect):
                if self.velY > 0:
                    self.rect.bottom = block.rect.top
                    self.velY = 0
                    self.isTouchingGround = True
                elif self.velY < 0:
                    self.rect.top = block.rect.bottom
                    self.velY = 0
        # since gravity is being added every iteration of update(), i have to reset vertical velocity so that the player doesn't fall through from the
        # top, or go into the platform from below

        if self.isTouchingGround == True:
            self.velY = 0

        if self.health <= 0:
            self.lives -= 1
            if self.lives <= 0:
                pass #self.rect.x, self.rect.y = beginning position x, beginning position y




    def collisionwithkillblock(self, killBlockList):
        for block in killBlockList:
            if self.rect.colliderect(block.rect):
                self.health -= 50






    
    def incrementLevel(self):
        self.level += 1
    
    # def drawPlayer(self, screen):
    #     pygame.draw.rect(screen, colours.RED, [self.centreX, self.centreY, self.width, self.height]) #DO

    


class PlatformBlock(pygame.sprite.Sprite):
    def __init__(self, xPos, yPos, length, height, colour):
        super().__init__()
        self.blockImage = pygame.Surface((length, height))
        self.blockImage.fill(colour)
        # self.blockImage = pygame.image.load("platform1tile.png").convert()
        self.rect = self.blockImage.get_rect(topleft=(xPos, yPos))
        self.xPosition = xPos
        self.yPosition = yPos
        self.length = length
        self.height = height
        self.colour = colour
         #gets the topleft corner of the block

    # def drawPlatform(self, givenScreen):
    #     pygame.draw.rect(givenScreen, self.colour, [self.xPosition, self.yPosition, self.length, self.height])




class MovingPlatformBlock(pygame.sprite.Sprite):
    def __init__(self, X, Y, lowerboundx,lowerboundy, upperboundx, upperboundy, length, height, colour, velX, velY):
        super().__init__()
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
        if self.rect.x <= self.lowerx:
            self.rect.x += self.velX
        if self.rect.x >= self.upperx:
            self.rect.x -= self.velX
        if self.rect.y <= self.lowery:
            self.rect.y += self.velY
        if self.rect.y >= self.uppery:
            self.rect.y -= self.velY

        

class MenuButton(pygame.sprite.Sprite):
    def __init__(self, image, x, y, textinput, font, colour, hovercolour):
        super().__init__()
        self.buttonImage = image
        self.rect = self.buttonImage.get_rect(topleft=(x, y))
        


        self.X = x
        self.Y = y
        self.font = font
        self.colour = 0

    def drawButtonOntoScreen(self, givenScreen):
        givenScreen.blit(self.buttonImage, (self.rect.x, self.rect.y))






class KillBlock(pygame.sprite.Sprite):
    def __init__(self, x, y, length, height, colour, collisionList):
        super().__init__()
        self.x = x
        self.y = y
        # self.colour = colour
        # self.killblockImage = pygame.Surface((self.x, self.y))
        self.killblockImage = pygame.image.load("").convert()
        # self.killblockImage.fill(self.colour)
        self.rect = self.killblockImage.get_rect(topleft=(self.x, self.y))
        self.collisionList = collisionList
                            


    def dealDamage(self, health):
        health -= 50 





