import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_states import GameStates
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_function as gf
from alien import Alien

def run_game():
    #Initialize pygame,setting and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make the play button.
    play_button = Button(ai_settings, screen, "Play")

    #Create an instance to store game statistics and create a scoreboard.
    states = GameStates(ai_settings)
    sb = Scoreboard(ai_settings, screen, states)
    #setting background colour
    bg_colour = (230,230,230)

    # Make an alien.
    alien = Alien(ai_settings, screen)

    #Making ship ,a group of bullets, and a group of aliens.
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()

    #Creating the fleet of aliens.
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #Start main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, states, sb, play_button, ship, aliens, bullets)
        if states.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, states, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, states, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, states, sb, ship, aliens, bullets, play_button)

run_game()
