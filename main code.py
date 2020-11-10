import pygame, random #import pygame and random libraries

import car
import obstacles
import boundary
import finish
import rival
import button

#import classes and functions created in other modules 
from car import Car
from obstacles import Obstacles
from boundary import Boundary
from finish import Finish
from pitstop import Pitstop
from rival import Rival
from button import Button
from printInstructions import printInstruct

#initialize pygame
pygame.init()

#declare variables to use as the width and height of the screen
screenw = 640
screenh = 600
#create a display using the screenw and screenh variables
screen = pygame.display.set_mode((screenw, screenh))

#set the caption and icon of the game
pygame.display.set_caption("Turbo!")
icon = pygame.image.load("carImg.png")
pygame.display.set_icon(icon)

#declare rgb values for colour constants to be used in the game
GREEN = (13, 160, 21)
BLUE = (39, 188, 204)
BLACK = (0, 0, 0)
GREY = (233, 233, 233)
WHITE = (255, 255, 255)

winSound = pygame.mixer.Sound("youwin.wav")
loseSound = pygame.mixer.Sound("youlose.wav")
#zoomSound = pygame.mixer.Sound("zoom.m4a")

#declare fonts to use later when displaying text
smallFont = pygame.font.SysFont('Courier', 20) #formerly score, menu, count
largeFont = pygame.font.SysFont('Courier', 40)
arialFont = pygame.font.SysFont('Arial', 200)


#create an object for the player's character, assign its
#starting position to 400, 450
playerStartX = 400
playerStartY = 450
playerCar = Car(playerStartX, playerStartY)
#create a sprite group to hold the playerCar object, add playerCar
#to the group (useful for collision detection later on)
playerGroup = pygame.sprite.Group()
playerGroup.add(playerCar)


#create an object for the opponent's character (this character is automated),
#assign its starting position to 150, 450
rivalStartX = 150
rivalStartY = 450
rivalCar = Rival(rivalStartX, rivalStartY)
#create a sprite group to hold the rivalCar object, add rivalCar
#to the group (useful for collision detection later on)
rivalGroup = pygame.sprite.Group()
rivalGroup.add(rivalCar)


#create two objects for the racetrack boundaries (one left, one right),
#assign them x positions of 50 (left) and 550 (right), both have y positions
#of zero
boundLeft = Boundary(50)
boundRight = Boundary(550)
#create a sprite group to hold the boundary objects, add both boundaries to
#the group (useful for collision detection)
boundaryGroup = pygame.sprite.Group()
boundaryGroup.add(boundLeft, boundRight)


#create an object of the finish class (in seperate module) to serve as
#the finish line
finishLine = Finish()
#Create a sprite group to hold the finishLine object, add finishLine to
#the group (useful for detecting when the player has crossed the finish line)
finishGroup = pygame.sprite.Group()
finishGroup.add(finishLine)
#create a variable finishY to hold the starting y position of finishLine
finishY = -200
finishYstart = -200
#create a variable finishAppear to use later to check whether the player
#has travelled far enough to reach the finish line
finishAppear = 1500




#create a sprite group to hold the pitStop, add pitStop to the group
#(used for collision detection)
pitGroup = pygame.sprite.Group()
#create a variable to use to check whether or not to display the pitstop on the screen
pitAppear = 750


#create objects of the Button class, assign them x and y positions, width and height,
#and two colours (one for when the button is selected, one for when it isn't)
easyButton = Button(250, 250, 150, 50, GREY, WHITE)
hardButton = Button(250, 350, 150, 50, GREY, WHITE)
instructionsButton = Button(175, 450, 300, 50, GREY, WHITE)
#create a sprite group to hold the buttons, add the three button objects to the group
#(useful for drawing them to the screen all together in a single line of code)
buttonGroup = pygame.sprite.Group()
buttonGroup.add(easyButton, hardButton, instructionsButton)


#create a sprite group to hold the obstacles (the group is empty for now because
#obstacles will be added later, since the number of obstacles depends on the level
#the user selects)
obsGroup = pygame.sprite.Group()


