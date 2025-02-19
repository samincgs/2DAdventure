from .object import Object
from ..const import *

class Heart(Object):
    def __init__(self, game, pos):
        super().__init__(game, pos, 'full_heart')
        
        self.img_states = {'empty_heart': self.game.assets.objects['empty_heart'], 'half_heart': self.game.assets.objects['half_heart']}