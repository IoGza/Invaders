
class GameStats:
    "Track statistics for alien Invasion"

    def __init__(self, ai_game):
        "Initialize stats"
        self.settings = ai_game.settings
        self.reset_stats()
        # Start Alien Invasion in an active state
        self.game_active = True

    def reset_stats(self):
        "Initializes stats that can change during the game"
        self.ships_left = self.settings.ship_limit
    