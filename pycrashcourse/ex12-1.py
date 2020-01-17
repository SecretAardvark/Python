import pygame
import sys
from ex12_2 import Rhino

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