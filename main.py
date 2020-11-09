import pygame, random

from car import Car
from obstacles import Obstacles
from boundary import Boundary
from finish import Finish
from pitstop import Pitstop
#from text import Text
from rival import Rival
from button import Button

pygame.init()
 
GREEN = (13, 160, 21)
BLUE = (39, 188, 204)
BLACK = (0, 0, 0)
GREY = (233, 233, 233)
WHITE = (255, 255, 255)


startScore = 100
currentDirA = ''
currentDirB = ''

level = 0

bgCount = 0

#done up to here
screenw = 640 #done (4 lines)
screenh = 600 
screen = pygame.display.set_mode((screenw, screenh))
pygame.display.set_caption("Game")



player_list = pygame.sprite.Group() #done

obs_list = pygame.sprite.Group() #done

boundary_list = pygame.sprite.Group() #done

#done (4 lines)
playerStartX = 400
playerStartY = 450
playerCar = Car(playerStartX, playerStartY)
player_list.add(playerCar)


#done (3 lines)
boundLeft = Boundary(50)
boundRight = Boundary(550)
boundary_list.add(boundLeft, boundRight)

bg = pygame.image.load("roadImg.png").convert_alpha() #done


#done (3 lines)
scoreFont = pygame.font.SysFont('Courier', 20)
menuFont = pygame.font.SysFont('Courier', 40)
countFont = pygame.font.SysFont('Arial', 200)

#done (5 lines)
easyButton = Button(250, 250, 150, 50, menuFont, GREY, WHITE)
hardButton = Button(250, 350, 150, 50, menuFont,  GREY, WHITE)
instructionsButton = Button(175, 450, 300, 50, menuFont, GREY, WHITE)
buttonGroup = pygame.sprite.Group()
buttonGroup.add(easyButton, hardButton, instructionsButton)

finishLineVisible = False #probably not needed

#done(5 lines)
finishY = -4
finishImage = Finish()
finishGroup = pygame.sprite.Group()
finishGroup.add(finishImage)
finishAppear = 2000

#done(3 lines)
pitStop = Pitstop()
pitGroup = pygame.sprite.Group()
pitGroup.add(pitStop)

#done (5 lines)
rivalStartX = 150
rivalStartY = 450
rivalCar = Rival(rivalStartX, rivalStartY)
rival_list = pygame.sprite.Group()
rival_list.add(rivalCar)

startGame = False

countdownComplete = False

#done up to here



def drawSprites():
    global FinishLineVisible 

    screen.fill(GREEN)

    screen.blit(bg, (50, bgY))
    screen.blit(bg, (50, bgY2))
    #player_list.update()

    rival_list.draw(screen)

    
    text = scoreFont.render(str(playerCar.score), 1, (0, 0, 0))
    screen.blit(text, (570, 10))

    if bgCount > finishAppear:
        print("finsh drawn")
        finishGroup.draw(screen)
    
    boundary_list.draw(screen)

    


    if bgCount > 1000:
        pitGroup.draw(screen)
            
    player_list.draw(screen)
    obs_list.update()
    obs_list.draw(screen)

def instructions():

    running = True
    
    while running:
        #pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #print("end instructions")
                startScreen()
                running = False

    
        screen.fill(GREEN)

        backstory = menuFont.render("(Backstory)", 1, (0, 0, 0))

        screen.blit(backstory, (screenw/2 - backstory.get_width()/2, 200))

        pygame.display.update()



def startScreen():

    global level, startGame

    #startGame = True

    while startGame == False:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                startGame = True
                pygame.quit()

        screen.fill(BLUE)
        title = menuFont.render("(Title)", 1, BLACK)
        screen.blit(title, (screenw/2 - title.get_width()/2, 150))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if easyButton.rect.x + easyButton.w > mouse[0] > easyButton.rect.x and easyButton.rect.y + easyButton.h > mouse[1] > easyButton.rect.y:
            easyButton.hover()
            if click[0] == 1:
                print("click")
                level = 1
                startGame = True
                print("startGame:", startGame)

        else:
            easyButton.regular()

        if hardButton.rect.x + hardButton.w > mouse[0] > hardButton.rect.x and hardButton.rect.y + hardButton.h > mouse[1] >hardButton.rect.y:
            hardButton.hover()
            if click[0] == 1:
                level = 3
                startGame = True
            
        else:
            hardButton.regular()

        if instructionsButton.rect.x + instructionsButton.w > mouse[0] > instructionsButton.rect.x and instructionsButton.rect.y + instructionsButton.h > mouse[1] >instructionsButton.rect.y:
            instructionsButton.hover()
            if click[0] == 1:
                #print("instructions clicked")
                instructions()
        else:
            instructionsButton.regular()

        buttonGroup.draw(screen)

        easyText = menuFont.render("Easy", 1, BLACK)
        easyTextRect = easyText.get_rect()
        easyTextRect.center = ((easyButton.rect.x + (easyButton.w/2)), (easyButton.rect.y + (easyButton.h/2)) )
        screen.blit(easyText, easyTextRect)

        hardText = menuFont.render("Hard", 1, BLACK)
        hardTextRect = hardText.get_rect()
        hardTextRect.center = ((hardButton.rect.x + (hardButton.w/2)), (hardButton.rect.y + (hardButton.h/2)) )
        screen.blit(hardText, hardTextRect)

        instructionsText = menuFont.render("Instructions", 1, BLACK)
        instructionsTextRect = instructionsText.get_rect()
        instructionsTextRect.center = ((instructionsButton.rect.x + (instructionsButton.w/2)), (instructionsButton.rect.y + (instructionsButton.h/2)) )
        screen.blit(instructionsText, instructionsTextRect)

        pygame.display.update()

