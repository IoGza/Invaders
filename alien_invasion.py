import pygame
import sys
from settings import Settings

# Class to manage ALien Invasion window and game assets
class AlienInvasion:
    def __init__(self):

        
        # initializes game and creates the resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Sets up the game window display and the display title/caption
        # Represented as a tuple giving the window its dimensions
        # A surface was assigned to the self.screen attribute, allowing
        # an element to be displayed on its own designated surface
        pygame.display.set_caption("Alien Invasion")

        # Main loop for the game

    def run_game(self):
        while True: 

            # Keyboard and mouse inputs
            # Redraws the screen through each loop, giving it a color
            self.screen.fill(self.settings.bg_color)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Make recently drawn screen visible, erasing the old screen and drawing a new one
            pygame.display.flip()


if __name__ == "__main__":
    # Makes an instance of the game by calling the alien invasion class
    ai = AlienInvasion()
    ai.run_game()
