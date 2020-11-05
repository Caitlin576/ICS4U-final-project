import pygame

class Pitstop(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("pitstop.png")
        self.rect = self.image.get_rect()
        self.rect.x = 70
        self.rect.y = -10

    def scroll(self):
        self.rect.y += 4
