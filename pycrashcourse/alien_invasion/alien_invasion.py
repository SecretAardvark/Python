import sys 
import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button

#TODO: -Change ship image to frylock from ATHF
#   -change bullet color to yellow 
#   -Figure out how to edit mooninite background color to match screen

#Bugs: -high score not displaying
#   -black screen before play button is pressed
#   - fix ship/highscore/score layout


def run_game():
    #initialize the game, settings, and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    
    pygame.bg_color = (ai_settings.bg_color)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings ,screen, stats)
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    #creates a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Starts the main loop for the game.
    while True: 
        #Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, 
        aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                bullets, play_button)


run_game()


