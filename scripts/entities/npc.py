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
            
    
        
        
    