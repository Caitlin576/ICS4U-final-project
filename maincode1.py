import pygame, random

from car import Car
from obstacles import Obstacles
from boundary import Boundary
from finish import Finish
#from movingBG import moveBG
#from background import Background
pygame.init()
 
GREEN = (13, 160, 21)

currentDirA = ''
currentDirB = ''

bgCount = 0

screenw = 600
screenh = 600
screen = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("Game")

all_sprites = pygame.sprite.Group()

player_list = pygame.sprite.Group()

obs_list = pygame.sprite.Group()

boundary_list = pygame.sprite.Group()
 
playerCar = Car(200, 450)
 
player_list.add(playerCar)

for i in range(3):
    obst = Obstacles(screen)
    obst.rect.x = random.randrange(screenw - 64)
    obst.rect.y = random.randrange(screenh - 64)
    obs_list.add(obst)

boundLeft = Boundary(50)
boundRight = Boundary(550)


boundary_list.add(boundLeft, boundRight)

finishLine = Finish()

#bg_list = pygame.sprite.Group()

#bg1 = Background(0)
#bg2 = Background(600)

#bg_list.add(bg1, bg2)

bg = pygame.image.load("wideroad.png")


def drawSprites():
    screen.fill(GREEN)
    #moveBG(screen, bg)
    screen.blit(bg, (50, bgY))
    screen.blit(bg, (50, bgY2))
    boundary_list.draw(screen)
    #bg_list.draw(screen)
    #obs_list.draw(screen)
    player_list.draw(screen)
    


bgY = 0
bgY2 = bg.get_height()
   
 

running = True
clock=pygame.time.Clock()


 
while running:

    #currentTime = pygame.time.get_ticks()

    #if pygame.time.get_ticks >= 15000:
        #screen.

    #bgY -= 1.4
    #bgY2 -= 1.4
    #if bgY < bg.get_height() * -1:
        #bgY = bg.get_height()
    #if bgY2 < bg.get_height() * -1:
        #bgY2 = bg.get_height()
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
 
    keys = pygame.key.get_pressed()
        
    if keys[pygame.K_LEFT]:
        currentDirA = 'l'
        currentDirB = 'l'
        playerCar.moveLeft()
        
    if keys[pygame.K_RIGHT]:
        currentDirA = 'r'
        currentDirB = 'r'
        playerCar.moveRight()
        
    if keys[pygame.K_DOWN]:
        #currentDir = 'u'
        currentDirB = 'u'
        playerCar.moveUp()

        
    if keys[pygame.K_UP]:
        #currentDir = 'd'
        currentDirB = 'd'

        if playerCar.rect.y > 350:
            playerCar.moveDown()
            
        else:
            bgY -= 4
            bgY2 -= 4
            
            if bgY < bg.get_height() *-1:
                bgY = bg.get_height()
                
                
            if bgY2 < bg.get_height() * -1:
                bgY2 = bg.get_height()
                

    if playerCar.rect.x < 0:
        playerCar.rect.x = 0
        
    if playerCar.rect.x > 536:
        playerCar.rect.x = 536

    if playerCar.rect.y > 536:
        playerCar.rect.y = 536
        
        
        #Game Logic
    player_list.update()
 
        #Drawing on Screen
    drawSprites()

    obs_list.update()

    obs_list.draw(screen)

    
    playerCar.collide(boundary_list, currentDirA)
    playerCar.collide(obs_list, currentDirB)

    for x in obs_list:
        x.bounce(player_list)


    #finishLine.appear(screen, bgCount)
 
        #Refresh Screen
    pygame.display.update()
 
        #Number of frames per secong e.g. 60
    clock.tick(60)
 
pygame.quit() 
