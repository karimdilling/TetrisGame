import pygame
from grid import Grid


class GameWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Tetris")
        self.grid = Grid(16, 10, 30)
        self.pause = False
        self.fall_time = 0

    def draw(self):
        self.screen.fill("blue")
        self.screen.blit(self.grid.surface, (50, 50))
        self.grid.draw()

    def handle_events(self, events, clock):
        # Moving down the stone at given time interval
        self.fall_time += clock.get_time()
        if self.fall_time >= self.grid.tetromino.fall_speed:
            self.fall_time = 0
            self.grid.tetromino.row += 1
            if self.grid.check_collision_overlap():
                self.grid.tetromino.row -= 1
                self.grid.tetromino.has_landed = True
        # Handling keyboard input
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.grid.tetromino.col += 1
                    if self.grid.check_collision_overlap():
                        self.grid.tetromino.col -= 1
                if event.key == pygame.K_LEFT:
                    self.grid.tetromino.col -= 1
                    if self.grid.check_collision_overlap():
                        self.grid.tetromino.col += 1
                if event.key == pygame.K_c:
                    self.grid.tetromino.rotate_clockwise()
                    if self.grid.check_collision_overlap():
                        self.grid.tetromino.rotate_counter_clockwise()
                if event.key == pygame.K_y:
                    self.grid.tetromino.rotate_counter_clockwise()
                    if self.grid.check_collision_overlap():
                        self.grid.tetromino.rotate_clockwise()
                if event.key == pygame.K_SPACE:
                    self.grid.tetromino.fall_speed = 50
