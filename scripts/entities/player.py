import pygame
from ..const import *
from ..utils import load_img

from .entity import Entity

class Player(Entity):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        
        self.direction = 'down'
        self.player_imgs = self.game.assets.player_imgs
        
        self.rect_offset = RECT_OFFSETS[type] if type in RECT_OFFSETS else (0, 0)
        self.collision_on = True
        
        self.has_keys = 0
        self.last_movement = 0
    
 
    @property
    def img(self):
        if self.direction == 'up':
            img = self.player_imgs['up_1'] if self.frame_num == 1 else self.player_imgs['up_2']
        elif self.direction == 'down':
            img = self.player_imgs['down_1'] if self.frame_num == 1 else self.player_imgs['down_2']
        elif self.direction == 'right':
            img = self.player_imgs['right_1'] if self.frame_num == 1 else self.player_imgs['right_2']
        elif self.direction == 'left':
            img = self.player_imgs['left_1'] if self.frame_num == 1 else self.player_imgs['left_2']
        return img

    def interact(self, obj):
        if obj:
            if obj.name == 'key':
                self.has_keys += 1
                self.game.object_spawner.objects.remove(obj)
                self.game.audio.sounds['coin'].play()
                self.game.ui.create_message('You got a key!')
            elif obj.name == 'door':
                if self.has_keys:
                    self.game.object_spawner.objects.remove(obj)
                    self.has_keys -=1
                    self.game.ui.create_message('You opened the door!')
                else:
                    self.game.ui.create_message('Seems like you need a key.')
            elif obj.name == 'sneaker':
                self.game.object_spawner.objects.remove(obj)
                self.speed += 50
                self.game.ui.create_message('You can now run faster!')
            elif obj.name == 'chest3':
                state = 'opened'
                obj.img = load_img(OBJECT_IMG_PATH + obj.name  + '_' + state + '.png')
                self.game.game_over = True
    
    def update(self, dt):
            
            self.last_movement = self.pos.copy()
            
            if self.game.input.pressed:
                self.frame_index += dt
                if self.frame_index > 0.15:
                    self.frame_index = 0
                    self.frame_num = 1 if self.frame_num == 2 else 2
            else:
                self.frame_num = 1
                self.frame_index = 0
            
            if self.game.input.up_pressed:
                self.direction = 'up'
                self.pos[1] -= int(self.speed * dt)
            elif self.game.input.down_pressed:
                self.direction = 'down'
                self.pos[1] += int(self.speed * dt)
            elif self.game.input.left_pressed:
                self.direction = 'left'
                self.pos[0] -= int(self.speed * dt)
            elif self.game.input.right_pressed:
                self.direction = 'right'
                self.pos[0] += int(self.speed * dt)
                                
            self.game.collision_manager.check_tile(self)
            # obj  = self.game.collision_manager.check_object(self)
            # self.interact(obj)
            
    def render_offset(self, offset=(0, 0)):
        offset = list(offset)
        if self.collision_on:
            offset[0] += self.rect_offset[0]
            offset[1] += self.rect_offset[1]
        return offset
         
    def render(self, surf, offset=(0, 0)):
        img = self.img
        if self.game.input.debug:
            pygame.draw.rect(surf, WHITE, pygame.Rect(self.rect.x - offset[0], self.rect.y - offset[1], self.rect.size[0], self.rect.size[1])) #debug
        offset = self.render_offset(offset=offset)
        surf.blit(img, (int(self.pos[0] - offset[0]) , int(self.pos[1] - offset[1])))
        