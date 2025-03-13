from .object import Object

class Sneaker(Object):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, 'sneaker', size)
        self.item_description = '[ Sneaker ]\n\nShoes that allow you to\nmove faster for a short\nduration.'
        