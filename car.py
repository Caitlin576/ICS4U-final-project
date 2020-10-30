import pygame

class Car(pygame.sprite.Sprite):
        
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("purplesquare.png").convert_alpha()
        self.rect = self.image.get_rect()
        
 
    def moveRight(self, pixels):
        self.rect.x += pixels
 
    def moveLeft(self, pixels):
        self.rect.x -= pixels
