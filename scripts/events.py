from scripts.const import TILE_SIZE

PITFALL_DMG = 2
EVENT_LOCS = {
    'pit_fall':(16 * TILE_SIZE + TILE_SIZE / 2, 18 * TILE_SIZE + TILE_SIZE / 3), 
    'heal_pool': (20 * TILE_SIZE + 7, -4 * TILE_SIZE + 2)
}

class  Events:
    def __init__(self, game, cm, em):
        self.game = game
        self.state = self.game.state
        self.cm = cm
        self.em = em
        self.player = em.player
        
        
        self.event_rect_size = 4
        
        self.pit_fall_happened = False
            
    def events(self):
        # FALL INTO PIT (DAMAGE EVENT)
        if not self.pit_fall_happened:
            if self.cm.check_event(self.player, loc=EVENT_LOCS['pit_fall'], size=self.event_rect_size, req_direction='left'):
                self.pit_fall()
                return True
        
        # HEALING EVENT (HEALTH EVENT)
        if self.cm.check_event(self.player, loc=EVENT_LOCS['heal_pool'], size=self.event_rect_size, req_direction='up'):
            self.heal_pool()
            return True
        
        return False

    def pit_fall(self):
        # functionality
        self.player.health -= PITFALL_DMG
        self.state.create_dialogue(message='You fell into a pit!', event='pitfall')
        self.pit_fall_happened = True
        
    def heal_pool(self):
        if self.game.input.interacted:
            # functionality
            self.player.health = self.player.max_health
            self.game.manager.em.spawn_enemies()
            
            self.state.create_dialogue(message='You drank the water!\nYour health has been recovered.', event='heal pool')