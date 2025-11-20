
#all modules


import pygame
import level1
import level2
import level3
import sys
import classes


 
#variables defined here
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



#initialise pygame
pygame.init()




#111111111111111111111111111111111111111111111111111111111111111111111
background = pygame.Surface((0,0))

#screen dimensions and setup
size = (1200, 900)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
mainMenuBackground = pygame.image.load("Screenshot 2023-04-08 190551.png").convert()
done = False
def pygameGetFont(size):
    return pygame.font.Font("CedarvilleCursive-Regular.ttf", size)

clock = pygame.time.Clock()
 

def menu():
    while not done:
        screen.blit(mainMenuBackground, (0,0))

        mousePosition = pygame.mouse.get_pos()

        menuTitleText = pygameGetFont(50).render("Main menu", True, "#964B00")
        menuRect = menuTitleText.get_rect(center=(700, 200))

        startGameButton = classes.generalpurposeButton(image=pygame.image.load("Button rectangle.png"), position=(700, 300), textinput="Begin", 
        font=pygameGetFont(50), colour="#964B00", collisioncolour="Red")

        settingsButton = classes.generalpurposeButton(image=pygame.image.load("Button rectangle.png"), position=(700, 400), textinput="Settings",
        font=pygameGetFont(50), colour="#964B00", collisioncolour="Red")

        closeButton = classes.generalpurposeButton(image=pygame.image.load("Button rectangle.png"), position=(700, 500), textinput="Close",
        font=pygameGetFont(50), colour="#964B00", collisioncolour="Red")


        screen.blit(menuTitleText, menuRect)
        for i in range(3):
            buttons = [startGameButton, settingsButton, closeButton]
            buttons[i].colourSwapOnHover(mousePosition)
            buttons[i].update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startGameButton.detectMouseInput(mousePosition):
                    pass #put play() here once it has been made
                elif settingsButton.detectMouseInput(mousePosition):
                    pass #put settings() here once it has been made
                elif closeButton.detectMouseInput(mousePosition):
                    pygame.quit()
        
        pygame.display.update()

menu()


while not done:

    screen.fill(BLACK)
     
    playbutton = None










    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
  

    





    pygame.display.flip()
 

    clock.tick(60)
 

pygame.quit()


def mainMenu():
    while True:


        # screen.blit(, (0,0))
        pass