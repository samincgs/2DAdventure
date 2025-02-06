import pygame

from scripts.const import *
from scripts.input import Input
from scripts.entities.player import Player
from scripts.tiles.tile_manager import TileManager


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        
        self.dt = 0.1 
        
        self.input = Input()
        
        self.tile_manager = TileManager(self)
        self.player = Player(self)
        
        
    def run(self):
        while True:
            self.display.fill((0, 0, 0))
                        
            self.input.update()
            
            self.tile_manager.render(self.display)
            
            self.player.update(self.dt)
            self.player.render(self.display)
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            
            self.dt = self.clock.tick(FPS) / 1000
                    
if __name__ == "__main__":
    Game().run()