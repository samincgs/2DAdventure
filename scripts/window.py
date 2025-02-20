import pygame
import time

from .const import *

class Window:
    def __init__(self, game):
        pygame.init()
        
        self.game = game
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption(f"FPS: {self.clock.get_fps():.2f}")
         
        self.dt = 0.1 
        
        # self.start_time = time.time()
          
    def create(self, ui):
        
        # self.dt = time.time() - self.start_time
        # self.start_time = time.time()
        
        pygame.display.set_caption(f"FPS: {int(self.clock.get_fps())}")
        self.dt = self.clock.tick(FPS) / 1000
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
        ui.render_font(self.screen)
        pygame.display.update()
        self.display.fill((0, 0, 0))
        
        
        
       
            