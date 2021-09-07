import pygame
import sys
from game_window import GameWindow
from grid import Grid


def main():
    WHITE = (255, 255, 255)
    font = pygame.font.SysFont(None, 72)
    font_small = pygame.font.SysFont(None, 36)
    font_surface_game_over = font.render("Game Over", True, WHITE)
    font_surface_game_over_2 = font_small.render("For restart press r, otherwise close the window", True, WHITE)
    font_surface_next_shape = font_small.render("Next Tetromino:", True, WHITE)
    game_window = GameWindow(font_surface_game_over)
    font_pos_game_over = (game_window.screen.get_width()/2 - font_surface_game_over.get_width()/2, game_window.screen.get_height()/2 - font_surface_game_over.get_height()/2)
    font_pos_game_over_2 = (game_window.screen.get_width()/2 - font_surface_game_over_2.get_width()/2, font_pos_game_over[1] + 100)
    font_pos_next_shape = (380, 10)
    font_pos_score = (380, 200)
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
            game_window.screen.blit(font_surface_next_shape, font_pos_next_shape)
            font_surface_score = font_small.render("Score: " + str(game_window.points), True, WHITE)
            game_window.screen.blit(font_surface_score, font_pos_score)
        elif game_window.check_game_over():
            game_window.screen.fill("black")
            game_window.screen.blit(font_surface_game_over, font_pos_game_over)
            game_window.screen.blit(font_surface_game_over_2, font_pos_game_over_2)
            font_surface_score_game_over = font_small.render("Score: " + str(game_window.points), True, WHITE)
            font_pos_score_game_over = (game_window.screen.get_width()/2 - font_surface_score_game_over.get_width()/2, font_pos_game_over[1] + 200)
            game_window.screen.blit(font_surface_score_game_over, font_pos_score_game_over)

        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
