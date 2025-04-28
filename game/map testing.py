
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
  

    




    screen.fill(WHITE)

    pygame.display.flip()
 

    clock.tick(60)
 

pygame.quit()
