import os
import sys

import pygame


def load_image(name, size, colorkey=None):
    fullname = os.path.join('../data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image1 = pygame.transform.scale(image, size)
    return image1


if __name__ == '__main__':
    from variables import WIDTH, HEIGHT, all_sprites, FPS, WHITE, enemies_group
    from scripts.create_levels import generate_level, load_level
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SnowFight")
    clock = pygame.time.Clock()
    player, level_x, level_y = generate_level(load_level('first'))
    running = True
    SHOOT_EVENT, t, trail = pygame.USEREVENT + 1, 1000, []
    pygame.time.set_timer(SHOOT_EVENT, t)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == SHOOT_EVENT:
                player.shoot(enemies_group)
        all_sprites.update()
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()

