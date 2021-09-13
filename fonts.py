import pygame


class Fonts:
    pygame.font.init()
    WHITE = (255, 255, 255)
    font = pygame.font.SysFont(None, 72)
    font_small = pygame.font.SysFont(None, 36)
    font_smallest = pygame.font.SysFont(None, 24)
    font_surface_game_over = font.render("Game Over", True, WHITE)
    font_surface_game_over_2 = font_small.render("For restart press r, otherwise close the window", True, WHITE)
    font_surface_next_shape = font_small.render("Next Tetromino:", True, WHITE)
    font_pos_score = (380, 200)
    font_pos_next_shape = (380, 10)

    def __init__(self):
        self.font_surface_list = []
        self.font_position_list = []
        self.font_pos_game_over = (0, 0)
        self.font_pos_game_over_2 = (0, 0)

    def setup_game_over_screen(self, game_window):
        self.font_pos_game_over = (game_window.screen.get_width()/2 - Fonts.font_surface_game_over.get_width()/2, game_window.screen.get_height()/2 - Fonts.font_surface_game_over.get_height()/2)
        self.font_pos_game_over_2 = (game_window.screen.get_width()/2 - Fonts.font_surface_game_over_2.get_width()/2, self.font_pos_game_over[1] + 100)

    def font_render(self):
        font_surface_controls = Fonts.font_small.render("Controls:", True, Fonts.WHITE)
        font_surface_controls_arrow = Fonts.font_smallest.render("Move left / right: left / right arrow key", True, Fonts.WHITE)
        font_surface_controls_rotate = Fonts.font_smallest.render("Rotate: y and c key", True, Fonts.WHITE)
        font_surface_controls_drop = Fonts.font_smallest.render("Drop down: Space bar", True, Fonts.WHITE)
        font_surface_controls_pause = Fonts.font_smallest.render("Pause / Unpause: p", True, Fonts.WHITE)
        font_surface_controls_restart = Fonts.font_smallest.render("Restart the game: r", True, Fonts.WHITE)
        font_surface_points = Fonts.font_smallest.render("Points for rows cleared:", True, Fonts.WHITE)
        font_surface_points_1 = Fonts.font_smallest.render("1 row: +40", True, Fonts.WHITE)
        font_surface_points_2 = Fonts.font_smallest.render("2 rows: +100", True, Fonts.WHITE)
        font_surface_points_3 = Fonts.font_smallest.render("3 rows: +300", True, Fonts.WHITE)
        font_surface_points_4 = Fonts.font_smallest.render("4 rows: +1200", True, Fonts.WHITE)

        self.font_surface_list = [
                             font_surface_controls,
                             font_surface_controls_arrow,
                             font_surface_controls_rotate,
                             font_surface_controls_drop,
                             font_surface_controls_pause,
                             font_surface_controls_restart,
                             font_surface_points, font_surface_points_1,
                             font_surface_points_2, font_surface_points_3,
                             font_surface_points_4
                             ]

    def font_positions(self, game_window):
        font_pos_game_over = (game_window.screen.get_width()/2 - Fonts.font_surface_game_over.get_width()/2, game_window.screen.get_height()/2 - Fonts.font_surface_game_over.get_height()/2)
        font_pos_game_over_2 = (game_window.screen.get_width()/2 - Fonts.font_surface_game_over_2.get_width()/2, font_pos_game_over[1] + 100)
        font_pos_points = (380, 300)
        font_pos_points_1 = (380, 325)
        font_pos_points_2 = (380, 350)
        font_pos_points_3 = (380, 375)
        font_pos_points_4 = (380, 400)
        font_pos_controls = (50, game_window.grid.rect.bottom + 100)
        font_pos_arrow = (font_pos_controls[0], font_pos_controls[1] + 50)
        font_pos_rotate = (font_pos_controls[0], font_pos_controls[1] + 75)
        font_pos_drop = (font_pos_controls[0], font_pos_controls[1] + 100)
        font_pos_pause = (font_pos_controls[0], font_pos_controls[1] + 125)
        font_pos_restart = (font_pos_controls[0], font_pos_controls[1] + 150)

        self.font_position_list = [font_pos_controls, font_pos_arrow,
                                   font_pos_rotate, font_pos_drop, font_pos_pause,
                                   font_pos_restart, font_pos_points, font_pos_points_1,
                                   font_pos_points_2, font_pos_points_3,
                                   font_pos_points_4]

    def font_blit(self, game_window):
        for i in range(11):
            game_window.screen.blit(self.font_surface_list[i], self.font_position_list[i])
        game_window.screen.blit(Fonts.font_surface_next_shape, Fonts.font_pos_next_shape)
