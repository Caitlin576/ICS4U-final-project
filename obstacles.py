import pygame
import random

pygame.init()

pygame.mixer.music.load('GameMusic.wav')
pygame.mixer.music.play(-1)


#create a sprite class for obstacles
class Obstacles(pygame.sprite.Sprite):

    pygame.mixer.music.load('GameMusic.wav')
    pygame.mixer.music.play(-1)

    #include a window (surface) in the parameters for initialization
    def __init__(self, window):
        #initialize the sprite class
        super().__init__()
        #load the image of the obstacles and convert it to prevent lagging
        self.image = pygame.image.load("obstacleImg.png").convert_alpha()
        #get the rectangle values (x, y, w, h) of the image 
        self.rect = self.image.get_rect()
        #set the speed in the x and y directions to a random number between
        #two specified numbers. 
        self.speedx = random.randint(3, 9)
        self.speedy = random.randint(4, 7)
        #set the window to the parameter passed in the __init__ function
        self.window = window

    #set the built in update function (from the sprite class) to move the
    #obstacles by their x and y speeds each time the function is called.  
    def update(self):
        self.rect.left += self.speedx
        self.rect.top += self.speedy
        #if the obstacle reaches the boundary of the window, the speed is negated
        #so that it will bounce and keep going in the opposite direction
        if self.rect.right > self.window.get_width() or self.rect.left < 0:
            self.speedx = -self.speedx
        #same for vertical boundary and y speed
        if self.rect.bottom > self.window.get_height() or self.rect.top < 0:
            self.speedy = -self.speedy

    #create a function to make the obstacle bounce (reverse directions) if
    #it comes into contact with a sprite in a given sprite group

    def bounce(self, spriteGroup):

        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.speedx = -self.speedx
            self.speedy = -self.speedy

    #create a function to keep the obstacles within the boundaries of the screen

    def obsBound(self, w, h):
        if self.rect.x > w:
            self.rect.x = w
            self.rect.x -= 2

        if self.rect.x < 0:
            self.rect.x = 0
            self.rect.x += 2

        if self.rect.y > h:
            self.rect.y = h
            self.rect.y -= 2
