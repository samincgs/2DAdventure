import pygame

class Entity:
    def __init__(self, game, pos, size):
        self.game = game
        self.pos = list(pos)
        self.size = list(size)
        self.speed = 3
        self.direction = None
        
        self.up1 = None
        self.up2 = None
        self.down1 = None
        self.down2 = None
        self.left1 = None
        self.left2 = None
        self.right1 = None
        self.right2 = None
        
        self.frame_index = 0 # spriteCounter
        self.frame_num = 0
        
        self.collision_on = False

    @property
    def rect(self):
        return pygame.Rect(*self.pos, *self.size)
    
    def update(self, dt):
        pass
    
    def render(self, surf, offset=(0, 0)):
        pass
    