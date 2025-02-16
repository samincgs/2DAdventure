import pygame
from .const import *

class Window:
    def __init__(self, game):
        self.game = game
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption(f"FPS: {self.clock.get_fps():.2f}")
         
        self.dt = 0.1 
          
    def create(self, ui):
        pygame.display.set_caption(f"FPS: {self.clock.get_fps():.2f}")
        self.dt = self.clock.tick(60) / 1000
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
        # ui.render_font(self.screen, self.dt)
        pygame.display.update()
        self.display.fill((0, 0, 0))
        
        
        
       
            