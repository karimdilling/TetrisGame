import pygame
from tetromino import Tetromino


class Grid:
    def __init__(self, rows, cols, tile_size):
        self.surface = pygame.Surface((cols * tile_size, rows * tile_size))
        self.rect = self.surface.get_rect()
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.tetromino = Tetromino(self.rows, self.cols)

    def draw_grid_lines(self):
        for row in range(1, self.rows):
            y = row * self.tile_size
            pygame.draw.line(self.surface, "grey", (0, y), (self.surface.get_width(), y))
        for col in range(1, self.cols):
            x = col * self.tile_size
            pygame.draw.line(self.surface, "grey", (x, 0), (x, self.surface.get_height()))
        pygame.draw.rect(self.surface, "grey", self.rect, 1)

    def draw_tetromino(self):
        for row_index, row in enumerate(self.tetromino.grid):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    rect = [col_index * self.tile_size, row_index * self.tile_size, self.tile_size, self.tile_size]
                    pygame.draw.rect(self.surface, self.tetromino.color, rect)

    def draw(self):
        self.draw_tetromino()
        self.draw_grid_lines()
