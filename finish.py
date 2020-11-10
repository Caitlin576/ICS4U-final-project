  
import pygame

pygame.init()

pygame.mixer.music.load('GameMusic.wav')
pygame.mixer.music.play(-1)

class Finish(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("finishImg.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = -200
        

    def increment(self):
        self.rect.y += 4
