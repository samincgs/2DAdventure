import pygame

from scripts.const import *
from scripts.input import Input
from scripts.entities.player import Player
from scripts.tiles.tile_manager import TileManager
from scripts.collisions import CollisionManager
from scripts.object_spawner import ObjectSpawner

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
        self.collision_manager = CollisionManager(self, self.tile_manager)
        self.player = Player(self, (372, 372), (10, 11), 'player')
        
        self.objects = []
        self.object_spawner = ObjectSpawner(self)
        
        self.scroll = [0, 0]

       
    def run(self):
        while True:
            self.display.fill((0, 0, 0))
                         
            self.scroll[0] += (self.player.rect.centerx - self.display.get_width() // 2 - self.scroll[0]) 
            self.scroll[1] += (self.player.rect.centery - self.display.get_height() // 2 - self.scroll[1])
            
            # world boundaries
            self.scroll[0] = max(0, min(self.scroll[0], WORLD_TILE_DIMENSION - DISPLAY_WIDTH))
            self.scroll[1] = max(0, min(self.scroll[1], WORLD_TILE_DIMENSION  - DISPLAY_HEIGHT))
            
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
                        
            self.input.update()
            
            self.tile_manager.render(self.display, offset=render_scroll)
            
            for obj in self.objects:
                obj.render(self.display, offset=render_scroll)
            
            self.player.update(self.dt)
            self.player.render(self.display, offset=render_scroll,)
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            
            self.dt = self.clock.tick(FPS) / 1000
            
            print('FPS: ' + str(int(self.clock.get_fps())))
            if self.input.debug:
                print(self.player.pos)
            
                    
if __name__ == "__main__":
    game = Game()
    game.run()