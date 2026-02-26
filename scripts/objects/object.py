import pygame

from scripts.entities.entity import Entity
from scripts.const import *


class  Object(Entity):
    def __init__(self, game, pos, type, size=(16,16)):
        super().__init__(game, pos, size, type)
        
        self.is_weapon = False
        self.is_consumable = False
        self.position_adjust = False
        self.amount = 1
        self.item_description = ''
                
    @property
    def img(self):
        return self.game.assets.objects[self.type]
        
    @property
    def rect(self):
        return pygame.Rect(self.pos[0] + self.rect_offset[0], self.pos[1] + self.rect_offset[1], self.size[0], self.size[1])
    
    
    @property
    def attack_value(self):
        return self.player.strength * self.damage_amt
     
    
    def update(self, dt):
        pass
    
    def render(self, surf, offset=(0, 0)):
        # pygame.draw.rect(surf, WHITE, pygame.Rect(self.rect.x - offset[0], self.rect.y - offset[1], *self.size), 1)
        surf.blit(self.img, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
