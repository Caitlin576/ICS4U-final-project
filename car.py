import pygame

class Car(pygame.sprite.Sprite):
        
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("purplesquare.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 4
 
    def moveRight(self):
        
        self.rect.x += self.speed
 
    def moveLeft(self):
        
        self.rect.x -= self.speed

    def moveUp(self):
        
        self.rect.y += self.speed

    def moveDown(self):
        self.rect.y -= self.speed
        

    def collide(self, spriteGroup, direct):


        if pygame.sprite.spritecollide(self, spriteGroup, False):
            if direct == 'l':
                self.rect.left += 15
                #self.rect.top -= 5
            if direct == 'r':
                self.rect.left -= 15
                #self.rect.top -= 5

            if direct == 'u':
                self.rect.top -= 15

            if direct == 'd':
                self.rect.top += 15
                
  
            
