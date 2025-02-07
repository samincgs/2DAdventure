from .object import Object
from ..const import *

class Key(Object):
    def __init__(self, pos, size):
        super().__init__(pos, 'key', size)
        