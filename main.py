import sys, pygame, random, car
from car import *

pygame.init()
pygame.key.set_repeat(10)

black = 0, 0, 0
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

player = playerCar(width, height)
oponents = []
maxOponents = 5

CREATE_OPONENT_TIMER = pygame.USEREVENT
MOVE_OPONENT_TIMER = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_OPONENT_TIMER, 500)
pygame.time.set_timer(MOVE_OPONENT_TIMER, 2) 

CARS_IN_LEVEL = 20
level = 1
untilLevelUp = CARS_IN_LEVEL

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            player.move(pygame.key.name(event.key))
            
        elif event.type == pygame.KEYUP:
            player.stopMoving(pygame.key.name(event.key))
            
        elif event.type == CREATE_OPONENT_TIMER:
            if None in oponents:
                oponents.remove(None)
            if untilLevelUp <= 0: # Level up
                untilLevelUp = CARS_IN_LEVEL
                level = level +1
                maxOponents = maxOponents + 3
            elif (len(oponents) < maxOponents) and (random.randint(0, 1) == 0):
                oponents.append(oponentCar(width, height, masterImage, level))
        
        elif event.type == MOVE_OPONENT_TIMER:
            for oponent in oponents:
                if oponent is not None:
                    if oponent.getBrakingTime() == 100 / oponent.getSpeed():
                        oponent.setBrakingTime(0)
                        oponent.move()
                        if oponent.getPosY() > height:
                            oponents[oponents.index(oponent)] = None
                            untilLevelUp = untilLevelUp - 1
                    else:
                        oponent.setBrakingTime(oponent.getBrakingTime() + 1)


    screen.fill(black)
    playerRect = screen.blit(PLAYER_SPRITES[player.getCurrentSprite()], (player.getPosX(), player.getPosY()))    
    
    for oponent in oponents:
        if oponent is not None:
            oponentRect = screen.blit(OPONENT_SPRITES[oponent.getCurrentSprite()],(oponent.getPosX(), oponent.getPosY()))
            if playerRect.colliderect(oponentRect):
                for i in range(1,10):
                    for color in ((255,0,0), black):
                        pygame.time.delay(300)
                        screen.fill(color)
                        screen.blit(pygame.font.Font(None, 150).render("GAME OVER", True, (255,0, 0)), (0,height/2))
                        pygame.display.flip()
                sys.exit()

    screen.blit(pygame.font.Font(None, 25).render("Level " + str(level), True, (255,255, 255)), (0,0))
    
    pygame.display.flip()
    
