import pygame

pygame.init()

pygame.mixer.music.load('GameMusic.wav')
pygame.mixer.music.play(-1)

#create a sprite class for the pitstop
class Pitstop(pygame.sprite.Sprite):

    def __init__(self):
        #initialize the sprite class
        super().__init__()
        #load the image of the pitstop and convert it to prevent
        #lagging
        self.image = pygame.image.load("pitstopImg.png").convert_alpha()
        #get the rectangle values of the image (x, y, w, h)
        self.rect = self.image.get_rect()
        #set the x and y coordinates so that the pitstop starts of the screen
        self.rect.x = 70
        self.rect.y = -100

    #create function to move the pitstop down the screen
    def scroll(self):
        self.rect.y += 4
