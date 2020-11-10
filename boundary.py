import pygame

pygame.init()
pygame.mixer.music.load('GameMusic.wav')
pygame.mixer.music.play(-1)

class Boundary(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = pygame.image.load("boundary.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0
