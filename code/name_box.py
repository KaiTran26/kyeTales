import pygame
from text import TextBox

class NameBox(pygame.sprite.Sprite):
    def __init__(self, groups, name, size, position):
        super().__init__(groups)

        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft = position)
        self.image.fill("LightBlue")

        self.width, self.height = size

        self.name_text = TextBox(
            name,
            self.height,
            self.image,
            "black",
            (self.width//2,self.height//2)
        )

        self.name_text.draw()