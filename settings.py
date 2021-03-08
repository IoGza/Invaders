import pygame

# Class which will store all of the game's settings 
class Settings:

    def __init__(self):
        # Initializing game settings and screen settings

        self.screen_width= 1000
        self.screen_height = 700
        self.bg_color = (230,230,230)
        #Sets the speed of the ship movement 
        self.ship_speed = 1.5

        #Values for the bullets the ship will shoot
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,0,60)
        
        #Limits number of bullets allowed on screen
        self.bullets_allowed = 3

        #Alien speed settings
        self.alien_speed = 1.0

        self.fleet_drop_speed = 10
        # Fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
