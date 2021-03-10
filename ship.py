import pygame
from pygame.sprite import Sprite


# Ship Class
class Ship(Sprite):

    def __init__(self,ai_game):
        # Creates a ship and gives it a starting position 
        super().__init__()
        self.screen = ai_game.screen
        #Settings attribute to be used in update method
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loads the ships image and  retreives the rectangle
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()

        # Starts a new ship at the bottom of the screens 
        self.rect.midbottom = self.screen_rect.midbottom

        #Stores a decimal number for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flag that determines if the ship is moving
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        # Uses the movement flag attribute to determine if the ship is moving 
        #Updating the ship's x value, not the rect and making sure the ship doesnt
        #Go off the bounds of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed        
        # Handles the movement to the left 
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #Updates the rect object based on the self.x object
        self.rect.x = self.x 

    def blitme(self):
        # Draws the ship at its current location
        self.screen.blit(self.image,self.rect)
    
    def center_ship(self):
        "Center the ship on the screen"
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    

