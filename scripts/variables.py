import os
import sys

import pygame

WIDTH = 1000
HEIGHT = 700
FPS = 60
WHITE = (255, 255, 255)
tile_width = tile_height = 50
bullet_width = bullet_height = 20


def load_image(name, size, colorkey=None):
    fullname = os.path.join('../data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image1 = pygame.transform.scale(image, size)
    return image1


tile_images = {
    'wall': load_image('cube.png', (tile_width, tile_height))
}
play = load_image('play.png', (100, 100))
background = load_image('snow.jpg', (WIDTH, HEIGHT))
back_screen = load_image('snow2.jpg', (WIDTH, HEIGHT))
restart = load_image('restart.png', (100, 100))
player_image = load_image('santa.gif', (50, 50))
enemy_image = load_image('snegovik.png', (50, 50))
bullet_image = load_image('snowball.png', (bullet_width, bullet_height))
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
bullets_group = pygame.sprite.Group()
bullet_speed = 10
LEVELS = ['first', 'second', 'third']


def clear_groups():
    all_sprites.empty()
    tiles_group.empty()
    player_group.empty()
    enemies_group.empty()
    bullets_group.empty()