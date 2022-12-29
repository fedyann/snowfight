import os
import sys

import pygame

from scripts.create_levels import generate_level, load_level


def load_image(name, size, colorkey=None):
    fullname = os.path.join('../data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image1 = pygame.transform.scale(image, size)
    return image1


WIDTH = 1000
HEIGHT = 700
FPS = 60
WHITE = (255, 255, 255)
tile_images = {
    'wall': load_image('wall.jpg', (50, 50))
}
player_image = load_image('santa.gif', (50, 50))
tile_width = tile_height = 50
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SnowFight")
    clock = pygame.time.Clock()
    player, level_x, level_y = generate_level(load_level('first', player_group, all_sprites, tiles_group), player_group, all_sprites, tiles_group)
    print(all_sprites)
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        all_sprites.update()
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()

