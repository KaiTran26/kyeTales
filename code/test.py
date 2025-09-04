import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1920,1080))

player_surf = pygame.Surface((108,108), pygame.SRCALPHA)
pygame.draw.circle(player_surf, "Red", (54,54), 54)

player_rect = player_surf.get_rect(center = (960,540))

background = pygame.Surface((864,864))
background.fill("Lavender")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(background, (528, 108))
    screen.blit(player_surf, player_rect)
    
    pygame.display.update()
    clock.tick(60)