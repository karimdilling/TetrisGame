import pygame
from tetromino import Tetromino


class Grid:
    def __init__(self, rows, cols, tile_size, font_surface):
        self.surface = pygame.Surface((cols * tile_size, rows * tile_size))
        self.rect = self.surface.get_rect()
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.tetromino = Tetromino(-4, cols//2 - 2)
        self.landed_tetrominos = self.create_stack()
        self.font_surface = font_surface

    def create_stack(self):
        """The stack contains all the landed tetrominos within the grid"""
        landed = [[0 for j in range(self.cols)] for i in range(self.rows)]
        return landed

    def update_stack(self):
        """Updates the list of all the landed tetrominos"""
        for row_index, row in enumerate(self.tetromino.grid):
            for col_index, cell in enumerate(row):
                if cell != 0 and self.tetromino.has_landed:
                    self.landed_tetrominos[row_index + self.tetromino.row][col_index + self.tetromino.col] = self.tetromino.grid[row_index][col_index]

    def draw_stack(self):
        """Draws the stack with all the landed tetrominos onto the grid"""
        self.update_stack()
        for row_index, row in enumerate(self.landed_tetrominos):
            for col_index, cell in enumerate(row):
                if cell != 0:
                    rect = pygame.Rect(col_index * self.tile_size, row_index * self.tile_size, self.tile_size, self.tile_size)
                    pygame.draw.rect(self.surface, "white", rect)

    def clear_row(self):
        """Looks for rows in the landed list that are full of non zero numbers
        (hence that tile is occupied), overwrites those rows with zeros and puts
        that row in the beginning of the list, so every row above falls one tile
        down.
        """
        for row_index, row in enumerate(self.landed_tetrominos):
            count = 0
            for col_index, cell in enumerate(row):
                if cell != 0:
                    count += 1
            if count >= self.cols:
                for col_index, cell in enumerate(row):
                    self.landed_tetrominos[row_index][col_index] = 0
                row_to_lift = self.landed_tetrominos.pop(row_index)
                self.landed_tetrominos.insert(0, row_to_lift)

    def check_collision_overlap(self):
        """Checks if the falling tetromino and one of the landed ones overlap
        and return True or False, so the movement can be withdrawn before drawing
        to the grid.
        """
        for row_index, row in enumerate(self.tetromino.grid):
            if row_index + self.tetromino.row >= 0: # Makes sure no negative rows get checked (tetrominos fall in from the top)
                for col_index, cell in enumerate(row):
                    if cell != 0:
                        i = row_index + self.tetromino.row
                        j = col_index + self.tetromino.col
                        if j < 0:
                            return True
                        elif j >= self.cols:
                            return True
                        elif i >= self.rows:
                            return True
                        elif self.landed_tetrominos[i][j] != 0:
                            return True
        return False

    def draw_grid_lines(self):
        for row in range(1, self.rows):
            y = row * self.tile_size
            pygame.draw.line(self.surface, "grey", (0, y), (self.surface.get_width(), y))
        for col in range(1, self.cols):
            x = col * self.tile_size
            pygame.draw.line(self.surface, "grey", (x, 0), (x, self.surface.get_height()))
        pygame.draw.rect(self.surface, "grey", self.rect, 1)

    def run_stack(self):
        self.surface.fill("black")
        self.clear_row()
        self.draw_stack()
    
    def run_tetromino_and_grid(self):
        if self.tetromino.has_landed:
            self.tetromino = Tetromino(-4, self.cols//2 - 2)
        self.tetromino.draw_tetromino(self.tile_size, self.surface)
        self.draw_grid_lines()
