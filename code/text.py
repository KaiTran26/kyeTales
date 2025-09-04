import pygame

class TextBox:
        def __init__(self, text, text_size, target_surf, text_colour="black", position=(0,0)):
            
            # Set up
            font = pygame.font.Font(None, text_size)
            self.text_surf = font.render(text, True, text_colour)
            self.text_rect = self.text_surf.get_rect(center = position)

            self.target_surf = target_surf
        
        def draw(self):
            self.target_surf.blit(self.text_surf, self.text_rect) # Puts the text on the image surface