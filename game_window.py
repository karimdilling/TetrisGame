import pygame
from grid import Grid


class GameWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Tetris")
        self.grid = Grid(16, 10, 30)

    def draw(self):
        self.screen.fill("blue")
        self.screen.blit(self.grid.surface, (50, 50))
        self.grid.draw()
