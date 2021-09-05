import pygame
from grid import Grid


class GameWindow:
    def __init__(self):
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Tetris")
        self.grid = Grid(16, 10, 30)
        self.pause = False

    def draw(self):
        self.screen.fill("blue")
        self.screen.blit(self.grid.surface, (50, 50))
        self.grid.draw()

    def handle_events(self, events):
        for event in events:
            if event.type == self.grid.tetromino.MOVE_DOWN and not self.grid.tetromino.has_landed:
                self.grid.tetromino.row += 1
                if self.grid.check_collision_overlap():
                    self.grid.tetromino.row -= 1
                    self.grid.tetromino.has_landed = True
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
                    pygame.time.set_timer(self.grid.tetromino.MOVE_DOWN, 50)
                if event.key == pygame.K_p:
                    if self.pause is False:
                        pygame.time.set_timer(self.grid.tetromino.MOVE_DOWN, 0)
                        self.pause = True
                    else:
                        pygame.time.set_timer(self.grid.tetromino.MOVE_DOWN, 500)
                        self.pause = False
