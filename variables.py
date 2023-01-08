import pygame

from scripts.main import load_image

WIDTH = 1000
HEIGHT = 700
FPS = 60
WHITE = (255, 255, 255)
tile_width = tile_height = 50
bullet_width = bullet_height = 20
tile_images = {
    'wall': load_image('wall.jpg', (tile_width, tile_height))
}
player_image = load_image('santa.gif', (50, 50))
enemy_image = load_image('snegovik.png', (50, 50))
bullet_image = load_image('snowball.png', (bullet_width, bullet_height))
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
bullet_speed = 10