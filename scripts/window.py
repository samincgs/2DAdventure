import pygame

from scripts.const import SCREEN_WIDTH, SCREEN_HEIGHT, DISPLAY_WIDTH, DISPLAY_HEIGHT, FPS, BLACK, BACKGROUND_PURPLE

class Window:
    def __init__(self, game):
        pygame.init()
        
        self.game = game
        
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
         
        self.dt = 0.1

          
    def create(self, ui):
        pygame.display.set_caption(f"FPS: {int(self.clock.get_fps())}")
        
        self.dt = self.clock.tick(FPS) / 1000
        
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
        ui.render_font(self.screen)
        pygame.display.update()
        
        if self.game.state.menu_state:
            self.display.fill(BACKGROUND_PURPLE)
        else:
            self.display.fill(BLACK)
        
        
        
       
            