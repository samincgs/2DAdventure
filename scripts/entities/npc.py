import pygame
import random

from ..const import *
from .entity import Entity

class NPC(Entity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        
        self.direction = 'down'
        self.images = self.game.assets.npc_imgs
        self.speed = 60
        
        self.collision_on = True
        self.last_movement = 0
        
    
    
    def set_action(self, dt):
        
        self.action_counter += dt
        
        if self.action_counter >= 3:
            random_direction = random.randint(0, 100)
            if random_direction <= 25:
                self.direction = 'up'
            elif random_direction <= 50:
                self.direction = 'down'
            elif random_direction <= 75:
                self.direction = 'left'
            else:
                self.direction = 'right'

            self.action_counter = 0
            
    def update(self, dt):
        
        if self.last_movement != self.pos:
            self.animation_update(dt)
        
        self.last_movement = self.pos.copy()
        
        self.set_action(dt)
        self.move(dt)
        
        self.game.collision_manager.check_tile(self)
    
    def render(self, surf, offset=(0, 0)):
        super().render(surf, offset=offset)
            
    
        
        
    