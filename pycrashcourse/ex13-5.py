import pygame 
import sys 

class Settings():
    def __init__():
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color= (230,230,230)

        self.ship_limit = 3 

        self.ball_width = 3
        self.ball_height = 15
        self.ball_color = 60, 60, 60 


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(self.screen_width, self.screen_height)