#load an image to use as the racetrack, convert_alpha() to prevent lagging
bg = pygame.image.load("roadImg.png").convert_alpha()
#create variables bgY and bgY2 to hold the y positions of the backgroud image (which will be displayed
#twice to allow for a scrolling background, the first image is dsiplayed at zero, the second is
#displayed at the bottom of the first image)
bgY = 0
bgY2 = bg.get_height()


#create variables to record the current direction of the car (used for
#collision detection)
currentDirA = ''
currentDirB = ''


#create variables to reset the game at for when the user wants to play again
startScore = 100 #set the starting score to 100
level = 0 #set the level (number of obstacles) to 0, to be changed when the user selects a level
bgCount = 0 #this variable records the 'distance' that the user has scrolled, so that the finish
#line can appear when they make it far enough


#create booleans to determine which methods to execute/ when to end the game
startGame = False
countdownComplete = False
obstaclesCreated = False
pitCreated = False
pause = 0

#a clock is created to control frames per second, and a speed variable is created to be
#used in the clock
speed = 60
clock = pygame.time.Clock()


#strings containing each line of the intriduction screen
instructionString1 = "This is your first race following the biggest crash"
instructionString2 = "of your racing career. In order to prove that"
instructionString3 = "you're still the best racecar driver, you need to"
instructionString4 = "win this next race against your arch enemy."
instructionString5 = "Press the right, left, up, and down arrows to move"
instructionString6 = "in those directions. Avoid hiting the obstacles and"
instructionString7 = "the sides of the racetrack, and make it to the"
instructionString8 = "finish line before your opponent to win. Stop at the"
instructionString9 = " pitstop (the pile of tires) to pick up extra"
instructionString10 = "points. If you bump into too many objects"
instructionString11 = "before you reach the finish line, the game"
instructionString12 = "will end. Click anywhere to return to the main menu."




#create a function to draw the various sprite groups and background onto the
#screen (to be used in the main code)
def drawSprites(): 

    #fill the screen with the colour green (declared earlier)
    screen.fill(GREEN)

    #display the background images at x = 50 and their y position variable
    #which changes as the user scrolls
    screen.blit(bg, (50, bgY))
    screen.blit(bg, (50, bgY2))

    #create a variable to hold the text for the player's score and display it
    #in the top right corner
    scoreWord = smallFont.render("Score:", 1, BLACK)
    scoreNum = smallFont.render(str(playerCar.score), 1, BLACK)
    screen.blit(scoreWord,(570, 10))
    screen.blit(scoreNum, (570, 29))

    #if the user has scrolled farther than the finishAppear variable value, the
    #finish line appears on the screen (bgCount increments as the user moves their
    #car forward)
    if bgCount > finishAppear:
        finishGroup.draw(screen)

    #draw the boundaries in the boundary group onto the screen
    boundaryGroup.draw(screen)

    #if the user has scrolled farther than the pitAppear variable value, the
    #pitstop appears on the screen (bgCount increments as the user moves their
    #car forward)
    if bgCount > pitAppear:
        pitGroup.draw(screen)

    #draws the object in the playerGroup onto the screen
    playerGroup.draw(screen)

    #draw the opponent's car onto the screen
    rivalGroup.draw(screen)
    
    #call the update method on the obstacles in obsGroup (method is in the obstacles
    #module) and draws the obstacles onto the screen
    obsGroup.update()
    obsGroup.draw(screen)



#create function to display the instructions/story of the game to the user
def instructions():

    running = True

    #running (local variable) starts as true, while the function is running, pygame
    #gets events. If the user presses the quit button, the program shuts down, running
    #is false, if they click the mouse button, they are returned to the main menu, running
    #is false
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                startScreen()
                running = False

        #the screen is filled green
        screen.fill(GREEN)

        printInstruct(instructionString1, 20, smallFont, BLACK, screen)
        printInstruct(instructionString2, 60, smallFont, BLACK, screen)
        printInstruct(instructionString3, 100, smallFont, BLACK, screen)
        printInstruct(instructionString4, 140, smallFont, BLACK, screen)
        printInstruct(instructionString5, 180, smallFont, BLACK, screen)
        printInstruct(instructionString6, 220, smallFont, BLACK, screen)
        printInstruct(instructionString7, 260, smallFont, BLACK, screen)
        printInstruct(instructionString8, 300, smallFont, BLACK, screen)
        printInstruct(instructionString9, 340, smallFont, BLACK, screen)
        printInstruct(instructionString10, 380, smallFont, BLACK, screen)
        printInstruct(instructionString11, 420, smallFont, BLACK, screen)
        printInstruct(instructionString12, 460, smallFont, BLACK, screen)

        #the display is updated
        pygame.display.update()


