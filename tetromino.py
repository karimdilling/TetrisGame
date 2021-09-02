import pygame
import random


class Tetromino:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.grid, self.color = self.get_random_tetromino()

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
              [0, 1, 1, 0],
              [0, 0, 1, 1],
              [0, 0, 0, 0]]
        T = [[0, 0, 0, 0],
             [0, 0, 1, 0],
             [0, 1, 1, 1],
             [0, 0, 0, 0]]
        tetrominos = [I, O, T, Z2, Z, J, L]
        colors = [(0, 255, 255), (255, 255, 0), (128, 0, 128), (0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 127, 0)]
        random_number = random.randint(0, len(tetrominos) - 1)
        return tetrominos[random_number], colors[random_number]

    # def draw(self, surface):
    #     for row_index, row in enumerate(self.grid):
    #         for col_index, cell in enumerate(row):
    #             if cell == 1:
    #                 rect = [col_index * tile_size]
    #                 pygame.draw.rect(surface, self.color, rect)
