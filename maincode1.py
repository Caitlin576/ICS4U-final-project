import pygame, random

from car import Car
from obstacles import Obstacles
from boundary import Boundary
#from movingBG import moveBG
#from background import Background
pygame.init()
 
GREEN = (13, 160, 21)
        
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Racing")

all_sprites = pygame.sprite.Group()

player_list = pygame.sprite.Group()

obs_list = pygame.sprite.Group()

boundary_list = pygame.sprite.Group()
 
playerCar = Car()
playerCar.rect.x = 200
playerCar.rect.y = 400
 
player_list.add(playerCar)

ob1 = Obstacles()
ob2 = Obstacles()
ob3 = Obstacles()
ob4 = Obstacles()

obs_list.add(ob1, ob2, ob3, ob4)

bound1 = Boundary(100, 100)
bound2 = Boundary(200, 200)

boundary_list.add(bound1, bound2)

#bg_list = pygame.sprite.Group()

#bg1 = Background(0)
#bg2 = Background(600)

#bg_list.add(bg1, bg2)

bg = pygame.image.load("road2.png")


def drawSprites():
    screen.fill(GREEN)
    #moveBG(screen, bg)
    screen.blit(bg, (0, bgY))
    screen.blit(bg, (0, bgY2))
    boundary_list.draw(screen)
    #bg_list.draw(screen)
    obs_list.draw(screen)
    player_list.draw(screen)
    


bgY = 0
bgY2 = bg.get_height()
   
 

running = True
clock=pygame.time.Clock()


 
while running:

    bgY -= 1.4
    bgY2 -= 1.4
    if bgY < bg.get_height() * -1:
        bgY = bg.get_height()
    if bgY2 < bg.get_height() * -1:
        bgY2 = bg.get_height()
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
 
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(5)
        
        #Game Logic
    player_list.update()
 
        #Drawing on Screen
    drawSprites()   
 
        #Refresh Screen
    pygame.display.update()
 
        #Number of frames per secong e.g. 60
    clock.tick(60)
 
pygame.quit() 
