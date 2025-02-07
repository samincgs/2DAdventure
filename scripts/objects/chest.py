from .object import Object
from ..const import *

class Chest(Object):
    def __init__(self, pos):
        super().__init__(pos, 'chest')
        self.collision_on = True
        