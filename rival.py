import pygame

class Rival(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image.load('purplesquare.png')
        self.rect = self.image.get_rect()
        self.speed = 3.5
        self.rect.x = x
        self.rect.y = y

    def moveRival(self):
        self.rect.y += self.speed

        
