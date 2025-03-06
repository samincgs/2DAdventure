from scripts.window import Window
from scripts.input import Input
from scripts.assets import Assets
from scripts.tile_manager import TileManager
from scripts.collisions import CollisionManager
from scripts.events import Events
from scripts.state import State
from scripts.object_mapper import ObjectMapper
from scripts.ui import UI
from scripts.entities.old_wizard import OldWizard
from scripts.entities.player import Player
from scripts.entities.knight import Knight
from scripts.monsters.green_slime import GreenSlime
from scripts.const import *

class Game:
    def __init__(self):
        self.window = Window(self)
        self.state = State(self)
        self.input = Input(self, self.state)
        self.assets = Assets()
        self.tile_manager = TileManager(self)
        self.collision_manager = CollisionManager(self, self.tile_manager)
        self.ui = UI(self, self.state)
        self.events = Events(self, self.state, self.collision_manager)
        self.object_mapper = ObjectMapper(self)
        
        self.entities = []
        self.load_entities()

        self.scroll = [0, 0] 

    def spawn_enemies(self):
        # reset monsters if they alr exist
        self.entities = [entity for entity in self.entities if entity.type not in MONSTERS]
        
        # monsters
        self.entities.append(GreenSlime(self, (636, 348), (11, 10), 'green_slime')) 
        self.entities.append(GreenSlime(self, (650, 363), (11, 10), 'green_slime')) 
        self.entities.append(GreenSlime(self, (610, 358), (11, 10), 'green_slime')) 
        self.entities.append(GreenSlime(self, (688, -176), (11, 10), 'green_slime')) 
    
    def load_entities(self):
        self.entities.append(Player(self, (326, 165), (8,8), 'player'))
        self.player = self.entities[-1]
         
        #npcs
        self.entities.append(OldWizard(self, (275, 150), (14, 10), 'old_wizard'))
        self.entities.append(Knight(self, (404, 367), (12, 14), 'knight'))
        
        # monsters
        self.spawn_enemies()

    def run(self):
        while True:
            
            surf = self.window.display   
            
            self.window.create(self.ui)
            self.input.update()
            self.state.track_last_state()
            
            if self.state.ingame_state:
                self.scroll[0] += (self.player.rect.centerx - surf.get_width() // 2 - self.scroll[0]) 
                self.scroll[1] += (self.player.rect.centery - surf.get_height() // 2 - self.scroll[1]) 
                render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

                self.tile_manager.render_visible(surf, offset=render_scroll)
                self.object_mapper.render(surf, offset=render_scroll)
                
                if self.state.play_state: 
                    for entity in self.entities.copy():
                        kill = entity.update(self.window.dt)
                        if kill:
                            self.entities.remove(entity)
                            self.player.check_level_up()
                elif self.state.dialogue_state:
                    self.state.track_event_and_dialogues()
                
                for entity in sorted(self.entities, key=lambda x: x.pos[1]): # sprite ordering
                    entity.render(surf, offset=render_scroll)
            
            self.ui.render(surf)   
                           
if __name__ == "__main__":
    Game().run()