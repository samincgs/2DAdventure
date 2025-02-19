import pygame
import math

from scripts.entities.npc import NPC

from ..const import *

from ..entity import Entity

class Player(Entity):
    def __init__(self, game, pos, size, type):        
        super().__init__(game, pos, size, type)
        
        self.direction = 'down'
        self.speed = 110
        
        self.max_health = 6 # 2 health equals one whole heart, 1 equals half heart
        self.health = self.max_health
        
        self.collision_on = True
        
        self.has_keys = 0
        self.last_movement = 0
        
        self.frame_motion = [0, 0]
        self.animation_timer = 0.13
        
    def move(self, dt):
        movement = [0, 0]
        if self.game.input.up_pressed:
            self.direction = 'up'
            movement[1] -= self.speed * dt 
        elif self.game.input.down_pressed:
            self.direction = 'down'
            movement[1] += self.speed * dt
        elif self.game.input.left_pressed:
            self.direction = 'left'
            movement[0] -= self.speed * dt
        elif self.game.input.right_pressed:
            self.direction = 'right'
            movement[0] += self.speed * dt
        return movement

    
    def interact_with_npc(self, npc, turn=True):
        dis = self.get_distance(npc)
        if dis <= npc.interact_range:
            if self.game.input.interacted:
                self.game.state.set_state('dialogue')
                if npc.can_turn: npc.turn_to_player(self)
                npc.speak()
                self.game.state.interacted_npc = npc
    
    def animation_update(self, dt):
        if self.game.input.pressed: 
            super().animation_update(dt)
        else:
            self.frame_num = 0
            self.frame_index = 0
    
    def update(self, dt):
            
        movement = self.move(dt)
        
        self.pos[0] += movement[0]
        self.pos[1] += movement[1]
        
        self.pos[0] = round(self.pos[0])
        self.pos[1] = round(self.pos[1])
        
        self.animation_update(dt)
        
        self.game.collision_manager.check_tile(self)
        self.game.events.events()
        
        for entity in (npc for npc in self.game.entities if npc.type != 'player'):
            if self.on_screen(entity, self.game.scroll, self.game.window.display):
                self.game.collision_manager.check_entity(self, entity)
                if isinstance(entity, NPC):
                    self.interact_with_npc(entity)
        

    def render(self, surf, offset=(0, 0)):
        super().render(surf, offset=offset)
