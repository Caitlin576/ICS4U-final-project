import pygame

class Text():

    def __init__(name, colour, size, text):
        self.name = name
        self.colour = colour
        self.size = size
        self.text = text
        #self.x = x
        #self.y = y
        #self.surface = surface

    #def centerText(self):
        #self.x = self


    def renderText(self):
        i = pygame.font.SysFont(self.name, self.size)

        j = i.render(self.text, 1, self.colour)
