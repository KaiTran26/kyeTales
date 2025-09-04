import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, position, combat_box_rect):
        super().__init__(groups)

        self.image = pygame.Surface((108,108), pygame.SRCALPHA) # Created a transparent surface
        pygame.draw.circle(self.image, "Black", (54,54), 54)# Drew a circle on top of the surface

        self.rect = self.image.get_rect(center = position)
        self.combat_box_rect = combat_box_rect

        self.speed = 12 # Movement speed

    def update(self):
        keys = pygame.key.get_pressed()

        temp_rect = self.rect.copy() # Copies rect before movement

        # Up and down
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        # Left and right
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        # Boundry logic
        if not self.combat_box_rect.contains(self.rect):
            self.rect = temp_rect
        # If the player is not in the combat box move them back