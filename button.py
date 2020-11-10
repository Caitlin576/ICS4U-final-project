import pygame

pygame.init()

pygame.mixer.music.load('GameMusic.wav')
pygame.mixer.music.play(-1)

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, w, h, colour1, colour2):
        super().__init__()
        self.w = w
        self.h = h
        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.font = font
        #self.text = text
        self.defaultColour = colour1
        self.hoverColour = colour2
      

    def regular(self):
        self.image.fill(self.defaultColour)


    def hover(self):
        self.image.fill(self.hoverColour)
