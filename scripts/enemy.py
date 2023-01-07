import pygame

from variables import enemy_image, tile_width, tile_height


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemies_group, all_sprites, tiles_group):
        super().__init__(enemies_group, all_sprites)
        self.tiles_group = tiles_group
        self.image = enemy_image
        self.rect = self.image.get_rect().move(
            tile_width * x + 15, tile_height * y + 5)
        self.rect = self.image.get_rect()
        self.rect.centerx = tile_width * x + 15
        self.rect.centery = tile_height * y + 5
        self.speed_x = 0
        self.speed_y = 0
    def update(self):
        pass