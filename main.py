import pygame
import sys
from game_window import GameWindow


def main():
    game_window = GameWindow()
    clock = pygame.time.Clock()
    FPS = 60
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            # Exiting the window and the pause button need to be accessible
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

        if not game_window.pause:
            game_window.handle_events(events, clock)
        game_window.draw()
        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
