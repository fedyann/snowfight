import pygame

from variables import tile_images, tile_width, tile_height


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, tiles_group, all_sprites):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
