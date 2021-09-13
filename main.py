import pygame
import sys
from game_window import GameWindow
from grid import Grid
from fonts import Fonts


def main():
    fonts = Fonts()
    fonts.font_render()
    game_window = GameWindow(fonts.font_surface_game_over)
    fonts.setup_game_over_screen(game_window)
    fonts.font_positions(game_window)
    clock = pygame.time.Clock()
    FPS = 60
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            # Exiting the window, pausing and restarting need to be accessible
            # here, so they work even when the other buttons are disabled due to
            # pausing the game
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if game_window.pause is False:
                        game_window.pause = True
                    else:
                        game_window.pause = False
                if event.key == pygame.K_r:
                    game_window.grid.points = 0
                    game_window.grid = Grid(16, 10, 30)
                    game_window.next_shape = Grid(4, 4, 30)
                    game_window.game_over = False
                    game_window.pause = False

        if not game_window.pause and not game_window.check_game_over():
            game_window.handle_events(events, clock)
            game_window.draw()
            font_surface_score = fonts.font_small.render("Score: " + str(game_window.points), True, fonts.WHITE)
            game_window.screen.blit(font_surface_score, fonts.font_pos_score)
            fonts.font_blit(game_window)
        elif game_window.check_game_over():
            game_window.screen.fill("black")
            game_window.screen.blit(fonts.font_surface_game_over, fonts.font_pos_game_over)
            game_window.screen.blit(fonts.font_surface_game_over_2, fonts.font_pos_game_over_2)
            font_surface_score_game_over = fonts.font_small.render("Score: " + str(game_window.points), True, fonts.WHITE)
            font_pos_score_game_over = (game_window.screen.get_width()/2 - font_surface_score_game_over.get_width()/2, fonts.font_pos_game_over[1] + 200)
            game_window.screen.blit(font_surface_score_game_over, font_pos_score_game_over)

        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
