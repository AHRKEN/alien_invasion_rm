import os


class GameStats():
    """Track statistics for Alien Invasion"""
    
    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start Alien Invasion in an inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0
        high_score_file = 'high_score.txt'
        try:
            with open(high_score_file) as hs_file:
                self.high_score = int(hs_file.read())
        # If there is no 'high_score.txt' file, then create it
        except FileNotFoundError:
            if not os.path.exists(high_score_file):
                with open(high_score_file, 'w+') as hs_file:
                    hs_file.write('0')
                self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
