from scripts.entities.entity import Entity
from scripts.const import DIALOGUES

class NPC(Entity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        
        self.direction = 'down'
        self.speed = 30
        
        self.dialogues = DIALOGUES[type] if type in DIALOGUES else []
        self.dialogue_index = 0
        
        self.collision_on = True
        
        self.interact_range = 12
         
        self.movement_timer = 0
        self.movement_cooldown = 3
        self.keep_moving = 4
        
    def speak(self):
        self.game.renderer.ui.current_dialogue = self.dialogues[self.dialogue_index]
             
    def continue_dialogue(self):
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
    
    def render(self, surf, offset=(0, 0)):
        super().render(surf, offset=offset)
            
    
        
        
    