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
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        game_window.handle_events(events)
        game_window.draw()
        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
