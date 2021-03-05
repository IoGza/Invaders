import sys
import pygame

# Class to manage ALien Invasion window and game assets
class AlienInvasion:
    def __init__(self):
        # initializes game and creates the resources
        pygame.init()

        # Sets up the game window display and the display title/caption
        # Represented as a tuple giving the window its dimensions
        # A surface was assigned to the self.screen attribute, allowing
        # an element to be displayed on its own designated surface
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Sets the background color
        self.bg_color = (230, 230, 230)

        # Main loop for the game

    def run_game(self):
        while True:
            # Keyboard and mouse inputs
            # Returns a list of events that were preformed on the method event.get()
            for event in pygame.event.get():
                # Exits the game if user chooses to quit the screen
                if event.type == pygame.QUIT:
                    sys.exit()

                # Redraws the screen through each loop, giving it a color
                self.screen.fill(self.bg_color)
                # Make recently drawn screen visible, erasing the old screen and drawing a new one
                pygame.display.flip()


if __name__ == "__main__":
    # Makes an instance of the game by calling the alien invasion class
    ai = AlienInvasion()
    ai.run_game()
