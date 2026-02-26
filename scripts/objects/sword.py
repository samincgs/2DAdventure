import pygame
from scripts.objects.object import Object

WEAPON_RECT_OFFSET = {
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

class Sword(Object):
    def __init__(self, game, pos, size, player):
        super().__init__(game, pos, 'sword', size)
        self.player = player
        
        self.is_weapon = True
        self.position_adjust = True
        self.damage_amt = 1
        self.item_description = '[ Rusty Broadsword ]\n\nAn old sword.'
        self.animation_timer = [0.08, 0.40]
        self.attack_delay = 0.15
    
        
    
    @property
    def img(self):
        return self.game.assets.objects[self.type]
    
    @property
    def attack_img(self): # image is instead the animation for player sword swing
        img = self.player.images[self.type + '_' + self.player.direction][self.player.attack_index]
        return img
    
    @property
    def attack_rect(self):
        return pygame.Rect(int(self.player.pos[0] + WEAPON_RECT_OFFSET['offset'][self.player.direction][0]), int(self.player.pos[1] + WEAPON_RECT_OFFSET['offset'][self.player.direction][1]), WEAPON_RECT_OFFSET['size'][self.player.direction][0], WEAPON_RECT_OFFSET['size'][self.player.direction][1])
    
    