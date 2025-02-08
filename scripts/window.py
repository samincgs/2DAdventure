import pygame

from scripts.ui import UI

from .const import *

class Window:
    def __init__(self, game):
        self.game = game
        pygame.init()
        
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
         
        self.dt = 0.1 
        
        self.ui = UI(game)
        
    def render(self):
        self.dt = self.clock.tick(FPS) / 1000
        
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
        self.ui.render(self.screen)
        pygame.display.update()
        
        self.display.fill((0, 0, 0))
            