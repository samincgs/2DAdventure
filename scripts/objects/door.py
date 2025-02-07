
from .object import Object
from ..const import *

class Door(Object):
    def __init__(self, pos):
        super().__init__(pos, 'door')
        self.collision_on = True
        