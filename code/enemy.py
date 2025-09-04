import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_path, name, max_hp, attacks):
        super().__init__(groups)

        self.image = pygame.image.load(sprite_path)
        self.rect = self.image.get_rect(center = (1056,540))

        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attacks = attacks

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            return True
        
    def draw_health_bar(self, screen):
        # Draw a health bar above the enemy
        width = 100
        height = 10
        ratio = self.hp / self.max_hp
        x = self.rect.centerx - width // 2 # From the centre, move to the centre
        y = self.rect.top - 20 # Move up from rect's top

        pygame.draw.rect(screen, "red", (x, y, width, height))
        pygame.draw.rect(screen, "green", (x, y, width * ratio, height)) # As hp is lowered the red is revealed
