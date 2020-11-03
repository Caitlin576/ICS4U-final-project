import pygame

class Boundary(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load("boundary.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0

        
