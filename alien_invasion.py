import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button


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

        self.bg = pygame.image.load("images/bg_1.png").convert()

        # Sets up the game window display and the display title/caption
        # Represented as a tuple giving the window its dimensions
        # A surface was assigned to the self.screen attribute, allowing
        # an element to be displayed on its own designated surface
        pygame.display.set_caption("Alien Invasion")

        #Create an instance to store hame stats
        self.stats = GameStats(self)

        self.ship = Ship(self)
        #Creating agroup of bullets which will update a bullet passing through the screen
        self.bullets = pygame.sprite.Group()

        # Adds the alien sprite into the sprite group allowing it to be drawn together with the other sprites simultaneously
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()

        # Make the play button
        self.play_button = Button(self, "Play")



    # Main loop for the game
    def run_game(self):
        while True:
            clock.tick(120)

            self.screen.blit(self.bg, (0, 0))
            # Separate method used for checking events such as key presses
            self._check_events()
            if self.stats.game_active:
                #Updates the positioning of the ship 
                self.ship.update()
                # Calls update bullets method
                self._update_bullets()
                #Calls to update alien position
                self._update_aliens()
        
             # Separate method used for updating the crseen elements
            self._update_screen()
            

    def _create_fleet(self):
        "Creates the fleet of aliens"
        # Make an alien and find the number of aliens in a row
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        #Calculation determines the width between each alien
        available_space_x = self.settings.screen_width - (2 * alien_width)
        # Calculation determines how much space is available per row on the screen
        number_aliens_x = available_space_x // (2 * alien_width)
        
        #Determine number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                                (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            # Create the first row of aliens
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)
            
    
    def _ship_hit(self):
        "Rspond to the ship being hit"
        #If block makes sure player has at least one ship left, if no ships left
        # Then the game will stop
        if self.stats.ships_left > 0:

            # Decrement ships_left
            self.stats.ships_left -= 1

            # Get rid of remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            #Pause the game once ship is hit
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _create_alien(self, alien_number, row_number):
        "Create an alien and place it in the row"
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
    
    def _check_aliens_bottom(self):
        "Check if any aliens have reached the bottom of the screen"
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if a ship was hit
                self._ship_hit()
                break

    def _update_aliens(self):
        "check if at an edge and then update the positions of aliens in the fleet"
        self._check_fleet_edges()
        self.aliens.update()

        #Look for alien/ship collisions
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        
        # Look for aliens hitting bottom of screen
        self._check_aliens_bottom()
    

    
    def _check_fleet_edges(self):
        "Determines if any of the aliens have reached an edge and handles that"
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        "Drops the entire fleet and changes the direction"
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        # Causes the fleet to move right instead of left
        self.settings.fleet_direction *= -1


    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets.""" 
        # Update bullet positions.
        self.bullets.update()
        #Getting rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
        
        

    def _check_bullet_alien_collisions(self):
        "Respond to bullet and alien collisions"
        #Remove any bullets and aliens that have collided 
        
        #Check for any bullets that have hit aliens
        # If a bullet hits, get rid of bullet and alien
        # True statements tell method to delete the bullet and alien that have collided
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if not self.aliens:
            #Destroy existing bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
            # Increases the tempo of the game
            self.settings.increase_speed()
        
    def _fire_bullet(self):
        "Creates a new bullet and adds it to the created bullet group"
        #Loop to check the number of bullets on the screen 
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            #Add method adds bullet to the group, like append
            self.bullets.add(new_bullet)

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
            # Determines if the mouse button was clicked down
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _check_keydown_events(self, event):
        #Method that responds to keydown events
        if event.key == pygame.K_RIGHT:
            # Moves the ship element to the right 
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Moves the ship element to the left 
            self.ship.moving_left = True
        #Allows user to exit using the q key
        elif event.key == pygame.K_p:
            self._start_game(event.key)
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _start_game(self, event):
        p_key_clicked = True

        if p_key_clicked and not self.stats.game_active:
            # Reset game settings
            self.settings.initialize_dynamic_settings()
            # Reset game stats
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hides the cursoe
            pygame.mouse.set_visible(False)
        else:
            p_key_clicked = False


    def _check_play_button(self, mouse_pos):
        "Start a new game when the player clicks the play button"
        # Determines if the mouse has clicked the play button
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        # For loop conditions makes it to where the game stats are reset on button push 
        # and removes the button area on game start
        if button_clicked and not self.stats.game_active:
            # Reset game settings
            self.settings.initialize_dynamic_settings()
            # Reset game stats
            self.stats.reset_stats()
            self.stats.game_active = True

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hides the cursoe
            pygame.mouse.set_visible(False)



    def _update_screen(self):
        # Updates images on the screen
        # self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Loops through a list of al; the sprites available in the group
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draws the alien sprite to the screen
        self.aliens.draw(self.screen)

        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Make recently drawn screen visible, erasing the old screen and drawing a new one
        pygame.display.flip()


if __name__ == "__main__":
    # Makes an instance of the game by calling the alien invasion class
    ai = AlienInvasion()
    ai.run_game()
