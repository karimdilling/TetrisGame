import pygame
import sys
from game_window import GameWindow


def main():
    game_window = GameWindow()
    clock = pygame.time.Clock()
    FPS = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        game_window.draw()
        clock.tick(FPS)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
