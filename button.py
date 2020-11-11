import pygame

pygame.init()

pygame.mixer.music.load('GameMusic.wav')
pygame.mixer.music.play(-1)

#create sprite class for the buttons
class Button(pygame.sprite.Sprite):

    #take x, y, width, height, and colour values during initialization
    def __init__(self, x, y, w, h, colour1, colour2):
        #initialize sprite class
        super().__init__()
        #set the w and h values to the w and h parameter values
        self.w = w
        self.h = h
        #set the image to a rectangle the size of the w and h values
        self.image = pygame.Surface((w, h))
        #get the rectangle values (x, y, w, h) of the image
        self.rect = self.image.get_rect()
        #set the x and y values to the x and y parameter values
        self.rect.x = x
        self.rect.y = y
        #set a default colour for the button and a colour for when the
        #mouse is hovering over the button
        self.defaultColour = colour1
        self.hoverColour = colour2
      
    #create a function to set the colour of the button to the
    #default colour
    def regular(self):
        self.image.fill(self.defaultColour)

    #create a function to set the colour of the button to the
    #hovering colour
    def hover(self):
        self.image.fill(self.hoverColour)
