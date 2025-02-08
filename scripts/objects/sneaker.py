from .object import Object

class Sneaker(Object):
    def __init__(self, pos, size):
        super().__init__(pos, 'sneaker', size)
        