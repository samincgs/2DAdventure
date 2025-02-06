import pygame
from ..const import *
from ..utils import load_img

from .entity import Entity

class Player(Entity):
    def __init__(self, game, pos):
        super().__init__(game, pos)
        
        self.direction = 'down'
        self.up1 = load_img(PLAYER_IMG_PATH + 'boy_up_1.png')
        self.up2 = load_img(PLAYER_IMG_PATH + 'boy_up_2.png')
        self.down1 = load_img(PLAYER_IMG_PATH + 'boy_down_1.png')
        self.down2 = load_img(PLAYER_IMG_PATH + 'boy_down_2.png')
        self.left1 = load_img(PLAYER_IMG_PATH + 'boy_left_1.png')
        self.left2 = load_img(PLAYER_IMG_PATH + 'boy_left_2.png')
        self.right1 = load_img(PLAYER_IMG_PATH + 'boy_right_1.png')
        self.right2 = load_img(PLAYER_IMG_PATH + 'boy_right_2.png')
    
    @property
    def img(self):
        if self.direction == 'up':
            img = self.up1 if self.frame_num == 1 else self.up2
        elif self.direction == 'down':
            img = self.down1 if self.frame_num == 1 else self.down2
        elif self.direction == 'right':
            img = self.right1 if self.frame_num == 1 else self.right2
        elif self.direction == 'left':
            img = self.left1 if self.frame_num == 1 else self.left2
        return img
    
    @property
    def rect(self):
        return pygame.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)
    
    def update(self, dt):
            
            if self.game.input.pressed:
                self.frame_index += dt
                if self.frame_index > 0.18:
                    self.frame_index = 0
                    self.frame_num = 1 if self.frame_num == 2 else 2
            else:
                self.frame_index = 0
            
            if self.game.input.up_pressed:
                self.y -= self.speed
                self.direction = 'up'
            elif self.game.input.down_pressed:
                self.y += self.speed
                self.direction = 'down'
            elif self.game.input.left_pressed:
                self.x -= self.speed
                self.direction = 'left'
            elif self.game.input.right_pressed:
                self.x += self.speed
                self.direction = 'right'
         
                
    def render(self, surf, offset=(0, 0)):
        surf.blit(self.img, (self.x - offset[0], self.y - offset[1]))