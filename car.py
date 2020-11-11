import pygame

pygame.init()

pygame.mixer.music.load('GameMusic.wav')
pygame.mixer.music.play(-1)

#create a sprite class for the car
class Car(pygame.sprite.Sprite):

    
    #receive x and  y values in the initialization   
    def __init__(self, x, y):
        #initialize the sprite class
        super().__init__()
        #load the picture of the car, convert to prevent lagging
        self.pic = pygame.image.load("carImg.png").convert_alpha()
        #set the image to the picture, rotated 90 degrees
        self.image = pygame.transform.rotate(self.pic, 90 )
        #get the rectangle values (x, y, w, h) of the image
        self.rect = self.image.get_rect()
        #set the x and y coordinates of the rectangle to the values
        #passed in the initialization parameters
        self.rect.x = x
        self.rect.y = y
        #set the speed variable to 5
        self.speed = 5
        #set the score to 100 to start
        self.score = 100
        #set the sound effect to the crashing sound
        self.sound = pygame.mixer.Sound("carcrashsoundeffect.wav")

    #create functions to move right, left, up and down by the number of pixels
    #in the speed variable
    def moveRight(self):
        pygame.mixer.music.play(-1)

        self.rect.x += self.speed
 
    def moveLeft(self):

        pygame.mixer.music.play(-1)
        
        self.rect.x -= self.speed

    def moveUp(self):

        pygame.mixer.music.play(-1)
        
        self.rect.y -= self.speed

    def moveDown(self):

        pygame.mixer.music.play(-1)
        
        self.rect.y += self.speed

    #create a function to prevent the player from going off the screen or
    #outside of the racetrack boundaries. If the player comes into contact
    #with the racetrack boundaries, the crash sound effect plays and they lose
    #a point from the score
    def playerBound(self):

        pygame.mixer.music.play(-1)

        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > 536:
            self.rect.x = 536

        if self.rect.y > 536:
            self.rect.y = 536

        if self.rect.y < 100:
            self.rect.y = 100

        if self.rect.x < 70:
            pygame.mixer.Sound.play(self.sound)
            self.score -= 1
            self.rect.x = 70

        if self.rect.x > 486:
            pygame.mixer.Sound.play(self.sound)
            self.score -= 1
            self.rect.x = 486
        

    #create a function for collision detection with the sides. If the
    #player hits the sides, they bounce in the opposite direction they
    #were coming from, the crash sound effect plays, and they lose a point
    def collideBound(self, spriteGroup, direct):

        pygame.mixer.music.play(-1)

        if pygame.sprite.spritecollide(self, spriteGroup, False):
            pygame.mixer.Sound.play(self.sound)
            self.score -= 1
            if direct == 'l':
                self.rect.left += 15

            if direct == 'r':
                self.rect.left -= 15
                

    #create a function so that if the player collides with other sprites,
    #the player bounces away from the sprite (ex: if the player is further
    #right than the sprite, they bounce right)
    def playerCollision(self, spriteGroup):

        pygame.mixer.music.play(-1)
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            #upon collision, the crash sound effect plays and the score
            #decreases by one
            pygame.mixer.Sound.play(self.sound)
            self.score -= 1
            for sprite in spriteGroup:
                #hit from the right
                if sprite.rect.x < self.rect.x:
                    self.rect.x -= 3.5
                    
                #hit from the left
                if sprite.rect.x > self.rect.x: 
                    self.rect.x += 3.5
                    
                #hit from the bottom
                if sprite.rect.y > self.rect.y:
                    
                    self.rect.y -= 3.5
                #hit from the top
                if sprite.rect.y < self.rect.y:
                    self.rect.y += 3.5
