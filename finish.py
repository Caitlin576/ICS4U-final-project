import pygame

class Finish(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("finishline.png")
        self.rect = self.image.get_rect()
        

    def appear(self, surface, time):
        if time >= 1:
            pygame.surface.blit(self)
        
