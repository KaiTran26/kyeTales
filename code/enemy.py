import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_path, position, size, name, max_hp, attacks):
        super().__init__(groups)

        self.image = pygame.transform.scale(pygame.image.load(sprite_path), size)
        self.rect = self.image.get_rect(topleft = position)

        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attacks = attacks

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            return True