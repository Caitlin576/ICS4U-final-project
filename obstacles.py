import pygame
import random

pygame.init()

pygame.mixer.music.load('GameMusic.wav')
pygame.mixer.music.play(-1)

class Obstacles(pygame.sprite.Sprite):

    pygame.mixer.music.load('GameMusic.wav')
    pygame.mixer.music.play(-1)

    def __init__(self, window):
        super().__init__()
        self.image = pygame.image.load("obstacleImg.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.speedx = random.randint(3, 9)
        self.speedy = random.randint(4, 7)
        self.window = window

    def update(self):
        self.rect.left += self.speedx
        self.rect.top += self.speedy
        if self.rect.right > self.window.get_width() or self.rect.left < 0:
            self.speedx = -self.speedx
        if self.rect.bottom > self.window.get_height() or self.rect.top < 0:
            self.speedy = -self.speedy

    def bounce(self, spriteGroup):

    
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.speedx = -self.speedx
            self.speedy = -self.speedy

    def obsBound(self, w, h):
        if self.rect.x > w:
            self.rect.x = w
            self.rect.x -= 2

        if self.rect.x < 0:
            self.rect.x = 0
            self.rect.x += 2

        if self.rect.y > h:
            self.rect.y = h
            self.rect.y -= 2
