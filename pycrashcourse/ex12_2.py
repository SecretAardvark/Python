import pygame

class Rhino():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/rhino.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)



def blue_screen():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    
    pygame.display.set_caption("Blue Screen of Death")
    bg_color = (0, 0, 255,)

    rhino = Rhino(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        rhino.blitme(self)
        
        

        pygame.display.flip()

blue_screen()