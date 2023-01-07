import pygame

from scripts.main import load_image

WIDTH = 1000
HEIGHT = 700
FPS = 60
WHITE = (255, 255, 255)
tile_images = {
    'wall': load_image('wall.jpg', (50, 50))
}
player_image = load_image('santa.gif', (50, 50))
enemy_image = load_image('snegovik.png', (50, 50))
tile_width = tile_height = 50
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()