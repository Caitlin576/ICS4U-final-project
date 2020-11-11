import pygame

pygame.init()
pygame.mixer.music.load('GameMusic.wav')
pygame.mixer.music.play(-1)

#create sprite class boundary
class Boundary(pygame.sprite.Sprite):
    #take x coordinate as parameter for the boundary class
    def __init__(self, x):
        #initialize the sprite class
        super().__init__()
        #set the image and convert it to prevent lagging,
        self.image = pygame.image.load("boundary.png").convert_alpha()
        #get the rectangle values (x, y, w, h) of the image 
        self.rect = self.image.get_rect()
        #set the object's x coordinate to the x argument passed and the y
        #coordinate to zero (top of the screen)
        self.rect.x = x
        self.rect.y = 0
