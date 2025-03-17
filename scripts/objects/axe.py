import pygame

from .object import Object


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

class Axe(Object):
    def __init__(self, game, pos, size, player):
        super().__init__(game, pos, 'axe', size)
        self.player = player
        self.item_description = "[ Woodcutter's Axe ]\n\nA flimsy axe that still\nseems to get the job done."
        self.damage_amt = 1
        self.is_weapon = True
        self.animation_timer = [0.36, 0.50]
        
    @property
    def img(self): # image is instead the animation for player sword swing
        img = self.player.images[self.type + '_' + self.player.direction][self.player.attack_index]
        return img
    
    @property
    def ui_img(self):
        return self.game.assets.objects[self.type]
    
    @property
    def rect(self):
        return pygame.Rect(int(self.player.pos[0] + WEAPON_RECT_OFFSET['offset'][self.player.direction][0]), int(self.player.pos[1] + WEAPON_RECT_OFFSET['offset'][self.player.direction][1]), WEAPON_RECT_OFFSET['size'][self.player.direction][0], WEAPON_RECT_OFFSET['size'][self.player.direction][1])