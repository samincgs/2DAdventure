import pygame

from ..const import *

class Entity:
    def __init__(self, game, pos, size, type):
        self.game = game
        self.pos = list(pos)
        self.size = list(size)
        self.speed = 150
        self.direction = None
        
        self.frame_index = 0 # spriteCounter
        self.frame_num = 0
        
        self.collision_on = False
        
        self.rect_offset = RECT_OFFSETS[type] if type in RECT_OFFSETS else (0, 0)

    @property
    def rect(self):
        return pygame.Rect(*self.pos, *self.size)
    
    def update(self, dt):
        pass
    
    def render(self, surf, offset=(0, 0)):
        pass
    