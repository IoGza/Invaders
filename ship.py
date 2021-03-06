import pygame


# Ship Class
class Ship:

    def __init__(self,ai_game):
        # Creates a ship and gives it a starting position 

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loads teh ships image and  retreives the rectangle
        self.image = pygame.image.load('images/spaceship.png')
        self.rect = self.image.get_rect()

        # Starts a new ship at the bottom of the screens 
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        # Draws the ship at its current location
        self.screen.blit(self.image,self.rect)
