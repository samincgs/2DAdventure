from .const import *

class Events:
    def __init__(self, game, collision_manager):
        self.game = game
        self.collision_manager = collision_manager
        
        self.event_rect_size = 2

    def set_event(self, event_name):
        self.game.current_event = event_name
    
    def event(self):
        # FALL INTO PIT (DAMAGE EVENT)
        pos = (16 * TILE_SIZE, 18 * TILE_SIZE)
        if self.collision_manager.check_event(loc=pos, size=self.event_rect_size,req_direction='left'): 
            self.fall_into_pit('dialogue')
            
    def fall_into_pit(self, state):
        self.game.set_state(state)
        self.game.ui.current_dialogue = 'You fell into a pit!'
        self.game.player.health -= 1
        self.set_event(self.fall_into_pit.__name__)