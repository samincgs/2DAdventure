import pygame

from scripts.const import *
from scripts.input import Input
from scripts.entities.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption(CAPTION)
        self.clock = pygame.time.Clock()
        
        self.input = Input()
        self.player = Player(self)
        
        self.playerx = 100
        self.playery = 100
        self.speed = 4
        self.dt = 0.1
        
    def run(self):
        while True:
            self.display.fill((0, 0, 0))
                        
            self.input.update()
            
            self.player.update(self.dt)
            self.player.render(self.display)
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.dt = self.clock.tick(FPS) / 1000
                    

if __name__ == "__main__":
    Game().run()