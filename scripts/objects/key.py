from .object import Object

class Key(Object):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, 'key', size)
        