from scripts.entities.npc import NPC
from scripts.window import Window
from scripts.input import Input
from scripts.assets import Assets
from scripts.ui import UI
from scripts.entities.player import Player
from scripts.tile_manager import TileManager
from scripts.collisions import CollisionManager
from scripts.object_spawner import ObjectSpawner
from scripts.const import *

class Game:
    def __init__(self):
        self.window = Window(self)
        self.input = Input(self)
        self.assets = Assets()
        self.tile_manager = TileManager(self)
        self.tile_manager.load_map('data/maps/world1.json')
        self.collision_manager = CollisionManager(self, self.tile_manager)
        self.player = Player(self, (323, 160), (7,6), 'player')
        self.old_wizard = NPC(self, (275, 150), (16, 16), 'old_wizard')
        self.ui = UI(self)
         
        self.object_spawner = ObjectSpawner(self)
        
        self.scroll = [0, 0]
        
        self.game_states = {'play': 0, 'pause': 1, 'dialogue': 2}
        self.current_state = 0
        self.last_state = self.current_state
        
        self.interacted_npc = None

    @property
    def play_state(self):
        return self.current_state == self.game_states['play']
    
    @property
    def pause_state(self):
        return self.current_state == self.game_states['pause']
    
    @property
    def dialogue_state(self):
        return self.current_state == self.game_states['dialogue']
    
    def set_state(self, state):
        self.current_state = self.game_states[state]
    
    def run(self):
        while True:
            surf = self.window.display   
            
            if not self.pause_state:
                self.last_state = self.current_state
                
            
            self.window.create(self.ui)
            
            self.scroll[0] += (self.player.rect.centerx - surf.get_width() // 2 - self.scroll[0]) 
            self.scroll[1] += (self.player.rect.centery - surf.get_height() // 2 - self.scroll[1]) 

            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            self.input.update()
            
            self.tile_manager.render_visible(surf, offset=render_scroll)
            
            # for obj in self.object_spawner.objects:
            #     obj.render(surf, offset=render_scroll)
            
            if self.current_state == self.game_states['play']:
                self.old_wizard.update(self.window.dt)
                self.player.update(self.window.dt)
            elif self.current_state == self.game_states['dialogue']:
                self.interacted_npc.continue_dialogue()
            
            
            if self.input.debug:
                print(f"POS: {self.player.pos}")         # Float position
                print(f"RECT: {self.player.rect.topleft}")  # Integer position
                print(f"SCROLL: {self.scroll}")            # Camera position
                print(f"FPS: {self.window.clock.get_fps()}") # FPS to check if dt is stable
                print("-" * 40)

            self.old_wizard.render(surf, offset=render_scroll)
            self.player.render(surf, offset=render_scroll)
            self.ui.render(surf)            
                
                              
if __name__ == "__main__":
    Game().run()