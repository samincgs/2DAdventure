import pygame
import math
import random

from ..const import *

class Entity:
    def __init__(self, game, pos, size, type):
        self.game = game
        self.pos = list(pos)
        self.size = list(size)
        self.type = type
        self.speed = 60
        self.rect_offset = ENTITY_RECT_OFFSETS[type] if type in ENTITY_RECT_OFFSETS else (0, 0)
        
        self.images = getattr(self.game.assets, type, None)
        self.direction = 'down'
        
        self.max_health = 3
        self.health = self.max_health
                
        self.invincible = False
        self.collision_on = False
        self.dead = False
        self.alpha = 100
        
        self.frame_index = 0 
        self.frame_num = 0
        self.animation_timer = 0.15
        self.action_counter = 0
        self.action_cooldown = 2
        self.invincible_time = 1
        self.invincible_counter = 0
        self.death_timer = 0
        
        self.last_movement = 0
        
        self.is_monster = False
        self.hp_bar_on = False
        self.hp_bar_counter = 0
        self.hp_bar_cooldown = 0
        
        self.death_message_shown = False
 
    @property
    def img(self):
        return self.images[self.direction][self.frame_index]
    
    @property
    def rect(self):
        return pygame.Rect(int(self.pos[0]), int(self.pos[1]), *self.size)
    
    
    
    def on_screen(self, entity, camera, display):
       return (camera[0] <= entity.pos[0] <= camera[0] + display.get_width() and camera[1] <= entity.pos[1] <= camera[1] + display.get_height())
   
    def move(self, dt):
        movement = [0, 0]
        if self.direction == 'up':
            movement[1] -= self.speed * dt
        elif self.direction == 'down':
            movement[1] += self.speed * dt
        elif self.direction == 'left':
            movement[0] -= self.speed * dt
        elif self.direction == 'right':
            movement[0] += self.speed * dt
        return movement
        
    #√(x2 - x1)^2 + (y2 - y1)^2
    def get_distance(self, target):
        return math.sqrt((self.rect.center[0] - target.rect.center[0]) ** 2 + (self.rect.center[1] - target.rect.center[1]) ** 2)   
            
    def update(self, dt):
        self.set_action(dt)
        movement = self.move(dt)
        return movement
        
    def set_action(self, dt):
        self.action_counter += dt
        if self.action_counter >= self.action_cooldown:
            self.direction = random.choice(['up', 'left', 'right', 'down'])
            self.action_counter = 0
    
    def damage(self, amt):
        if not self.invincible:
            self.health -= amt
            self.invincible = True
            
    def death_animation(self, img, surf, offset=(0, 0)):
        mask = self.gen_mask(img)
        surf.blit(mask, (int(self.pos[0] - offset[0]), int(self.pos[1] - offset[1])))
    
    def reset_invincible(self, dt):
        # invincible timer
            if self.invincible:
                self.invincible_counter += dt
                if self.invincible_counter >= self.invincible_time:
                    self.invincible = False
                    self.invincible_counter = 0
    
    def animation_update(self, dt): #TODO: fix
        self.frame_num += dt
        if self.frame_num > self.animation_timer:
            self.frame_index += 1
            self.frame_num = 0
            if self.frame_index >= len(self.images[self.direction]):
                self.frame_index = 0
    
    def gen_mask(self, curr_img):
        img = curr_img.copy()
        mask_img = pygame.mask.from_surface(img)
        mask_img = mask_img.to_surface(setcolor=(255,255,255,255), unsetcolor=(0, 0, 0, 0))
        return mask_img
     
    def check_death(self, dt):
        if self.health <= 0:
            self.dead = True
            if self.dead:
                self.death_timer += dt
                if self.death_timer > 0.2:
                    return self.dead
       
    def render_offset(self, offset=(0, 0)):
        offset = list(offset)
        if self.rect_offset:
            offset[0] += self.rect_offset[0]
            offset[1] += self.rect_offset[1]
        return offset
    
    def render(self, surf, offset=(0, 0)):
        if self.game.input.debug:
            pygame.draw.rect(surf, WHITE, pygame.Rect(self.rect.x - offset[0], self.rect.y - offset[1], self.rect.size[0], self.rect.size[1])) #debug
            
        img = self.img.copy()
        if self.invincible:
            if self.invincible_counter % 0.20 <= 0.1:
                img.set_alpha(self.alpha)  
            else:
                img.set_alpha(255)
    
        offset = self.render_offset(offset=offset)
 
        if self.dead:
            self.death_animation(img, surf, offset=offset)
        else:       
            surf.blit(img, (int(self.pos[0] - offset[0]), int(self.pos[1] - offset[1])))
        
        
    