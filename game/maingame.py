#all modules
import pygame
import level1
import level2
import level3
import colours
#w
#W
#variables defined here
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SKY = (149, 186, 245)
movingUp = False
movingDown = False
movingLeft = False
movingRight = False
isTouchingGround = True #when player first spawns in, always set to true to begin with, the player wont start falling from the air
GRAVITY = 2

setOfMovements = {pygame.K_w: "movingUp", pygame.K_s: "movingDown", pygame.K_a: "movingLeft", pygame.K_d: "movingRight"}
    # use later for movements instead of if statements

#classes defined here
class Character(pygame.sprite.Sprite):
    
    def __init__(self, colour, width, height, radius, centreXval, centreYval, currentLevel): # add more parameters later like difficulty, 
        super().__init__()
        self.width = width
        self.height = height
        self.colour = colour
        self.radius = radius
        self.centreX = centreXval
        self.centreY = centreYval
        self.level = currentLevel
        self.health = 100
        self.lives = 10
        #self. multipliers, difficulty etc later on
    
    def incrementLevel(self):
        self.level += 1
    
    def drawPlayer(self):
        pygame.draw.circle(screen, BLACK, [self.centreX + 7.5, self.centreY - 13], self.radius)
        pygame.draw.rect(screen, RED, [self.centreX, self.centreY, self.width, self.height])

    






        



        
x = 50 # test position variables
y = 590
resetX = 50
resetY = 590
levelBeginningX = 50 #set to the beginning value for each level later, add a beginning value for each level
levelBeginningY = 250

allSpritesList = pygame.sprite.Group()

player = Character(RED, 15, 30, 15, levelBeginningX, levelBeginningY, 1)
allSpritesList.add(player)



#initialise pygame
pygame.init()
#screen dimensions and setup
size = (1200, 900)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

done = False

clock = pygame.time.Clock()
 
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN: # later on, make variables for the keys so that the player can change the keys for movement, then replace k_...
            #with the variables so that depending on which key the player sets to as move up left right down, it will move accordingly ...
            if event.key == pygame.K_SPACE: #for now use up, replace with w later
                movingUp = True
            if event.key == pygame.K_s:
                movingDown = True
            if event.key == pygame.K_a:
                movingLeft = True
            if event.key == pygame.K_d:
                movingRight = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE: #line 75
                movingUp = False
            if event.key == pygame.K_s:
                movingDown = False
            if event.key == pygame.K_a:
                movingLeft = False
            if event.key == pygame.K_d:
                movingRight = False

    if movingUp == True:    
        if player.centreY > 10: # replace Y and X later with character class's Y and X line 39, 40
            player.centreY -= 5 #pygame's cartesian coordinate system: Up = decrease, down = increase, left right remain same orientation        
    if movingDown == True:
        if player.centreY < 890:
            player.centreY += 5
    if movingLeft == True:
        if player.centreX > 10:
            player.centreX -= 5
    if movingRight == True:
        if player.centreX < 1190:
            player.centreX += 5
    
    
    #add boundaries 


    screen.fill(SKY)
    #drawing code below

    pygame.draw.circle(screen, (255,0,0), [x,y], 10)
    player.drawPlayer()

    
    if player.level == 1:
        level1.drawLevel(screen, GREEN, RED, YELLOW, BLACK)
        levelBeginningX = level1.startPositionX
        levelBeginningY = level1.startPositionY
    if player.level == 2:
        level2.drawLevel(screen, GREEN, RED, YELLOW) # parameters for these 2 levels for now are just placeholders.
        #levelBeginningX = level2.startPositionX
        #levelBeginningY = level2.startPositionY
    if player.level == 3:
        level3.drawLevel(screen, GREEN, RED, YELLOW)
        #levelBeginningX = level3.startPositionX
        #levelBeginningY = level3.startPositionY
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
