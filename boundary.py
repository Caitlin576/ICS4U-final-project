import pygame

class Boundary(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("boundary.png")
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        
