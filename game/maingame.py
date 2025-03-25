
#all modules


import pygame
import level1
import level2
import level3





 
#variables defined here
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
movingUp = False
movingDown = False
movingLeft = False
movingRight = False
GRAVITY = 2

setOfMovements = {pygame.K_w: "movingUp", pygame.K_s: "movingDown", pygame.K_a: "movingLeft", pygame.K_d: "movingRight"}
    # use later for movements instead of if statements

#classes defined here
class Character(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, radius, centreXval, centreYval):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.radius = radius
        self.centreX = centreXval
        self.centrey = centreYval
        

x = 0
y = 0


allSpritesList = pygame.sprite.Group()

player = Character(RED, 2, 2, 2, 2, 2)
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
            if event.key == pygame.K_w:
                movingUp = True
            if event.key == pygame.K_s:
                movingDown = True
            if event.key == pygame.K_a:
                movingLeft = True
            if event.key == pygame.K_d:
                movingRight = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                movingUp = False
            if event.key == pygame.K_s:
                movingDown = False
            if event.key == pygame.K_a:
                movingLeft = False
            if event.key == pygame.K_d:
                movingRight = False
            
    if movingUp == True: # add boundaries later so that it only moves if it isnt already at screen boundary
        y -= 5 #pygame's cartesian coordinate system: Up = decrease, down = increase, left right remain same orientation
    if movingDown == True:
        y += 5
    if movingLeft == True:
        x -= 5
    if movingRight == True:
        x += 5

    




    screen.fill(WHITE)

    pygame.draw.circle(screen, (255,0,0), [x,y], 10)

    pygame.display.flip()
 

    clock.tick(60)
 

pygame.quit()