#define a function to display the main menu
def startScreen():

    #define the scope for level and startGame as global so they can be changed in the function
    #and their values can be saved for use outside of the function
    global level, startGame

    #while startGame is False (the user has not indicated that they would like to start the
    #game), get the events. If the quit button is pressed, startGame is true so the function stops
    #running and and the game quits.
    while startGame == False:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                startGame = True
                pygame.quit()

        #fill the screen blue
        screen.fill(BLUE)

        #create a variable to render the text for the title of the game, display it on the screen
        #To center it, the x variable is set to half the width of the screen, minus half the width
        #of the text. The y value is set to 200
        title = largeFont.render("Turbo!", 1, BLACK)
        screen.blit(title, (screenw/2 - title.get_width()/2, 150))

        #create a varible to get the position of the mouse and a variable to check if the mouse has
        #been clicked. 
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        
        #if the position of the mouse is within the same position as the easy button, the hover() method
        #(from the button class) is executed (the button lights up). If the left mouse button is
        #clicked, the level is set to one so that 1 obstacles is created, and startGame becomes
        #True, so the function exits and the game begins on the easy level
        if easyButton.rect.x + easyButton.w > mouse[0] > easyButton.rect.x and easyButton.rect.y + easyButton.h > mouse[1] > easyButton.rect.y:
            easyButton.hover()
            if click[0] == 1:
                level = 1
                startGame = True

        #if the mouse is not hovering over the Easy button, the button remains the same
        else:
            easyButton.regular()

        #the Hard button works on the same principle as the easy button, but the level is set to three
        #and three obstacles are created instead when the game begins

        if hardButton.rect.x + hardButton.w > mouse[0] > hardButton.rect.x and hardButton.rect.y + hardButton.h > mouse[1] >hardButton.rect.y:
            hardButton.hover()
            if click[0] == 1:
                level = 3
                startGame = True    
        else:
            hardButton.regular()

        #the instructions button works on the same principle as the other button, but then it is pressed,
        #the instructions function is executed (the game does not start in this case)

        if instructionsButton.rect.x + instructionsButton.w > mouse[0] > instructionsButton.rect.x and instructionsButton.rect.y + instructionsButton.h > mouse[1] >instructionsButton.rect.y:
            instructionsButton.hover()
            if click[0] == 1:
                instructions()
        else:
            instructionsButton.regular()

        #the group containing the buttons is drawn to the screen
        buttonGroup.draw(screen)

        #text is displayed and centered on the buttons (same principle used to center text on the
        #screen, but the center of the text is set to the center of the button rectangle)
        easyText = largeFont.render("Easy", 1, BLACK)
        easyTextRect = easyText.get_rect()
        easyTextRect.center = ((easyButton.rect.x + (easyButton.w/2)), (easyButton.rect.y + (easyButton.h/2)) )
        screen.blit(easyText, easyTextRect)

        hardText = largeFont.render("Hard", 1, BLACK)
        hardTextRect = hardText.get_rect()
        hardTextRect.center = ((hardButton.rect.x + (hardButton.w/2)), (hardButton.rect.y + (hardButton.h/2)) )
        screen.blit(hardText, hardTextRect)

        instructionsText = largeFont.render("Instructions", 1, BLACK)
        instructionsTextRect = instructionsText.get_rect()
        instructionsTextRect.center = ((instructionsButton.rect.x + (instructionsButton.w/2)), (instructionsButton.rect.y + (instructionsButton.h/2)) )
        screen.blit(instructionsText, instructionsTextRect)

        #the display is updated
        pygame.display.update()


