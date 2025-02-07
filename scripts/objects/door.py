from .object import Object

class Door(Object):
    def __init__(self, pos):
        super().__init__(pos, 'door')
        self.collision_on = True
        