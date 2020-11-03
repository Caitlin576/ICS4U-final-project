import pygame
import random

class Obstacles(pygame.sprite.Sprite):

    def __init__(self, window):
        super().__init__()
        self.image = pygame.image.load("redsquare.png")
        self.rect = self.image.get_rect()
        self.speedx = random.randint(3, 7)
        self.speedy = random.randint(3, 5)
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
    
        
