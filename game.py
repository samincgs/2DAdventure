from scripts.entities.npc import NPC
from scripts.events import Events
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
        self.entities = []
        self.entities.append(Player(self, (323, 160), (8,8), 'player'))
        self.entities.append(NPC(self, (275, 150), (14, 10), 'old_wizard'))
        self.player = self.entities[0]
        self.old_wizard = self.entities[-1]
        self.ui = UI(self)
        self.events = Events(self, self.collision_manager)
         
        self.object_spawner = ObjectSpawner(self)
        
        self.scroll = [0, 0]
        self.game_states = {'play': 0, 'pause': 1, 'dialogue': 2, 'menu': 3}
        self.current_state = self.game_states['menu']
        self.last_state = self.current_state
        
        self.interacted_npc = None
        self.current_event = None

    @property
    def play_state(self):
        return self.current_state == self.game_states['play']
    
    @property
    def pause_state(self):
        return self.current_state == self.game_states['pause']
    
    @property
    def dialogue_state(self):
        return self.current_state == self.game_states['dialogue']
    
    @property
    def menu_state(self):
        return self.current_state == self.game_states['menu']
    
    def set_state(self, state):
        self.current_state = self.game_states[state]
    
    def return_to_play_state(self):
        self.set_state('play')
        self.current_event = None
        self.interacted_npc = None
    
    def run(self):
        while True:
            surf = self.window.display   
            
            if not self.pause_state:
                self.last_state = self.current_state
            
            self.window.create(self.ui)
            self.input.update()
            
            if self.current_state in {self.game_states['play'], self.game_states['pause'], self.game_states['dialogue']}:
                self.scroll[0] += (self.player.rect.centerx - surf.get_width() // 2 - self.scroll[0]) 
                self.scroll[1] += (self.player.rect.centery - surf.get_height() // 2 - self.scroll[1]) 

                render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
                self.tile_manager.render_visible(surf, offset=render_scroll)
                
                # for obj in self.object_spawner.objects:
                #     obj.render(surf, offset=render_scroll)
                
                if self.current_state == self.game_states['play']:
                    for entity in self.entities:
                        entity.update(self.window.dt)
                elif self.current_state == self.game_states['dialogue']:
                    if self.interacted_npc:
                        self.interacted_npc.continue_dialogue()
                    if self.current_event:
                        if self.input.interacted:
                            self.return_to_play_state()
                
                for entity in sorted(self.entities, key=lambda x: x.pos[1]): # sprite ordering
                    entity.render(surf, offset=render_scroll)
                
                
            self.ui.render(surf)            
                
                              
if __name__ == "__main__":
    Game().run()