  
import pygame

pygame.init()

pygame.mixer.music.load('GameMusic.wav')
pygame.mixer.music.play(-1)

#create a sprite class for the finish line
class Finish(pygame.sprite.Sprite):

    def __init__(self):
        #initialize the sprite class
        super().__init__()
        #load the image of the finish line and convert it to prevent
        #lagging
        self.image = pygame.image.load("finishImg.png").convert_alpha()
        #get the rectangle values (x, y, w, h) of the image
        self.rect = self.image.get_rect()
        #set the x and y coordinates of the finish line so that it begins
        #off the screen
        self.rect.x = 70
        self.rect.y = -200
        
    #create a function to move the finish line down the screen
    def increment(self):
        self.rect.y += 4
