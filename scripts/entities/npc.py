import pygame
import random

from ..const import *
from .entity import Entity

class NPC(Entity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        
        self.direction = random.choice(['up', 'left', 'right', 'down'])
        self.images = self.game.assets.npc_imgs
        self.speed = 30
        
        self.collision_on = True
        self.last_movement = 0
    
    def set_action(self, dt):
        
        self.action_counter += dt
        
        if self.action_counter >= 2:
            self.direction = random.choice(['up', 'left', 'right', 'down'])
            self.action_counter = 0
    
    def speak(self):
        self.game.ui.current_dialogue = self.dialogues[self.dialogue_index]
             
    def continue_dialogue(self):
        if self.game.input.interacted:
            self.dialogue_index += 1
            if self.dialogue_index >= len(self.dialogues):
                self.dialogue_index = 0
                self.game.current_state = self.game.game_states['play']
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
        
        super().update(dt)
        
        if self.last_movement != self.pos:
            self.animation_update(dt)  
            self.game.collision_manager.check_tile(self)
        
        if self.on_screen(self, self.game.scroll, self.game.window.display):
            self.game.collision_manager.check_entity(self, self.game.player)
            
        
        self.last_movement = self.pos.copy()        
    
    def render(self, surf, offset=(0, 0)):
        super().render(surf, offset=offset)
            
    
        
        
    