import pygame

# Class which will store all of the game's settings 
class Settings:

    def __init__(self):
        # Initializing game settings and screen settings

        self.screen_width= 1000
        self.screen_height = 700
        self.bg_color = (230,230,230)

        #Sets the speed of the ship movement 
        self.ship_limit = 3


        #Values for the bullets the ship will shoot
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,0,60)
        
        #Limits number of bullets allowed on screen
        self.bullets_allowed = 3


        self.fleet_drop_speed = 10
        # Fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        "Initializes settings that change throughout the game"
        self.bullet_speed = 1.5
        self.alien_speed = 1.0
        self.ship_speed = 1.5

        # Fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring 
        self.alien_points = 50

    def increase_speed(self):
        "Increase speed settings"
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale


