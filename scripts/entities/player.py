import pygame
import math

from ..const import *

from .entity import Entity

class Player(Entity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        
        self.direction = 'down'
        self.images = self.game.assets.player_imgs
        self.speed = 110
        
        self.collision_on = True
        
        self.has_keys = 0
        self.last_movement = 0
        
        self.frame_motion = [0, 0]
        
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

     
    def update(self, dt):

            movement = self.move(dt)
                        
            self.pos[0] += movement[0]
            self.pos[1] += movement[1]
            
            self.game.collision_manager.check_tile(self)
            npc_collide = self.game.collision_manager.check_entity(self, self.game.old_wizard)
            
            if npc_collide:
                if self.game.input.interacted:
                    self.game.current_state = self.game.game_states['dialogue']
            

            if self.game.input.pressed:    
                self.animation_update(dt)
            else:
                self.frame_num = 0
                self.frame_index = 1
                
            
    def render(self, surf, offset=(0, 0)):
        if self.game.input.debug:
            pygame.draw.rect(surf, WHITE, pygame.Rect(self.rect.x - offset[0], self.rect.y - offset[1], self.rect.size[0], self.rect.size[1])) #debug
        offset = self.render_offset(offset=offset)
        surf.blit(self.img, (int(round(self.pos[0]) - offset[0]), int(round(self.pos[1]) - offset[1])))



        