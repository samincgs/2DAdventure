from .object import Object

class Key(Object):
    def __init__(self, pos, size):
        super().__init__(pos, 'key', size)
        