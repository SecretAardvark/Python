import pygame

class rhino():

    def __init__(self, ):
        self.screen = pygame.display.set_mode(1200, 800,)
        self.image = pygame.image.load('images/rhino.bmp')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

rhino()
rhino.blitme()