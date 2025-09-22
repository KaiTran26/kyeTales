import pygame

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, groups, max_hp, size, position):
        super().__init__(groups)

        self.image = pygame.Surface(size)
        
        self.rect = self.image.get_rect(topleft = position)

        self.hp = max_hp
        self.max_hp = max_hp
        self.ratio = self.hp / self.max_hp

        self.width, self.height = size

        self.update(max_hp)

    def update(self, hp):

        self.image.fill("Red")

        ratio = hp / self.max_hp
        green_width = int(ratio*self.width)

        green_bar = pygame.Surface((green_width,self.height))
        green_bar.fill("Green")

        self.image.blit(green_bar, (0,0))