
from .objects.key import Key
from .objects.chest import Chest
from .objects.door import Door

class ObjectSpawner:
    def __init__(self, game):
        self.game = game
        
        self.spawn()
        
    def spawn(self):
        self.game.objects.append(Key((384, 642), (8, 9)))
        self.game.objects.append(Key((384, 128), (8, 9)))
        self.game.objects.append(Door((208, 370)))
        self.game.objects.append(Door((144, 463)))
        self.game.objects.append(Door((176, 191)))
        self.game.objects.append(Chest((177, 128)))
        self.game.objects.append(Chest((177, 128)))