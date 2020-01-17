import pygame 

class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5



class Rocket():
    def __init__(self, ai_settings, screen):
        self.settings = Settings()
        self.screen = pygame.display.setmode(self.settings.screen_width, self.settings.screen_height)
        self.image = pygame.image.load(' ')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def run_game(self):
        pygame.init()
        ai_settings = self.settings
        pygame.display.set_caption('Rocket Ship')
        pygame.bg_color = ai_settings.bg_color
        screen = self.screen
        
    def check_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key = pygame.K_RIGHT:
                    self.moving_right = True
                elif event.key = pygame.K_LEFT:
                    self.moving_left = True
                elif event.key = pygame.K_UP:
                    self.moving_up = True 
