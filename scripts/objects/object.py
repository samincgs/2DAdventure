import pygame

from ..const import *


class Object:
    def __init__(self, game, pos, name, size=(16, 16)):
        self.game = game
        self.pos = list(pos)
        self.name = name
        self.size = list(size)
        self.img = self.game.assets.object_imgs[self.name]
        self.img_states = None
        self.collision_on = False
        
        self.rect_offset = RECT_OFFSETS[name] if name in RECT_OFFSETS else (0, 0)
        
    @property
    def rect(self):
        return pygame.Rect(self.pos[0] + self.rect_offset[0], self.pos[1] + self.rect_offset[1], self.size[0], self.size[1])
    
    def render(self, surf, offset=(0, 0)):
        # pygame.draw.rect(surf, WHITE, pygame.Rect(self.rect.x - offset[0], self.rect.y - offset[1], *self.size), 1)
        surf.blit(self.img, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
