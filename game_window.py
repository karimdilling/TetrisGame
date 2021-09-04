import pygame
from grid import Grid
from tetromino import Tetromino


class GameWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Tetris")
        self.grid = Grid(16, 10, 30)

    def draw(self):
        self.screen.fill("blue")
        self.screen.blit(self.grid.surface, (50, 50))
        self.grid.draw()

    def handle_events(self, events):
        for event in events:
            if (event.type == self.grid.tetromino.MOVE_DOWN and not
                    self.grid.tetromino.has_collided_with_bottom(self.grid.rows)):
                self.grid.tetromino.row += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.grid.tetromino.col += 1
                if event.key == pygame.K_LEFT:
                    self.grid.tetromino.col -= 1
                if event.key == pygame.K_c:
                    self.grid.tetromino.rotate_clockwise()
                if event.key == pygame.K_y:
                    self.grid.tetromino.rotate_counter_clockwise()
