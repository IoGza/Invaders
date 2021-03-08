import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    "A class to represent a single alien in the fleet"

    def __init__(self, ai_game):
        "Intitialize the alien and give it a start position"
        super().__init__()
        self.screen = ai_game.screen

        #Load an image of the alien and set the rect attribute
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()

        # Start alien position at top left of screen
        self.rect.x = self.rect.screen_width
        self.rect.y = self.rect.screen_height

        # STore the horizontal position of the alien
        self.x = float(self.rect.x) 