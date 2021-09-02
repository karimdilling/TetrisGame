import pygame


class Grid:
    def __init__(self, pos, rows, cols, tile_size):
        self.surface = pygame.Surface((cols * tile_size, rows * tile_size))
        self.rect = self.surface.get_rect(topleft=pos)
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size

    def draw(self):
        for row in range(1, self.rows + 1):
            y = row * self.tile_size
            pygame.draw.line(self.surface, "grey", (0, y), (self.surface.get_width(), y))
        for col in range(1, self.cols + 1):
            x = col * self.tile_size
            pygame.draw.line(self.surface, "grey", (x, 0), (x, self.surface.get_height()))
        pygame.draw.rect(self.surface, "grey", self.rect, 1)