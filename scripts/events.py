from .const import *

class Events:
    def __init__(self, game, state, collision_manager):
        self.game = game
        self.state = state
        self.collision_manager = collision_manager
        
        self.event_rect_size = 4
        
        self.pit_fall_happened = False
            
    def events(self):
        # FALL INTO PIT (DAMAGE EVENT)
        pos = (16 * TILE_SIZE + TILE_SIZE / 2, 18 * TILE_SIZE + TILE_SIZE / 3)
        if not self.pit_fall_happened:
            if self.collision_manager.check_event(loc=pos, size=self.event_rect_size, req_direction='left', push=False):
                self.pit_fall('dialogue')
                self.pit_fall_happened = True
        
        pos = (20 * TILE_SIZE + 7, -4 * TILE_SIZE + 2)
        # HEALING EVENT (HEALTH EVENT)
        if self.collision_manager.check_event(loc=pos, size=self.event_rect_size, req_direction='up'):
            self.heal_pool('dialogue')
            
    def pit_fall(self, state):
        self.state.set_state(state)
        self.game.ui.current_dialogue = 'You fell into a pit!'
        self.state.set_event(self.pit_fall.__name__)
        
        # functionality
        self.game.player.health -= 2
        
    def heal_pool(self, state):
        if self.game.input.interacted:
            self.state.set_state(state)
            self.game.ui.current_dialogue = 'You drank the water!\nYour health has been recovered.'
            self.state.set_event(self.heal_pool.__name__)
            
            # functionality
            self.game.player.health = self.game.player.max_health