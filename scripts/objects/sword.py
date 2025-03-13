import pygame
from .object import Object

from ..const import *

class Sword(Object):
    def __init__(self, game, pos, size, player):
        super().__init__(game, pos, 'sword', size)
        self.player = player
        
        self.is_weapon = True
        self.damage_amt = 1
        self.item_description = '[ Sword ]\n\nAn old sword.'
    
        
    @property
    def img(self): # image is instead the animation for player sword swing
        img = self.player.images[self.type + '_' + self.player.direction][self.player.attack_index]
        return img
    
    @property
    def ui_img(self):
        return self.game.assets.objects[self.type]
    
    @property
    def rect(self):
        rect_offset = {
        'size': {
            'up': [6, 9],
            'down': [6, 9],
            'right': [10 , 6],
            'left': [10, 6],
            },
        'offset': {
            'up': [3, -16],
            'down': [-1, 9],
            'right': [11 , -1],
            'left': [-12, -1],
            }
        }
        return pygame.Rect(int(self.player.pos[0] + rect_offset['offset'][self.player.direction][0]), int(self.player.pos[1] + rect_offset['offset'][self.player.direction][1]), rect_offset['size'][self.player.direction][0], rect_offset['size'][self.player.direction][1])
    
    @property
    def attack_value(self):
        return self.player.strength * self.damage_amt