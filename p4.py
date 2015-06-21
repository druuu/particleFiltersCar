import pygame, time
from pygame.locals import *

#necessary pygame initializing
pygame.init()

#create a surface that will be seen by the user
screen =  pygame.display.set_mode((400, 400))

#create a varible for degrees pf rotation
degree = 0
while True:
    #clear screen at the start of every frame
    screen.fill((40, 40, 40)) # Hash

    #create new surface with white BG
    surf =  pygame.Surface((100, 100))
    surf.fill((255, 255, 255)) # White
    #set a color key for blitting
    surf.set_colorkey((255, 0, 0)) #Red

    #create shapes so you can tell rotation is happenning
    #bigger =  pygame.Rect(10, 10, 10, 10)
#    smaller = pygame.Rect(25, 50, 50, 50)

    #draw those two shapes to that surface
    pygame.draw.rect(surf, (0, 0, 0), Rect(10, 10, 10, 10)) # Brown
    #pygame.draw.rect(surf, (100, 0, 0), smaller) # Brown

    ##ORIGINAL UNCHANGED
    #what coordinates will the static image be placed:
    #where = 200, 200

    #draw surf to screen and catch the rect that blit returns
    #blittedRect = screen.blit(surf, where)
    #screen.fill((40,40,40))

    ##ROTATED
    #get center of surf for later
    #oldCenter = blittedRect.center

    #rotate surf by DEGREE amount degrees
    rotatedSurf =  pygame.transform.rotate(surf, degree)

    #get the rect of the rotated surf and set it's center to the oldCenter
    #rotRect = rotatedSurf.get_rect()
    #print rotRect
    #rotRect.center = oldCenter

    #draw rotatedSurf with the corrected rect so it gets put in the proper spot
    screen.blit(rotatedSurf, Rect(70,70,0,0))

    #change the degree of rotation
    degree += 45 
    if degree > 45:
        degree = 0
    time.sleep(2)

    #show the screen surface
    pygame.display.flip()

    #wait 60 ms until loop restart
    pygame.time.wait(60)