#define a function for a countdown at the beginning of the game
def countdown():

    #define the scope for countdownComplete as global so it can be changed in the function
    #and the value can be saved for use outside of the function
    global countdownComplete

    #local variable running is true
    running = True

    #while runnning is True, if the user presses the quit button, the game exits
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

        #create variables to render text for the numbers in the countdown and the
        #word go
        three = arialFont.render("3", 1, BLACK)
        two = arialFont.render("2", 1, BLACK)
        one = arialFont.render("1", 1, BLACK)
        go = arialFont.render("GO", 1, BLACK)
        
        #define a function to display the numbers of the countdown on the
        #screen with one second between each one
        def displayNumber(x):
            drawSprites()
            screen.blit(x, (screenw/2 - x.get_width()/2, 250))
            pygame.display.update()
            pygame.time.delay(1000)

        #call the function for each item in the countdown
        displayNumber(three)

        displayNumber(two)

        displayNumber(one)

        displayNumber(go)

        #draw the sprites over the countdown and update the display
        drawSprites()
        pygame.display.update()

        #set countdownComplete to True so that the countdown doesn't repeat again
        countdownComplete = True

        #running is false so that the function exits
        running = False

        playMusic()

#define a function for the end screen when the user has lost the game
def endScreenLoss():
    #define the scope for pause, obstaclesCreated, and countdownComplete as global so
    #they can be changed in the function and their values can be saved for use outside
    #of the function
    global pause, bgCount, countdownComplete, obstaclesCreated, startGame, pitCreated

    #reset bgCount, pause, the player and rival start positions, the player's score, countdown
    #complete, obstaclesCreated and the finish line's y coordinate to the way they were at
    #the beginnning so the user can play again.  
    bgCount = 0
    pause = 0

    playerCar.rect.x = playerStartX
    playerCar.rect.y = playerStartY
    playerCar.score = startScore

    rivalCar.rect.x = rivalStartX
    rivalCar.rect.y = rivalStartY

    obstaclesCreated = False
    countdownComplete = False
    startGame = False
    pitCreated = False

    finishLine.rect.y = finishYstart

    for ob in obsGroup:
            ob.kill()

    #pitGroup.add(pitStop)

    #while running, if the user clicks the quit button, the game exits, running is
    #false. If they click the screen, running is false, the function exits, and the
    #game starts again. A slight delay prevents them from clicking too fast

    pygame.mixer.Sound.play(loseSound)
    running = True
    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                startScreen()
                running = False

        #The screen is filled blue, game over is displayed, and a message to play
        #again is displayed. The display is updated

        #
        screen.fill(BLUE)
        gameOver = largeFont.render("Game Over!", 1, (0, 0, 0))
        screen.blit(gameOver, (screenw/2 - gameOver.get_width()/2, 200))
        playAgain = largeFont.render("Click to play again", 1, (0, 0, 0))
        screen.blit(playAgain, (screenw/2 - playAgain.get_width()/2, 300))
        
        pygame.display.update()



def endScreenWin():

    #define the scope for pause, obstaclesCreated and countdownComplete as global so
    #they can be changed in the function and their values can be saved for use outside
    #of the function
    
    global pause, bgCount, countdownComplete, obstaclesCreated, endScore, startGame, pitCreated

    #reset bgCount, pause, the player and rival start positions, the player's score, countdown
    #complete, obstaclesCreated and the finish line's y coordinate to the way they were at
    #the beginnning so the user can play again.
    bgCount = 0
    pause = 0
    countdownComplete = False
    obstaclesCreated = False
    startGame = False
    pitCreated = False
    
    playerCar.rect.x = playerStartX
    playerCar.rect.y = playerStartY
    playerCar.score = startScore

    rivalCar.rect.x = rivalStartX
    rivalCar.rect.y = rivalStartY

    finishLine.rect.y = finishYstart

    for ob in obsGroup:
        ob.kill()

    

    finalScore = "Your score: " + str(endScore)

    #while running (local variable), if the user clicks the quit button, the game
    #exits, running is false. If they click the screen, running is false, the
    #function exits, and the game starts again. A slight delay prevents them from
    #clicking too fast

    pygame.mixer.Sound.play(winSound)
    
    running = True

    while running:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                startScreen()
                running = False

        

        #The screen is filled blue, the score is displayed, and a message to play
        #again is displayed. The display is updated
        #
        screen.fill(BLUE)
        yourScore = largeFont.render(finalScore, 1, BLACK)
        screen.blit(yourScore, (screenw/2 - yourScore.get_width()/2, 200))
        playAgain = largeFont.render("Click to play again", 1, (0, 0, 0))
        screen.blit(playAgain, (screenw/2 - playAgain.get_width()/2, 300))

        pygame.display.update()

