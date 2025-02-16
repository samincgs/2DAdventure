import pygame
import math

from ..const import *

from .entity import Entity

class Player(Entity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        
        self.direction = 'down'
        self.images = self.game.assets.player_imgs
        self.speed = 120
        
        self.collision_on = True
        
        self.has_keys = 0
        self.last_movement = 0
        
        self.frame_motion = [0, 0]
    
    def interact(self, obj):
        pass
                
    def get_direction(self, dt):
        if self.game.input.up_pressed:
            self.direction = 'up'
        elif self.game.input.down_pressed:
            self.direction = 'down'
        elif self.game.input.left_pressed:
            self.direction = 'left'
        elif self.game.input.right_pressed:
            self.direction = 'right'
    
     
    def update(self, dt):

            movement = [0, 0]
            speed = self.speed * dt
            
            if self.game.input.up_pressed:
                self.direction = 'up'
                movement[1] -= speed 
            elif self.game.input.down_pressed:
                self.direction = 'down'
                movement[1] += speed
            elif self.game.input.left_pressed:
                self.direction = 'left'
                movement[0] -= speed
            elif self.game.input.right_pressed:
                self.direction = 'right'
                movement[0] += speed
                        
            self.pos[0] += movement[0]
            self.pos[1] += movement[1]
            
            if self.game.input.pressed:    
                self.animation_update(dt)
            else:
                self.frame_num = 0
                self.frame_index = 1
            
            self.game.collision_manager.check_tile(self)
            self.game.collision_manager.check_entity(self, self.game.old_wizard)
            
                     
    def render(self, surf, offset=(0, 0)):
        if self.game.input.debug:
            pygame.draw.rect(surf, WHITE, pygame.Rect(self.rect.x - offset[0], self.rect.y - offset[1], self.rect.size[0], self.rect.size[1])) #debug
        offset = self.render_offset(offset=offset)
        surf.blit(self.img, (self.pos[0] - offset[0], self.pos[1] - offset[1])) 
        