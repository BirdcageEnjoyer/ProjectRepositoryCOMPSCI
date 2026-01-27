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

level1timelimit = 10



platform1 = classes.PlatformBlock(0, 600, 500, 300, colours.GREEN)
platform2 = classes.PlatformBlock(600, 600, 500, 300, colours.GREEN)
platform3 = classes.PlatformBlock(500, 800, 100, 50, colours.BLACK)
platform4 = classes.PlatformBlock(1120, 400, 50, 150, colours.YELLOW)
platform5 = classes.PlatformBlock(1400, 600, 500, 300, colours.GREEN)
platform6 = classes.PlatformBlock(2100, 400, 500, 300, colours.GREEN)
movingPlatform1 = classes.MovingPlatformBlock(1100, 400, 1100, 100, 1400, 100, 200, 200, colours.PURPLE, 3, 2)
platform7 = classes.PlatformBlock(-4000, 600, 4600, 300, colours.GREEN)


enemy1 = classes.BasicEnemy(700, 400, 650, 750, colours.RED, 3)

level1enemies = pygame.sprite.Group()
level1enemies.add(enemy1)


level1platforms = pygame.sprite.Group()


level1platforms.add(platform1)
level1platforms.add(platform2)
level1platforms.add(platform3)
level1platforms.add(platform4)
level1platforms.add(platform5)
level1platforms.add(platform6)
level1platforms.add(platform7)
level1platforms.add(movingPlatform1)

level1groundplatforms = pygame.sprite.Group()



def drawLevel(givenScreen, offsetX, offsetY): #rectangles 3rd parameter follow x, y, xlength, ylength, also draw from the position given, towards the right, and down

    movingPlatform1.move()
    givenScreen.blit(enemy1.image, (enemy1.rect.x - offsetX, enemy1.rect.y - offsetY))
    # givenScreen.blit(platform2.blockImage, (platform2.rect.x - offsetX, platform2.rect.y - offsetY))
    # givenScreen.blit(platform1.blockImage, (platform1.rect.x - offsetX, platform1.rect.y - offsetY))
    # # givenScreen.blit(platform3.blockImage, (platform3.rect.x - offsetX, platform3.rect.y - offsetY))
    # # givenScreen.blit(platform4.blockImage, (platform4.rect.x - offsetX, platform4.rect.y - offsetY))
    # givenScreen.blit(movingPlatform1.image, (movingPlatform1.rect.x - offsetX, movingPlatform1.rect.y - offsetY))
    # givenScreen.blit(platform5.blockImage, (platform5.rect.x - offsetX, platform5.rect.y - offsetY))
    # givenScreen.blit(platform6.blockImage, (platform6.rect.x - offsetX, platform6.rect.y - offsetY))

    # in order to make it more efficient, we can just use a for loop to iterate through every instance of the platforms of the map
    # and blit each platform onto the map

    for collidableplatform in level1platforms:
        if isinstance(collidableplatform, classes.MovingPlatformBlock):
            collidableplatform.move()
            givenScreen.blit(collidableplatform.image, (collidableplatform.rect.x - offsetX, collidableplatform.rect.y - offsetY))
        else:
            givenScreen.blit(collidableplatform.blockImage, (collidableplatform.rect.x - offsetX, collidableplatform.rect.y - offsetY))

