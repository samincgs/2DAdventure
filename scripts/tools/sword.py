import pygame

from ..const import *

class Sword:
    def __init__(self, player, images):
        self.type = 'sword'
        self.pos = [0, 0]
        self.player = player
        self.images = images
        self.direction = player.direction
        self.get_pos()
        
        self.sword_timer = 0.28
        self.rect_size = 8
        self.rect_offset = WEAPON_RECT_OFFSETS[self.type][self.direction] if self.type in WEAPON_RECT_OFFSETS else [0, 0]
        
    @property
    def img(self):
        return self.images[self.direction]

    def get_pos(self):
        img = self.img
        if self.direction == 'up':
            pos = [self.player.rect.midtop[0] - 5, self.player.rect.midtop[1] - 20]
        elif self.direction == 'right':
            pos = [self.player.rect.midright[0] - 1, self.player.rect.midright[1] - 9]
        elif self.direction == 'down':
            pos = [self.player.rect.midbottom[0] - 4, self.player.rect.midbottom[1] - 6]
        elif self.direction == 'left':
            pos = [self.player.rect.midleft[0] - 15, self.player.rect.midleft[1] - 9]
        self.pos = list(pos)
    
    def get_rect_offset(self):
        offset = WEAPON_RECT_OFFSETS[self.type][self.direction] if self.type in WEAPON_RECT_OFFSETS else [0, 0]
        return offset
    
    def rect(self):
        rect_offset = self.get_rect_offset()
        sword_rect = pygame.Rect(self.pos[0] + rect_offset[0], self.pos[1] + rect_offset[1], self.rect_size, self.rect_size)
        return sword_rect
    
    def update(self, dt):
        remove = self.player.reset_attack(dt, timer=self.sword_timer)
        for monster in (monster for monster in self.player.game.entities if monster.type in MONSTERS): # if player sword hits any enemy
            if self.rect().colliderect(monster.rect):
                monster.damage(self.player.damage_amt)
                monster.hp_bar_on = True
                monster.hp_bar_counter = 0
                opp_directions = {'right': 'left', 'left': 'right', 'up':'down', 'down': 'up'}
                monster.direction = opp_directions[self.player.direction]
                
                
                
        return remove
    
    def render(self, surf, offset=(0, 0)):
        # debug
        if self.player.game.input.debug:
            sword_rect = self.rect()
            pygame.draw.rect(surf, (255, 255, 255), pygame.Rect(sword_rect.x - offset[0], sword_rect.y - offset[1], sword_rect[2], sword_rect[3]))
        img = self.img
        surf.blit(img, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    