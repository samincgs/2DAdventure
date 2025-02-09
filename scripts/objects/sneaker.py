from .object import Object

class Sneaker(Object):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, 'sneaker', size)
        