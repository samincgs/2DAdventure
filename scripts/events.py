from .const import *

PITFALL_DMG = 2

class  Events:
    def __init__(self, game):
        self.game = game
        self.state = self.game.state
        self.collision_manager = self.game.manager.cm
        
        self.event_locs = {'pit_fall':(16 * TILE_SIZE + TILE_SIZE / 2, 18 * TILE_SIZE + TILE_SIZE / 3), 'heal_pool': (20 * TILE_SIZE + 7, -4 * TILE_SIZE + 2)}
        self.event_rect_size = 4
        
        self.pit_fall_happened = False
            
    def events(self):
        # FALL INTO PIT (DAMAGE EVENT)
        if not self.pit_fall_happened:
            if self.collision_manager.check_event(loc=self.event_locs['pit_fall'], size=self.event_rect_size, req_direction='left', push=False):
                self.pit_fall()
                return True
        
        # HEALING EVENT (HEALTH EVENT)
        if self.collision_manager.check_event(loc=self.event_locs['heal_pool'], size=self.event_rect_size, req_direction='up'):
            self.heal_pool()
            return True
        
        return False

    def pit_fall(self):
        # functionality
        self.game.player.health -= PITFALL_DMG
        
        self.state.create_dialogue(message='You fell into a pit!', event=self.pit_fall.__name__)
        self.pit_fall_happened = True
        
        
        
    def heal_pool(self):
        if self.game.input.interacted:

            # functionality
            self.game.player.health = self.game.player.max_health
            self.game.manager.em.spawn_enemies()
            
            self.state.create_dialogue(message='You drank the water!\nYour health has been recovered.', event=self.heal_pool.__name__)