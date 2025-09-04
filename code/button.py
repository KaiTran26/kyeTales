import pygame
from text import TextBox

class Button(pygame.sprite.Sprite):
    def __init__(self, groups, button_size, position, button_colour, text_size, text, text_colour, callback):
        # Button rectangle
        super().__init__(groups)
        self.image = pygame.Surface(button_size)
        self.rect = self.image.get_rect(center = position)
        self.image.fill(button_colour)

        self.text = TextBox(
            text, 
            text_size, 
            self.image, 
            text_colour, 
            (button_size[0]//2,button_size[1]//2))
        self.text.draw()

        # Callback set up
        self.callback = callback

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # Check if the mouse has been clicked and if it is a left click
            if self.rect.collidepoint(event.pos): # If the event (mouse click) happens inside the rect
                if self.callback: # If a callback function exists
                    self.callback() # Call the function given

        