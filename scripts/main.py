import pygame

from scripts.finish_screen import FinishScreen

if __name__ == '__main__':
    from scripts.variables import WIDTH, HEIGHT, all_sprites, FPS, WHITE, enemies_group, clear_groups, LEVELS, \
        background
    from scripts.create_levels import generate_level, load_level

    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    from scripts.start_screen import StartScreen

    start_screen = StartScreen(screen)
    start_screen.start_screen()
    pygame.display.set_caption("SnowFight")
    clock = pygame.time.Clock()
    player, level_x, level_y = generate_level(load_level('first'))
    running = True
    SHOOT_EVENT, t, trail = pygame.USEREVENT + 1, 1000, []
    pygame.time.set_timer(SHOOT_EVENT, t)
    level_index = 0
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == SHOOT_EVENT:
                player.shoot(enemies_group)
        all_sprites.update()
        screen.fill(WHITE)
        fon = pygame.transform.scale(background, (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        if player.health <= 0 or not enemies_group:
            if player.health <= 0:
                finish = FinishScreen(screen, 'Вы проиграли!')
            elif not enemies_group:
                finish = FinishScreen(screen, '     Победа!')
                level_index += 1
            finish.finish_screen()
            clear_groups()
            if level_index >= len(LEVELS):
                level_index = 0
            player, level_x, level_y = generate_level(load_level(LEVELS[level_index]))
    pygame.quit()
