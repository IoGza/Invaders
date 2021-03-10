import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    "A class to report scoring information"
    def __init__(self, ai_game):
        "Initialize scorekeeping attributes"
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring infor
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        "Turn the score into a rendered image"
        # Rounds up the score and makes it comma separated
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        score_str = str(self.stats.score)
        # Create the score as an image
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Dispay the score at the top of the screen
        self.score_rect = self.score_image.get_rect()
        # Sets the right edge of the score 20 pixels from the right edge of the screen
        self.score_rect.right = self.screen_rect.right - 20
        #Place the top edge 20 pixels down from top of screen
        self.score_rect.top = 20
    
    def show_score(self):
        "Draw score and level to the screen"
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
    
    def prep_high_score(self):
        "Turn the high score into a rendered image"
        infile = open("All Time High Score.txt", "r")
        score_data = []
        for score in infile:
            score_data.append([int(i) for i in score.split()])
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render("Hi Score: " + high_score_str, True,self.text_color, self.settings.bg_color)

        # Center the highe score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def check_high_score(self):
        "Check to see if there is a new high score"
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            outfile = open("All Time High Score.txt", "w")
            outfile.write(str(self.stats.high_score))
            self.prep_high_score()
            outfile.close()

    
    def prep_level(self):
        "Turn the level into a rendered image"
        level_str = str(self.stats.level)
        self.level_image = self.font.render("Level " + level_str, True, self.text_color, self.settings.bg_color)

        # Position the level below the screen
        self.level_rect = self.level_image.get_rect()
        # Setting the level attribute to the same position as the score attribute
        self.level_rect.right = self.score_rect.right
        # Places the level attribute 10 pixels below the score attribute 
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        "Show how many ships are left"
        self.ships = Group()
        # Loop used to determine how many ships a player has left and draw that many to screen
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


