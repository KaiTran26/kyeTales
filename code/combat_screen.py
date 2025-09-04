import pygame
from player import Player

class CombatScreen():
    def __init__(self, window_width, window_height):
        self.sprites = pygame.sprite.Group() # Create Group
        
        # Combat & Player
        box_length = window_height-(window_height/5) # Size logic
        self.combat_box = pygame.Rect( # No need for surf
            (window_width - box_length) / 2, # Centering logic
            (window_height - box_length) / 2,
            box_length,
            box_length
        )

        self.player = Player( # Create Player and put it in group
            self.sprites,
            (window_width/2,window_height/2), 
            self.combat_box
            )

        # Graphics
        

    # Logic
    def update(self):
        self.sprites.update()

    # Graphics
    def draw(self, screen):
        screen.fill("Dark Gray")
        pygame.draw.rect(screen, "white", self.combat_box, 10)
        self.sprites.draw(screen)

    def update(self):
        self.player.update()

    def handle_event(self, event):
        pass
