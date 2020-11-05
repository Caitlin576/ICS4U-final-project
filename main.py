import pygame, random

from car import Car
from obstacles import Obstacles
from boundary import Boundary
from finish import Finish
from pitstop import Pitstop
from text import Text

pygame.init()
 
GREEN = (13, 160, 21)
BLUE = (39, 188, 204)
BLACK = (0, 0, 0)
GREY = (173, 173, 173)
WHITE = (255, 255, 255)

#easyButton = Text('Courier', BLACK, 40, 'Easy')
#easyHover = Text('Courier', GREY, 40, 'Easy')
#hardButton = Text('Courier', BLACK, 40, 'Hard')
#hardHover = Text('Courier', GREY, 40, 'Hard')

startScore = 100
currentDirA = ''
currentDirB = ''

level = 0

bgCount = 0

screenw = 640
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

bg = pygame.image.load("wideroad.png")

scoreFont = pygame.font.SysFont('Courier', 20)

menuFont = pygame.font.SysFont('Courier', 40)

finishLineVisible = False

finishY = -4

print("finishY:", finishY)

finishImage = Finish()

finishGroup = pygame.sprite.Group()

finishGroup.add(finishImage)

pitStop = Pitstop()

pitGroup = pygame.sprite.Group()

pitGroup.add(pitStop)



def drawSprites():
    global FinishLineVisible 

    screen.fill(GREEN)

    screen.blit(bg, (50, bgY))
    screen.blit(bg, (50, bgY2))
    player_list.update()

    
    text = scoreFont.render(str(playerCar.score), 1, (0, 0, 0))
    screen.blit(text, (570, 10))
    
    boundary_list.draw(screen)

    if bgCount > 2000:
        print("finsh drawn")
        finishGroup.draw(screen)


    if bgCount > 1000:
        pitGroup.draw(screen)
            
    player_list.draw(screen)
    obs_list.update()
    obs_list.draw(screen)


def endScreenLoss():
    global pause, bgCount
    bgCount = 0
    pause = 0
    running = True
    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                playerCar.score = startScore
                running = False
        playerCar.rect.x = 200
        playerCar.rect.y = 450
        screen.fill(BLUE)
        gameOver = menuFont.render("Game Over!", 1, (0, 0, 0))
        screen.blit(gameOver, (screenw/2 - gameOver.get_width()/2, 200))
        playAgain = menuFont.render("Click to play again", 1, (0, 0, 0))
        screen.blit(playAgain, (screenw/2 - playAgain.get_width()/2, 300))
        playerCar.score = startScore
        pygame.display.update()

def endScreenWin():
    global pause, bgCount
    bgCount = 0
    pause = 0
    running = True

    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                playerCar.score = 100
                running = False

        print("score:", playerCar.score)
        playerCar.rect.x = 200
        playerCar.rect.y = 450
        screen.fill(BLUE)
        yourScore = menuFont.render("Your score:", 1, BLACK)
        screen.blit(yourScore, (screenw/2 - yourScore.get_width()/2, 200))
        playAgain = menuFont.render("Click to play again", 1, (0, 0, 0))
        screen.blit(playAgain, (screenw/2 - playAgain.get_width()/2, 300))

        playerCar.score = startScore

        #newScore = menuFont.render("New score:", 1, BLACK)
        #screen.blit(newScore, (screenw/2 - newScore.get_width()/2, 350))

        

        pygame.display.update()
  

bgY = 0
bgY2 = bg.get_height()

pause = 0
speed = 60

running = True
clock=pygame.time.Clock()


 
while running:    

    if pause > 0:
        print("pause greater than zero")
        pause += 1
        print("pause", pause)
        if pause == 2:
            print("pause == 2")
            pygame.time.delay(600)
            endScreenLoss()
    
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
        currentDirB = 'd'
        playerCar.moveDown()


    if keys[pygame.K_UP]:
        currentDirB = 'u'

        if playerCar.rect.y > 350:
            playerCar.moveUp()

        else:

            bgY += 4
            bgY2 += 4

            if bgY > bg.get_height():
                bgY = bg.get_height() * -1


            if bgY2 > bg.get_height():
                bgY2 = bg.get_height() * -1

            bgCount+= 1
            print("bgCount:", bgCount)

            if bgCount > 2000:
            
                finishImage.increment()

            if bgCount > 1000:

                pitStop.scroll()
                
                




    playerCar.playerBound()

    drawSprites()


    playerCar.collideBound(boundary_list, currentDirA)


    if pygame.sprite.spritecollide(playerCar, obs_list, False):
        playerCar.score -= 1
        for i in obs_list:
            if i.speedx > 0:
                playerCar.rect.x += playerCar.speed

            if i.speedx < 0:
                playerCar.rect.x -= playerCar.speed

            if i.speedy > 0:
                playerCar.rect.y += playerCar.speed

            if i.speedy < 0:
                playerCar.rect.y  -= playerCar.speed
        

    for x in obs_list:
        x.bounce(player_list)


    if playerCar.score <= -1:
        print("score is zero")
        pause = 1

    if pygame.sprite.spritecollide(playerCar, finishGroup, False):
        print("collide with finish")
        for i in range(5):
            playerCar.rect.y -= 4
            player_list.draw(screen)

        endScreenWin()



    if pygame.sprite.spritecollide(playerCar, pitGroup, True):
        playerCar.score += 30
        
        

    

    
    pygame.display.update()

                    #Number of frames per secong e.g. 60
    clock.tick(speed)

pygame.quit()
