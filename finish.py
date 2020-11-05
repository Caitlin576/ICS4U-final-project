import pygame

class Finish(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        #self.image = pygame.surface((100, 100))
        #self.image.fill((0, 0, 0))
        #self.rect = self.image.get_rect
        #self.rect.x = 100
        #self.rect.y = 100

        self.image = pygame.image.load("finishline.png")
        self.rect = self.image.get_rect()
        self.rect.x = 75
        self.rect.y = -4
        

    def increment(self):
        self.rect.y += 4

