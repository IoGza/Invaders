import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet


# Class to manage ALien Invasion window and game assets
clock = pygame.time.Clock()

class AlienInvasion:
    def __init__(self):

        # initializes game and creates the resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.bg = pygame.image.load("images/bg.png").convert()

        # Sets up the game window display and the display title/caption
        # Represented as a tuple giving the window its dimensions
        # A surface was assigned to the self.screen attribute, allowing
        # an element to be displayed on its own designated surface
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        #Creating agroup of bullets which will update a bullet passing through the screen
        self.bullets = pygame.sprite.Group()

    # Main loop for the game
    def run_game(self):
        while True:
            clock.tick(120)

            self.screen.blit(self.bg, (0, 0))
            # Separate method used for checking events such as key presses
            self._check_events()
            #Updates the positioning of the ship 
            self.ship.update()
            # Separate method used for updating the crseen elements
            self._update_screen()
            # Calls update bullets method
            self._update_bullets()
            


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets.""" 
        # Update bullet positions.
        self.bullets.update()
        #Getting rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_events(self):
        # Keyboard and mouse inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Loop used to detect and respond to a  right keystroke 
            elif event.type == pygame.KEYDOWN:
               self._check_keydown_events(event)
            # Detects if the user has lifted off of the right key
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        #Method that responds to keydown events
        if event.key == pygame.K_RIGHT:
            # Moves the ship element to the right 
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Moves the ship element to the left 
            self.ship.moving_left = True
        #Allows user to exit using the q key
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        "Creates a new bullet and adds it to the created bullet group"
        #Loop to check the number of bullets on the screen 
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            #Add method adds bullet to the group, like append
            self.bullets.add(new_bullet)

    def _update_screen(self):
        # Updates images on the screen
        # self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Loops through a list of al; the sprites available in the group
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make recently drawn screen visible, erasing the old screen and drawing a new one
        pygame.display.flip()



if __name__ == "__main__":
    # Makes an instance of the game by calling the alien invasion class
    ai = AlienInvasion()
    ai.run_game()


