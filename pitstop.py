import pygame

pygame.init()

pygame.mixer.music.load('GameMusic.wav')
pygame.mixer.music.play(-1)

class Pitstop(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("pitstopImg.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = -100

    def scroll(self):
        self.rect.y += 4
