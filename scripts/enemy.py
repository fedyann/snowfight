import math

import pygame

from variables import enemy_image, tile_width, tile_height, enemies_group, all_sprites, tiles_group, HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        super().__init__(enemies_group, all_sprites)
        self.player = player
        self.tiles_group = tiles_group
        self.image = enemy_image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect().move(
            tile_width * x + 15, tile_height * y + 5)
        self.rect = self.image.get_rect()
        self.rect.centerx = tile_width * x + 15
        self.rect.centery = tile_height * y + 5
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        bx, by = self.player.rect.centerx, self.player.rect.centery
        ax, ay = self.rect.centerx, self.rect.centery
        dx, dy = (bx - ax, by - ay)
        r = math.sqrt(dx * dx + dy * dy)
        if r == 0:
            return
        dx, dy = dx / r, dy / r
        speed = 2
        dx, dy = dx * speed, dy * speed
        old_rect = self.rect
        self.rect = self.rect.move(dx, dy)
        collide_object = pygame.sprite.spritecollide(self, tiles_group, False)
        if collide_object:
            self.rect = old_rect
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT