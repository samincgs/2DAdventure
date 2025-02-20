import pygame

from ..const import MONSTERS

class Sword:
    def __init__(self, player, images):
        self.type = 'sword'
        self.pos = [0, 0]
        self.player = player
        self.images = images
        self.direction = player.direction
        self.get_pos()
        
        self.rect_size = 4
        self.sword_timer = 0.45
        
    @property
    def img(self):
        return self.images[self.direction]

    def get_pos(self):
        img = self.img
        if self.direction == 'up':
            pos = [self.player.rect.midtop[0] - 6, self.player.rect.midtop[1] - 22]
        elif self.direction == 'right':
            pos = [self.player.rect.midright[0] - 1, self.player.rect.midright[1] - 9]
        elif self.direction == 'down':
            pos = [self.player.rect.midbottom[0] - 5, self.player.rect.midbottom[1] - 4]
        elif self.direction == 'left':
            pos = [self.player.rect.midleft[0] - 15, self.player.rect.midleft[1] - 9]
        self.pos = list(pos)
    
    def rect(self):
        if self.direction == 'up':
            rect_offset = (6,5)
        elif self.direction == 'right':
            rect_offset = (7, 6)
        elif self.direction == 'down':
            rect_offset = (6, 7)
        elif self.direction == 'left':
            rect_offset = (5, 6)    
        sword_rect = pygame.Rect(self.pos[0] + rect_offset[0], self.pos[1] + rect_offset[1], self.rect_size, self.rect_size)
        return sword_rect
    
    def update(self, dt):
        remove = self.player.reset_attack(dt, timer=self.sword_timer)
        for slime in (monster for monster in self.player.game.entities if monster.type in MONSTERS):
            if self.player.on_screen(slime, self.player.game.scroll, self.player.game.window.display):
                if self.rect().colliderect(slime.rect):
                    slime.damage(self.player.damage_amt)           
        return remove
    
    def render(self, surf, offset=(0, 0)):
        # debug
        if self.player.game.input.debug:
            sword_rect = self.rect()
            pygame.draw.rect(surf, (255, 255, 255), pygame.Rect(sword_rect.x - offset[0], sword_rect.y - offset[1], sword_rect[2], sword_rect[3]))
        img = self.img
        surf.blit(img, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
    