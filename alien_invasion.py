import pygame
import sys
from settings import Settings
from ship import Ship


# Class to manage ALien Invasion window and game assets
class AlienInvasion:
    def __init__(self):

        # initializes game and creates the resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.bg = pygame.image.load("images/bg.png")

        # Sets up the game window display and the display title/caption
        # Represented as a tuple giving the window its dimensions
        # A surface was assigned to the self.screen attribute, allowing
        # an element to be displayed on its own designated surface
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    # Main loop for the game
    def run_game(self):
        while True:
            self.screen.blit(self.bg, (0, 0))

            # Separate method used for checking events such as key presses
            self._check_events()
            #Updates the positioning of the ship 
            self.ship.update()
            # Separate method used for updating the crseen elements
            self._update_screen()

    def _check_events(self):
        # Keyboard and mouse inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Loop used to detect and respond to a  right keystroke 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Moves the ship element to the right 
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    # Moves the ship element to the left 
                    self.ship.moving_left = True
            # Detects if the user has lifted off of the right key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False



    def _update_screen(self):
        bg = pygame.image.load("images/bg.png")
        # Updates images on the screen
        # self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make recently drawn screen visible, erasing the old screen and drawing a new one
        pygame.display.flip()


if __name__ == "__main__":
    # Makes an instance of the game by calling the alien invasion class
    ai = AlienInvasion()
    ai.run_game()
