import sys

import pygame

from scripts.button import Button
from scripts.variables import play, WHITE, WIDTH, HEIGHT, back_screen


class StartScreen:
    def __init__(self, screen):
        self.FPS = 50
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.button = Button(450, 400, play, 1)

    def terminate(self):
        pygame.quit()
        sys.exit()

    def start_screen(self):
        intro_text = ["SnowFight"]
        fon = pygame.transform.scale(back_screen, (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 100)
        text_coord = 200
        for line in intro_text:
            string_rendered = font.render(line, 1, WHITE)
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 325
            text_coord += intro_rect.height
            self.screen.blit(string_rendered, intro_rect)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
            if self.button.draw(self.screen):
                return
            pygame.display.flip()
            self.clock.tick(self.FPS)

