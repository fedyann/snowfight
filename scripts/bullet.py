import math

import pygame

from variables import bullets_group, all_sprites, bullet_image, HEIGHT, tiles_group, bullet_width, bullet_height, \
    player_group, enemies_group


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy):
        super().__init__(bullets_group, all_sprites)
        self.enemy = enemy
        self.image = bullet_image
        self.rect = self.image.get_rect().move(x, y)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speed_x = 1
        self.speed_y = 1
        self.x = x
        self.y = y

    def update(self):
        bx, by = self.enemy.rect.centerx, self.enemy.rect.centery
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
            self.kill()
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        collide_enemy = pygame.sprite.spritecollide(self, enemies_group, False)
        if collide_enemy:
            collide_enemy[0].hit()
            self.kill()