pygame.mixer.music.load('GameMusic.wav')

def playMusic():
    #print("in playMusic")
    pygame.mixer.music.play(-1)
    
 
#set running to true
running = True

playMusic()



#main game loop is executed as long as running is True
while running:

    print("playing music")
    #playMusic()

    #while the user has not performed an action indicating they want to start the game,
    #startGame is false and the startScreen function is executed. 
    while startGame == False:
        startScreen()

    #if the obstacles have not been created, a certain number of obstacles is created depending
    #on the level the user selected. Each obstacle is added to the obstacle group
    if obstaclesCreated == False:
        for i in range(level):
            obst = Obstacles(screen)
            obst.rect.x = random.randrange(screenw - 64)
            obst.rect.y = random.randrange(screenh - 64)
            obsGroup.add(obst)

        #once all the obstacles are created, obstaclesCreated is set to true so that
        #this loop does not get repeated 
        obstaclesCreated = True

    if pitCreated == False:
        pitStop = Pitstop()
        pitGroup.add(pitStop)
        pitCreated = True

    

    #if the countdown has not happened (the user has just started the game),
    #the countdown function executes and the countdown complete variable is
    #set to true within the function so that it doesn't get repeated
    if countdownComplete == False:
        countdown()

    #if the pause variable is greater than zero, the game ends  
    if pause > 0:
        endScreenLoss()
        #pause += 1
        #if pause == 2:
            #pygame.time.delay(600)
            #endScreenLoss()

    #if pygame.sprite.spritecollide(rivalCar, finishGroup, False):
        #endScreenLoss()
        
    for event in pygame.event.get():
        playMusic()
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
                
                finishLine.increment()
                print("finish line incremented")

            if bgCount > pitAppear:

                pitStop.scroll()

    else:
        rivalCar.rect.y -= rivalCar.speedy               

    playerCar.playerBound()

    drawSprites()

    rivalCar.rivalCollision(obsGroup)

    rivalCar.rivalCollision(playerGroup)
    
    playerCar.playerCollision(rivalGroup)

    rivalCar.rivalBound()

    playerCar.collideBound(boundaryGroup, currentDirA)

    #if pygame.sprite.spritecollide(playerCar, rivalGroup, False):
        
        
     
                                   
    if pygame.sprite.spritecollide(playerCar, obsGroup, False):
        pygame.mixer.Sound.play(playerCar.sound)

        playerCar.score -= 1

        for i in obsGroup:
            if i.speedx > 0:
                playerCar.rect.x += playerCar.speed

            if i.speedx < 0:
                playerCar.rect.x -= playerCar.speed

            if i.speedy > 0:
                playerCar.rect.y += playerCar.speed

            if i.speedy < 0:
                playerCar.rect.y  -= playerCar.speed
      

    for x in obsGroup:
        x.bounce(playerGroup)

    for i in obsGroup:
        i.bounce(rivalGroup)

    for j in obsGroup:
        j.obsBound(screenw, screenh)


    if playerCar.score <= 0:
        pause = 1


    if playerCar.rect.y <= finishLine.rect.y - 50:
        
        endScore = playerCar.score

        endScreenWin()

    if pygame.sprite.spritecollide(playerCar, pitGroup, True):
        playerCar.score += 30

    if pygame.sprite.spritecollide(rivalCar, pitGroup, True):
        pitStop.kill()

    #if pygame.sprite.spritecollide(rivalCar, finishGroup, False):

    if rivalCar.rect.y <= finishLine.rect.y - 50:
        print("rival collided with finish")
        print("finish y:", finishLine.rect.y)
        endScreenLoss()
            

    pygame.display.update()

                        
    clock.tick(speed)

pygame.quit()
