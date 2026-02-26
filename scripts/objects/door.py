from scripts.objects.object import Object

class Door(Object):
    def __init__(self, game, pos):
        super().__init__(game, pos, 'door')
        self.collision_on = True
        