def countdown():

    global countdownComplete

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

        three = countFont.render("3", 1, BLACK)
        two = countFont.render("2", 1, BLACK)
        one = countFont.render("1", 1, BLACK)
        go = countFont.render("GO", 1, BLACK)

        def displayNumber(x):
            drawSprites()
            screen.blit(x, (screenw/2 - x.get_width()/2, 250))
            pygame.display.update()
            pygame.time.delay(1000)

        displayNumber(three)

        displayNumber(two)

        displayNumber(one)

        displayNumber(go)
            

        

        

        drawSprites()
        pygame.display.update()

        countdownComplete = True

        running = False


def endScreenLoss():
    global pause, bgCount, obstaclesCreated, countdownComplete
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
                running = False

        playerCar.rect.x = playerStartX
        playerCar.rect.y = playerStartY

        rivalCar.rect.x = rivalStartX
        rivalCar.rect.y = rivalStartY

        for ob in obs_list:
            ob.kill()

        countdownComplete = False

        finishImage.rect.y = -30
        screen.fill(BLUE)
        gameOver = menuFont.render("Game Over!", 1, (0, 0, 0))
        screen.blit(gameOver, (screenw/2 - gameOver.get_width()/2, 200))
        playAgain = menuFont.render("Click to play again", 1, (0, 0, 0))
        screen.blit(playAgain, (screenw/2 - playAgain.get_width()/2, 300))
        playerCar.score = startScore
        obstaclesCreated = False
        pygame.display.update()

def endScreenWin():
    global pause, bgCount, obstaclesCreated
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
    
                running = False

        print("score:", playerCar.score)

        playerCar.rect.x = playerStartX
        playerCar.rect.y = playerStartY
        playerCar.score = startScore

        rivalCar.rect.x = rivalStartX
        rivalCar.rect.y = rivalStartY

        for ob in obs_list:
            ob.kill()

        finishImage.rect.y = -10
        screen.fill(BLUE)
        yourScore = menuFont.render("Your score:", 1, BLACK)
        screen.blit(yourScore, (screenw/2 - yourScore.get_width()/2, 200))
        playAgain = menuFont.render("Click to play again", 1, (0, 0, 0))
        screen.blit(playAgain, (screenw/2 - playAgain.get_width()/2, 300))

        
        obstaclesCreated = False

        #newScore = menuFont.render("New score:", 1, BLACK)
        #screen.blit(newScore, (screenw/2 - newScore.get_width()/2, 350))

        

        pygame.display.update()
  

bgY = 0 #done
bgY2 = bg.get_height() #done

pause = 0 #done
speed = 60 #done

obstaclesCreated = False #done

running = True #done
clock=pygame.time.Clock() #done
 
while running:

    print("startGame 1:", startGame)

    while startGame == False:
        
        startScreen()
        print("startGame in main loop:", startGame)

    if obstaclesCreated == False:
        for i in range(level):
            obst = Obstacles(screen)
            obst.rect.x = random.randrange(screenw - 64)
            obst.rect.y = random.randrange(screenh - 64)
            obs_list.add(obst)

        obstaclesCreated = True

    if countdownComplete == False:
        countdown()
        #countdownComplete = True
        print("countdown complete:", countdownComplete)

    

    if pause > 0:
        print("pause greater than zero")
        pause += 1
        print("pause", pause)
        if pause == 2:
            print("pause == 2")
            pygame.time.delay(600)
            endScreenLoss()

    #if pygame.sprite.spritecollide(rivalCar, finishGroup, False):
        #endScreenLoss()
        
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

        rivalCar.rect.y += 1

        if playerCar.rect.y > 350:
            playerCar.moveUp()

        else:

            bgY += 10
            bgY2 += 10

            if bgY > bg.get_height():
                bgY = -600


            if bgY2 > bg.get_height():
                bgY2 = -600

            bgCount+= 1
            print("bgCount:", bgCount)

            if bgCount > finishAppear:
                
                finishImage.increment()

            if bgCount > 750:

                pitStop.scroll()

    else:
        rivalCar.rect.y -= rivalCar.speedy
                    
                    

    playerCar.playerBound()

    drawSprites()

    rivalCar.rivalCollision(obs_list)

    print("rival speed:", rivalCar.speedy)

    rivalCar.rivalCollision(player_list)
    playerCar.playerCollision(rival_list)

    rivalCar.rivalBound()



    playerCar.collideBound(boundary_list, currentDirA)

    if pygame.sprite.spritecollide(playerCar, rival_list, False):
        

        print("collision")
                                   
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

    for i in obs_list:
        i.bounce(rival_list)


    if playerCar.score <= 0:
        print("score is zero")
        pause = 1

   

    if pygame.sprite.spritecollide(playerCar, finishGroup, False):

        print("finish x:", finishImage.rect.x)
        print("finish y:", finishImage.rect.y)
        print("car x:", playerCar.rect.x)
        print("car y:", playerCar.rect.y)
        print("collide with finish")
        for i in range(5):
            playerCar.rect.y -= 4
            player_list.draw(screen)

        endScreenWin()

    if pygame.sprite.spritecollide(playerCar, pitGroup, True):
        playerCar.score += 30

    if pygame.sprite.spritecollide(rivalCar, pitGroup, True):
        pitStop.kill()
            

    pygame.display.update()

                        
    clock.tick(speed)

pygame.quit()


