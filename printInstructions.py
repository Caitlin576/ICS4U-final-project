

def printInstruct(string, y, font, colour, screen):

    text = font.render(string, 1, colour)
    screen.blit(text, (screen.get_width()/2 - text.get_width()/2, y))
    
  
