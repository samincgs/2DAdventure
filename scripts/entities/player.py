import pygame
from ..const import *
from ..utils import load_img

from .entity import Entity

class Player(Entity):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, size)
        
        self.direction = 'down'
        self.up1 = load_img(PLAYER_IMG_PATH + 'boy_up_1.png')
        self.up2 = load_img(PLAYER_IMG_PATH + 'boy_up_2.png')
        self.down1 = load_img(PLAYER_IMG_PATH + 'boy_down_1.png')
        self.down2 = load_img(PLAYER_IMG_PATH + 'boy_down_2.png')
        self.left1 = load_img(PLAYER_IMG_PATH + 'boy_left_1.png')
        self.left2 = load_img(PLAYER_IMG_PATH + 'boy_left_2.png')
        self.right1 = load_img(PLAYER_IMG_PATH + 'boy_right_1.png')
        self.right2 = load_img(PLAYER_IMG_PATH + 'boy_right_2.png')
        
        self.collision_on = True
        
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

    
    def update(self, dt):
            
            if self.game.input.pressed:
                self.frame_index += dt
                if self.frame_index > 0.15:
                    self.frame_index = 0
                    self.frame_num = 1 if self.frame_num == 2 else 2
            else:
                self.frame_index = 0
            
            if self.game.input.up_pressed:
                self.direction = 'up'
                self.pos[1] -= self.speed
            elif self.game.input.down_pressed:
                self.direction = 'down'
                self.pos[1] += self.speed
            elif self.game.input.left_pressed:
                self.direction = 'left'
                self.pos[0] -= self.speed
            elif self.game.input.right_pressed:
                self.direction = 'right'
                self.pos[0] += self.speed
            self.game.collision_manager.check_tile(self)
         
    
    def render_offset(self, offset=(0, 0)):
        offset = list(offset)
        player_offset = (3, 5)
        if self.collision_on:
            offset[0] += player_offset[0]
            offset[1] += player_offset[1]
        return offset
        
                
    def render(self, surf, offset=(0, 0)):
        # pygame.draw.rect(surf, WHITE, pygame.Rect(self.rect.x - offset[0], self.rect.y - offset[1], self.rect.size[0], self.rect.size[1])) debug
        offset = self.render_offset(offset=offset)
        surf.blit(self.img, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        