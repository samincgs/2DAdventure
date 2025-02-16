import pygame

from ..const import *

class Entity:
    def __init__(self, game, pos, size, type):
        self.game = game
        self.pos = list(pos)
        self.size = list(size)
        self.speed = 60
        
        self.images = None
        self.direction = None
        
        self.frame_index = 1 # spriteCounter
        self.frame_num = 0
        
        self.last_movement = 0
        
        self.collision_on = False
        
        self.rect_offset = RECT_OFFSETS[type] if type in RECT_OFFSETS else (0, 0)
        
        self.action_counter = 0
        
    @property
    def img(self):
        img = self.images[self.direction + '_' + str(self.frame_index)]
        return img
    
    @property
    def rect(self):
        return pygame.Rect(self.pos[0] // 1, self.pos[1] // 1, *self.size)
    
    @property
    def render_pos(self):
        return [round(self.pos[0]), round(self.pos[1])]
    
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
            
        
            
    def update(self, dt):
        self.set_action(dt)
        movement = self.move(dt)
        
        self.pos[0] += movement[0]
        self.pos[1] += movement[1]
        
    def set_action(self, dt):
        pass
    
    def animation_update(self, dt):
        self.frame_num += dt
        if self.frame_num > 0.15:
            self.frame_index = 1 if self.frame_index == 2 else 2
            self.frame_num = 0
        
    def render_offset(self, offset=(0, 0)):
        offset = list(offset)
        if self.rect_offset:
            offset[0] += self.rect_offset[0]
            offset[1] += self.rect_offset[1]
        return offset
    
    def render(self, surf, offset=(0, 0)):
        if self.game.input.debug:
            pygame.draw.rect(surf, WHITE, pygame.Rect(self.rect.x - offset[0], self.rect.y - offset[1], self.rect.size[0], self.rect.size[1])) #debug
        offset = self.render_offset(offset=offset)
        surf.blit(self.img, (int(self.pos[0] - offset[0]), int(self.pos[1] - offset[1])))
    