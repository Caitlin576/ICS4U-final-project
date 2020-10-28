import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

car = pygame.image.load('alien.png')

class playerCar(pygame.sprite.Sprite):

    def __init__(self, image):
        super().__init__()

        self.image = car
        self.rect = self.image.get_rect()
        
    def moveRight(self, change):
        self.rect.x += change

    def moveLeft(self, change):
        self.rect.x -= change

player1 = playerCar(car)
player1.rect.x = 300
player1.rect.y = 100

playerGroup = pygame.sprite.Group()

playerGroup.add(player1)

running = True

while running:
    for event in pygame.event.get():

        if event.type== pygame.QUIT:
            pygame.quit()
            running = False

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.moveLeft(1)

            if event.key == pygame.K_RIGHT:
                player1.moveRight(1)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
                


    

    playerGroup.update()

    playerGroup.draw(screen)

    pygame.display.update()






  







    
