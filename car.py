import pygame

pygame.__init__

class Car(pygame.sprite.Sprite):
        
    def __init__(self, x, y):
        super().__init__()
        self.pic = pygame.image.load("carImg.png").convert_alpha()
        self.image = pygame.transform.rotate(self.pic, 90 )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.score = 100
        self.sound = pygame.mixer.Sound("carcrashsoundeffect.wav")
 
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
            pygame.mixer.Sound.play(self.sound)
            #self.score -= 1
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


    def playerCollision(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.score -= 1
            for sprite in spriteGroup:
                #hit from the right
                if sprite.rect.x < self.rect.x:
                    self.rect.x -= 3.5
                    
                #hit from the left
                if sprite.rect.x > self.rect.x: 
                    self.rect.x += 3.5
                    
                #hit from the bottom
                if sprite.rect.y > self.rect.y:
                    
                    self.rect.y -= 3.5
                #hit from the top
                if sprite.rect.y < self.rect.y:
                    self.rect.y += 3.5
