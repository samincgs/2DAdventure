import pygame

from ..entities.entity import Entity
from ..const import *


class  Object(Entity):
    def __init__(self, game, pos, type, size=(16,16)):
        self.game = game
        self.pos = list(pos)
        self.type = type
        self.size = list(size)
        
        self.is_weapon = False
        self.collision_on = False
        self.amount = 1
        self.item_description = ''
        
        self.rect_offset = ENTITY_RECT_OFFSETS[type] if type in ENTITY_RECT_OFFSETS else (0, 0)
        
    @property
    def img(self):
        return self.game.assets.objects[self.type]
        
    @property
    def rect(self):
        return pygame.Rect(self.pos[0] + self.rect_offset[0], self.pos[1] + self.rect_offset[1], self.size[0], self.size[1])
    
    def update(self):
        pass
    
    def render(self, surf, offset=(0, 0)):
        # pygame.draw.rect(surf, WHITE, pygame.Rect(self.rect.x - offset[0], self.rect.y - offset[1], *self.size), 1)
        surf.blit(self.img, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
