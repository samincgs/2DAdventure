from .object import Object

class Sword(Object):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, 'sword', size)
        