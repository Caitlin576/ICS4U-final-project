import pygame

class Car(pygame.sprite.Sprite):
        
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("purplesquare.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 4
        self.score = 100
 
    def moveRight(self):
        
        self.rect.x += self.speed
 
    def moveLeft(self):
        
        self.rect.x -= self.speed

    def moveUp(self):
        
        self.rect.y -= self.speed

    def moveDown(self):
        self.rect.y += self.speed

    def playerBound(self):
        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > 536:
            self.rect.x = 536

        if self.rect.y > 536:
            self.rect.y = 536

        if self.rect.y < 100:
            self.rect.y = 100

        if self.rect.x < 70:
            self.rect.x = 70

        if self.rect.x > 550:
            self.rect.x = 550
        
        

    def collideBound(self, spriteGroup, direct):

        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.score -= 1
            if direct == 'l':
                self.rect.left += 15
                #self.rect.top -= 5
            if direct == 'r':
                self.rect.left -= 15
                #self.rect.top -= 5

            #if direct == 'u':
             #   self.rect.top -= 15

            #if direct == 'd':
             #   self.rect.top += 15


    


    



