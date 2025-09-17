import pygame
import colours
import classes
import camera
#top, bottom or left, right
boundaryPlatform1_Y = [600, 900]
boundaryPlatform2_Y = [600, 900]
boundaryPlatform1_X = [0, 500]
boundaryPlatform2_X = [600, 1200]
boundaryLavaBlock1_x = [500, 600]
boundaryLavaBlock1_Y = [850, 900]
boundaryEndBlock1_X = [1120, 1170]
boundaryEndBlock1_Y = [400, 550]

startPositionX = 15
startPositionY = 600





platform1 = classes.PlatformBlock(0, 600, 500, 300, colours.GREEN)
platform2 = classes.PlatformBlock(600, 600, 600, 300, colours.GREEN)
platform3 = classes.PlatformBlock(500, 800, 100, 50, colours.BLACK)
platform4 = classes.PlatformBlock(1120, 400, 50, 150, colours.YELLOW)
platform5 = classes.PlatformBlock(1250, 400, 600, 300, colours.PINK)
movingPlatform1 = classes.MovingPlatformBlock(250, 400, 100, 100, 900, 500, 100, 50, colours.PURPLE, 5, 5)



level1platforms = pygame.sprite.Group()


level1platforms.add(platform1)
level1platforms.add(platform2)
level1platforms.add(platform3)
# level1platforms.add(platform4)
level1platforms.add(platform5)
level1platforms.add(movingPlatform1)




def drawLevel(givenScreen, offsetX, offsetY): #rectangles 3rd parameter follow x, y, xlength, ylength, also draw from the position given, towards the right, and down

    movingPlatform1.move()
    
    givenScreen.blit(platform2.blockImage, (platform2.rect.x - offsetX, platform2.rect.y - offsetY))
    givenScreen.blit(platform1.blockImage, (platform1.rect.x - offsetX, platform1.rect.y - offsetY))
    givenScreen.blit(platform3.blockImage, (platform3.rect.x - offsetX, platform3.rect.y - offsetY))
    # givenScreen.blit(platform4.blockImage, (platform4.rect.x - offsetX, platform4.rect.y - offsetY))
    givenScreen.blit(movingPlatform1.image, (movingPlatform1.rect.x - offsetX, movingPlatform1.rect.y - offsetY))
    givenScreen.blit(platform5.blockImage, (platform5.rect.x - offsetX, platform5.rect.y - offsetY))
