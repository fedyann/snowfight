import os
import sys

import pygame

WIDTH = 1000
HEIGHT = 700
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    image1 = pygame.transform.scale(image, (100, 100))
    return image1


class Player(pygame.sprite.Sprite):
    image = load_image("creature.png")

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.x = 0
        self.y = 0

    def update(self):
        self.x = 0
        self.y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.x = -8
        if keystate[pygame.K_RIGHT]:
            self.x = 8
        if keystate[pygame.K_UP]:
            self.y = -8
        if keystate[pygame.K_DOWN]:
            self.y = 8
        self.rect.x += self.x
        self.rect.y += self.y
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("SnowFight")
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)
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