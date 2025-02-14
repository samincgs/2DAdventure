from scripts.window import Window
from scripts.input import Input
from scripts.assets import Assets
from scripts.ui import UI
from scripts.entities.player import Player
from scripts.audio import AudioManager
from scripts.tile_manager import TileManager
from scripts.collisions import CollisionManager
from scripts.object_spawner import ObjectSpawner
from scripts.const import *

class Game:
    def __init__(self):
        self.window = Window(self)
        self.input = Input(self)
        self.assets = Assets()
        self.audio = AudioManager()
        self.tile_manager = TileManager(self)
        self.tile_manager.load_map('data/maps/world1.json')
        self.collision_manager = CollisionManager(self, self.tile_manager)
        self.player = Player(self, (323, 160), (9, 10), 'player')
        self.ui = UI(self)
        
        self.object_spawner = ObjectSpawner(self)
        
        self.scroll = [0, 0]
        
        self.game_over = False
        
        
    def run(self):
        while True:
            surf = self.window.display   
            
            self.window.render(self.ui)
            
            self.scroll[0] += (self.player.rect.centerx - surf.get_width() // 2 - self.scroll[0]) 
            self.scroll[1] += (self.player.rect.centery - surf.get_height() // 2 - self.scroll[1])
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            self.input.update()
            
            self.tile_manager.render(surf, offset=render_scroll)
            
            for obj in self.object_spawner.objects:
                obj.render(surf, offset=render_scroll)
        
            if not self.game_over:
                self.player.update(self.window.dt)
                self.ui.render(surf)
                
            self.player.render(surf, offset=render_scroll)
            
            # print('FPS: ' + str(int(self.window.clock.get_fps())))
            if self.input.debug:
                print(self.player.pos)
                
                              
if __name__ == "__main__":
    Game().run()