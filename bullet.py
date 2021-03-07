import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    "Class which manages the bullets fired by the ship"

    def __init__(self, ai_game):
        "Create a bullet object at the ship's current position"
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Creates a bullet rect at (0,0) position and sets the curroect position
        self.rect = pygame.Rect(0,0,self.settigs.bullet_width,
             self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
    
