class GameStats():

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.read_high_score()
        self.level = 1

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0 

    def read_high_score(self):
        with open('highscore.txt', 'r') as fo:
            self.high_score = int(fo.read())
        