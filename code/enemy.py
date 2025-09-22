import pygame
from health_bar import HealthBar
from name_box import NameBox

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, sprite_path, position, size, name, max_hp, attacks):
        super().__init__(groups)

        self.image = pygame.transform.scale(pygame.image.load(sprite_path), size)
        self.rect = self.image.get_rect(topleft = position)

        self.name = name

        self.attacks = attacks


        self.max_hp = max_hp
        self.hp = max_hp
        self.width, self.height  = size
        self.x, self.y = position

        self.enemy_health_bar = HealthBar(
            groups,
            self.max_hp,
            (self.width,self.height/10),
            (self.x,self.y-(self.height/7))
        )

        self.name_box = NameBox(
            groups,
            name,
            (self.width,int(self.height/10)),
            (self.x,self.y+(self.y*6))
        )

    def take_damage(self, damage):
        self.hp -= damage
        self.enemy_health_bar.update(self.hp)
        if self.hp <= 0:
            return True