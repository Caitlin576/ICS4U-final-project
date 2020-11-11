import pygame

pygame.init()

#create sprite class for the rival car
class Rival(pygame.sprite.Sprite):

    pygame.mixer.music.load('GameMusic.wav')
    pygame.mixer.music.play(-1)

    #take x and y values for initialization
    def __init__(self, x, y):
        #initialize the sprite class
        super().__init__()
        #load the image of the rival car and convert it to prevent lagging
        self.pic = pygame.image.load("rivalImg.png").convert_alpha()
        #rotate to image 90 degrees
        self.image = pygame.transform.rotate(self.pic, 90 )
        #get the rectangle values (x, y, w, h) of the image
        self.rect = self.image.get_rect()
        #create variables for the speed in x and y directions for the rival
        self.speedx = 3.5
        self.speedy = 6
        #set the x and y coordinates to the values of the parameters passed
        self.rect.x = x
        self.rect.y = y
        #create an empy variable to hold the direction that the rival was hit from
        self.hit_direction = ''
        self.count = 0

    #create a function to keep the rival within certain boundaries. 

    def rivalBound(self):
        if self.rect.y > 500:
            self.rect.y = 500

        if self.rect.y < -64:
            self.rect.y = -64

        if self.rect.x < 70:
            self.rect.x = 70

        if self.rect.x > 486:
            self.rect.x = 486

    #create a function to handle collision of the rival

    def rivalCollision(self, spriteGroup):

        #if the rival bumps into an object from another sprite group,
        #the rival bounces away from the object that hit it by checking
        #whether the rival or the other sprite has the greatest x/y value
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
