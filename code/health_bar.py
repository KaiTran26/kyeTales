import pygame

class health_bar(pygame.sprite.Sprite):
    def __init__(self, groups, hp, max_hp, size, position):
        super().__init__(groups)

        self.image = pygame.Surface(size)
        self.image.fill("Red")
        self.rect = self.image.get_rect(center = position)

        self.hp = hp
        self.max_hp = max_hp
        self.ratio = self.hp / self.max_hp

    def update(self):
        self.remaining_hp = pygame.Surface()
        self.remaining_hp.fill("Green")
        self.remaining_hp_rect = self.remaining_hp.get_rect(topleft = )
        self.image.blit(self.remaining_hp,)

        pygame.draw.rect(screen, "red", (x, y, width, height))
        pygame.draw.rect(screen, "green", (x, y, width * ratio, height)) # As hp is lowered the red is revealed