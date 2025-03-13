from scripts.objects.axe import Axe
from scripts.window import Window
from scripts.input import Input
from scripts.assets import Assets
from scripts.tile_manager import TileManager
from scripts.collisions import CollisionManager
from scripts.entity_manager import EntityManager
from scripts.events import Events
from scripts.state import State
from scripts.object_mapper import ObjectMapper
from scripts.ui import UI

class Game:
    def __init__(self):
        self.window = Window(self)
        self.state = State(self)
        self.input = Input(self, self.state)
        self.assets = Assets()
        self.tile_manager = TileManager(self)
        self.collision_manager = CollisionManager(self, self.tile_manager)
        self.entity_manager = EntityManager(self)
        self.ui = UI(self, self.state)
        self.events = Events(self, self.state, self.collision_manager)
        self.object_mapper = ObjectMapper(self)
        
        self.player = self.entity_manager.player
        self.scroll = [0, 0] 

    
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
                    self.entity_manager.update(self.window.dt)
                elif self.state.dialogue_state:
                    self.state.track_event_and_dialogues()
                
                self.entity_manager.render(surf, offset=render_scroll)
            
            self.ui.render(surf)   
                           
if __name__ == "__main__":
    Game().run()