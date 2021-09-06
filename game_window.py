import pygame
from grid import Grid


class GameWindow:
    def __init__(self, font_surface):
        self.screen = pygame.display.set_mode((600, 800))
        pygame.display.set_caption("Tetris")
        self.pause = False
        self.game_over = False
        self.grid = Grid(16, 10, 30, font_surface)
        self.fall_time = 0
        self.font_surface = font_surface

    def draw(self):
        self.screen.fill("blue")
        self.screen.blit(self.grid.surface, (50, 50))
        self.grid.run_stack()
        if self.check_game_over():
            self.pause = True
            self.game_over = True
        else:
            self.grid.run_tetromino_and_grid()
    
    def check_game_over(self):
        if self.grid.tetromino.has_landed:
            for cell in self.grid.landed_tetrominos[0]:
                if cell != 0:
                    self.pause = True
                    self.game_over = True
                    return True
        return False

    def handle_events(self, events, clock):
        # Moving down the stone at given time interval
        self.fall_time += clock.get_time()
        if not self.game_over:
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
