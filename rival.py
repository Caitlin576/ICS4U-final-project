import pygame

class Rival(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('bluesquare.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speedx = 3.5
        self.speedy = 6
        self.rect.x = x
        self.rect.y = y
        self.hit_direction = ''
        self.count = 0

        

    def rivalBound(self):
        if self.rect.y > 500:
            self.rect.y = 500

        if self.rect.y < 0:
            self.rect.y = 0

        if self.rect.x < 70:
            self.rect.x = 70

        if self.rect.x > 486:
            self.rect.x = 486

    def rivalCollision(self, spriteGroup):

        #self.rect.y -= self.speedy

        #self.count += 0.25
        #print("rival count:", self.count)
        

        if pygame.sprite.spritecollide(self, spriteGroup, False):
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

        

                
                


          
            

            
            
