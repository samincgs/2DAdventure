from .entity import Entity
from ..const import *

class NPC(Entity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        
        self.direction = 'down'
        self.speed = 30
        
        self.dialogues = DIALOGUES[type] if type in DIALOGUES else []
        self.dialogue_index = 0
        
        self.collision_on = True
        self.last_movement = 0
        
        self.interact_range = 12
        self.can_move = True
        self.can_turn = True
         
        self.movement_timer = 0
        self.movement_cooldown = 3
        self.keep_moving = 4
        
    def speak(self):
        self.game.ui.current_dialogue = self.dialogues[self.dialogue_index]
             
    def continue_dialogue(self):
        if self.game.input.interacted:
            self.dialogue_index += 1
            if self.dialogue_index >= len(self.dialogues):
                self.dialogue_index = 0
                self.game.state.return_to_play_state()
                return
            self.speak()
    
    def turn_to_player(self, player):
        if player.direction == 'left':
            self.direction = 'right'
        elif player.direction == 'right':
            self.direction = 'left'
        elif player.direction == 'down':
            self.direction = 'up'
        else:
            self.direction = 'down'
    
    def update(self, dt):
        
        if self.can_move:
            movement = super().update(dt)
            
            self.movement_timer += dt
            if self.movement_timer > self.movement_cooldown:
                self.pos[0] += movement[0]
                self.pos[1] += movement[1]
                if self.movement_timer > self.keep_moving:
                    self.movement_timer = 0
            
            if self.last_movement != self.pos:
                self.animation_update(dt)  
                self.game.collision_manager.check_tile(self)
            
            if self.on_screen(self, self.game.scroll, self.game.window.display): # check if self is on the screen
                self.game.collision_manager.check_entity(self, self.game.player)
                
            
            self.last_movement = self.pos.copy()        
    
    def render(self, surf, offset=(0, 0)):
        super().render(surf, offset=offset)
            
    
        
        
    