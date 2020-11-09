
import pygame

class Background(pygame.sprite.Sprite):

    def __init__(self, y):
        super().__init__()
        self.image = pygame.image.load("road.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.move = 1.4
        self.rect.x = 150
        self.rect.y = y
