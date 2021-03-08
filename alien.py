import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    "A class to represent a single alien in the fleet"

    def __init__(self, ai_game):
        "Intitialize the alien and give it a start position"
        super().__init__()
        self.screen = ai_game.screen

        # Used to access speed method in update
        self.settings = ai_game.settings

        #Load an image of the alien and set the rect attribute
        self.image = pygame.image.load('images/alien_3.png')
        self.rect = self.image.get_rect()

        # Start alien position at top left of screen
        self.rect.x = 0
        self.rect.y = 0

    def check_edges(self):
        "Return True if alien is at edge of screen"
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        "Move the alien to the right"
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        # Store the horizontal position of the alien
        self.rect.x = self.x 
    

