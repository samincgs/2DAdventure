from .object import Object

class Boots(Object):
    def __init__(self, pos, size):
        super().__init__(pos, 'boots', size)
        