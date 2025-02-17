import pygame
import math

from ..const import *

from .entity import Entity

class Player(Entity):
    def __init__(self, game, pos, size, type):        
        super().__init__(game, pos, size, type)
        
        self.direction = 'down'
        self.images = self.game.assets.player
        self.speed = 110
        
        self.max_health = 6 # 2 health equals one whole heart, 1 equals half heart
        self.health = self.max_health
        
        self.collision_on = True
        
        self.has_keys = 0
        self.last_movement = 0
        
        self.frame_motion = [0, 0]
        
        self.interact_range = 18
        
        self.animation_timer = 0.14
        
    
    @property
    def img(self):
        return self.images[self.direction][self.frame_index]
    
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

    
    def animation_update(self, dt):
        self.frame_num += dt
        if self.frame_num > self.animation_timer:
            self.frame_index += 1
            self.frame_num = 0
            if self.frame_index >= len(self.images[self.direction]):
                self.frame_index = 0
    
    def update(self, dt):
            
            movement = self.move(dt)
            
            self.pos[0] += movement[0]
            self.pos[1] += movement[1]
            
            self.pos[0] = round(self.pos[0])
            self.pos[1] = round(self.pos[1])

            
            self.game.collision_manager.check_tile(self)
            
            if self.on_screen(self.game.old_wizard, self.game.scroll, self.game.window.display):
                self.game.collision_manager.check_entity(self, self.game.old_wizard)
                
                dis = self.get_distance(self.game.old_wizard)
                if dis < self.interact_range:
                    if self.game.input.interacted:
                        self.game.set_state('dialogue')
                        self.game.interacted_npc = self.game.old_wizard
                        self.game.interacted_npc.turn_to_player(self)
                        self.game.interacted_npc.speak()
               
                        
            if self.game.input.pressed:    
                self.animation_update(dt)
            else:
                self.frame_num = 0
                self.frame_index = 0
                
            
    def render(self, surf, offset=(0, 0)):
        img = self.img
        if self.game.input.debug:
            pygame.draw.rect(surf, WHITE, pygame.Rect(self.rect.x - offset[0], self.rect.y - offset[1], self.rect.size[0], self.rect.size[1])) #debug
        offset = self.render_offset(offset=offset)
        
        surf.blit(img, (int(self.pos[0] - offset[0]), int(self.pos[1] - offset[1])))



        