from ..utils import blit_center


class Object:
    def __init__(self, pos, name):
        self.pos = list(pos)
        self.name = name
        self.img = None
        self.collison = False
        
        
    def render(self, surf, offset=(0, 0)):
        surf.blit(self.img, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
