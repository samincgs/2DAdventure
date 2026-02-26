from scripts.objects.object import Object

class Chest(Object):
    def __init__(self, game, pos):
        super().__init__(game, pos, 'chest3')
        self.collision_on = True
        