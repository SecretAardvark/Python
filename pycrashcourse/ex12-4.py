import pygame 


class Settings():
    def __init__(self):
        self.screen_width = 1200 
        self.screen_height = 800 
        self.bg_color =(230, 230, 230)

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.bg_color = settings.bg_color
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)


run_game()