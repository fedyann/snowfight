import sys

import pygame

from scripts.button import Button
from scripts.variables import WHITE, play, back_screen, WIDTH, HEIGHT, restart


class FinishScreen:
    def __init__(self, screen, result):
        self.result = result
        self.FPS = 50
        self.screen = screen
        self.clock = pygame.time.Clock()
        if result == 'Вы проиграли!':
            self.button = Button(450, 350, restart, 1)
        else:
            self.button = Button(450, 350, play, 1)

    def terminate(self):
        pygame.quit()
        sys.exit()

    def finish_screen(self):
        intro_text = [self.result]

        fon = pygame.transform.scale(back_screen, (WIDTH, HEIGHT))
        self.screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 100)
        text_coord = 100
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color(WHITE))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 250
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

