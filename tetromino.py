import pygame
import random


class Tetromino:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.grid, self.color = self.get_random_tetromino()
        # self.set_move_down_timer(500)
        self.has_landed = False
        self.fall_speed = 500  # tick time in milliseconds until moving down

    def get_random_tetromino(self):
        I = [[0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0]]
        J = [[0, 0, 1, 0],
             [0, 0, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0]]
        L = [[0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0]]
        O = [[0, 0, 0, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0]]
        Z = [[0, 0, 0, 0],
             [0, 1, 1, 0],
             [0, 0, 1, 1],
             [0, 0, 0, 0]]
        Z2 = [[0, 0, 0, 0],
              [0, 0, 1, 1],
              [0, 1, 1, 0],
              [0, 0, 0, 0]]
        T = [[0, 0, 0, 0],
             [0, 0, 1, 0],
             [0, 1, 1, 1],
             [0, 0, 0, 0]]
        tetrominos = [I, O, T, Z2, Z, J, L]
        colors = [(0, 255, 255), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 127, 0)]
        random_number = random.randint(0, len(tetrominos) - 1)
        return tetrominos[random_number], colors[random_number]

    def draw_tetromino(self, tile_size, surface):
        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    rect = pygame.Rect((col_index + self.col) * tile_size, (row_index + self.row) * tile_size, tile_size, tile_size)
                    pygame.draw.rect(surface, self.color, rect)

    def get_loc_list(self):
        loc_list = []
        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                if cell == 1:
                    loc_list.append((col_index + self.col, row_index + self.row))
        return loc_list

    def has_collided_with_bottom(self, grid_rows):
        loc_list = self.get_loc_list()
        for loc in loc_list:
            if loc[1] >= grid_rows - 1:
                return True
        return False

    def rotate_clockwise(self):
        """Rotation of a NxN matrix consists of transposing it and then
        swapping the opposing columns (e.g. first column with the last column)
        """
        # Transposing the matrix of the tetromino
        for i in range(4):
            for j in range(i, 4):
                self.grid[i][j], self.grid[j][i] = self.grid[j][i], self.grid[i][j]
        # Swapping opposing columns of the tetromino
        for i in range(4):
            for j in range(2):
                self.grid[i][j], self.grid[i][3 - j] = self.grid[i][3 - j], self.grid[i][j]

    def rotate_counter_clockwise(self):
        self.rotate_clockwise()
        self.rotate_clockwise()
        self.rotate_clockwise()

    def set_move_down_timer(self, delay):
        self.MOVE_DOWN = pygame.USEREVENT
        pygame.time.set_timer(self.MOVE_DOWN, delay)
