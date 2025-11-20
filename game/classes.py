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
        self.lives = 3
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
        changeinX = 0
        changeinY = 0
        self.rect.x += self.velX
        changeinX = self.velX
        collisionuncertainty = 25
    

    
        # for block in collisionList:
        #     if block.colliderect(self.rect.x + changeinX, self.rect.y, self.width, self.height):
        #         changeinX = 0
        #     if block.colliderect(self.rect.x, self.rect.y + changeinY, self.width, self.height):
        #         if self.velY >= 0:
        #             changeinY = block.bottom - self.rect.top
        #             self.velY = 0
        #         elif self.velY < 0:
        #             changeinY = block.top - self.rect.bottom
        #             self.velY = 0
        #             self.isTouchingGround = False

        collisionList = pygame.sprite.spritecollide(self, platformList, False) # this variable is a list of objects from the group of sprites that
        #include the platforms of the level the character is on that can be stood on that my character has collided with

       
    
        for block in collisionList:
            if isinstance(block, PlatformBlock):
                if self.rect.colliderect(block.rect):
        
                    if self.movingLeft == True:
                        self.rect.left = block.rect.right
                    elif self.movingRight == True:
                        self.rect.right = block.rect.left
            if isinstance(block, MovingPlatformBlock):
                if self.rect.colliderect(block.rect):
                    # if block.velX > 0 and (self.rect.x >= block.rect.x):
                    #     self.rect.left = block.rect.right
                    # if block.velX <= 0 and (self.rect.x >= block.rect.x):

                    if self.rect.x >= block.rect.x:
                        self.rect.left = block.rect.right
                    if self.rect.x <= block.rect.x:
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
        changeinY += self.velY

        collisionList = pygame.sprite.spritecollide(self, platformList, False) #refreshes collisionList as it is now stale, if we used the
        #collisionList from before, the variable is detecting collision from the previous position, after self.rect.x has been updated via self.velx
        #

        self.isTouchingGround = False
        
        for block in collisionList:
            # if isinstance(block, MovingPlatformBlock):
            #     self.rect.x += block.velX  this caused an issue because it was checked before the standard collision checks
            if self.rect.colliderect(block.rect):
                # if isinstance(block, PlatformBlock):
                    if self.velY > 0:
                        self.rect.bottom = block.rect.top
                        self.velY = 0
                        self.isTouchingGround = True

                    # if isinstance(block, MovingPlatformBlock): #isinstance checks if the block that we are currently inspecting is of the class 
                    #     #for moving platforms
                    #     self.rect.x += block.velX 
                    #     self.rect.y += block.velY
                    elif self.velY < 0:
                        self.rect.top = block.rect.bottom
                        self.velY = 0
                    collisionList = pygame.sprite.spritecollide(self, platformList, False)

                    if isinstance(block, MovingPlatformBlock):
                        self.rect.x += block.velX * 2
                # if isinstance(block, MovingPlatformBlock):
                #     if self.velY > 0:
                #         self.rect.bottom = block.rect.top
        
        # collisionList = pygame.sprite.spritecollide(self, platformList, False)
        

    
            
            
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
    # unnecessary now that i have a procedure that draws each block in each level


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
        self.image = pygame.Surface((200, 100))
        self.image.fill(colours.PURPLE)
        self.rect = self.image.get_rect(topleft=(X,Y))
        self.platformGoLeft = False
        self.platformGoRight = False
        
    
    def move(self):
        self.rect.y += self.velY
        self.rect.x += self.velX

        if self.rect.left < min(self.lowerx, self.upperx) or self.rect.left > max(self.lowerx, self.upperx):
            self.velX = self.velX * -1

        
        if self.rect.top < min(self.lowery, self.uppery) or self.rect.top > max(self.lowery, self.uppery):
            self.velY = self.velY * -1
        
        # if self.velX > 0:
        #     self.platformGoRight = True
        # elif self.velX < 0:
        #     self.platformGoLeft = True

    def velToAddOn(self, playerVelX, playerVelY, needX, needY):
        if needX == True:
            return playerVelX - self.velX
        elif needY == True:
            pass #figure this out later


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


class generalpurposeButton(pygame.sprite.Sprite):
    def __init__(self, image, position, font, colour, collisioncolour, textinput):
        self.image = image
        self.position = position
        self.x = position[0]
        self.y = position[1]
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.font = font
        self.colour = colour
        self.collisioncolour = collisioncolour
        self.textinput = textinput
        self.displayedtext = self.font.render(self.textinput, True, self.colour)
        self.textrect = self.displayedtext.get_rect(center=(self.x, self.y))
        if self.image is not None:
            self.image = self.displayedtext
        

    
        self.textrect = self.displayedtext.get_rect(center=(self.x, self.y))

    def update(self, givenScreen):
        if self.image is not None:
            givenScreen.blit(self.image, self.rect)
        givenScreen.blit(self.displayedtext, self.textrect)
    
    def detectMouseInput(self, mouseposition):
        # if mouseposition[0] in range(self.rect.left, self.rect.right) and mouseposition[1] in range(self.rect.top, self.rect.bottom):
        #     return True
        # else:
        #     return False
        return self.rect.collidepoint(mouseposition)
        
    def colourSwapOnHover(self, mouseposition):
        if mouseposition[0] in range(self.rect.left, self.rect.right) and mouseposition[1] in range(self.rect.top, self.rect.bottom):
            self.displayedtext = self.font.render(self.textinput, True, self.collisioncolour)
        else:
            self.displayedtext = self.font.render(self.textinput, True, self.colour)


