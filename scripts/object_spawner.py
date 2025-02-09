
from .objects.key import Key
from .objects.chest import Chest
from .objects.door import Door
from .objects.sneaker import Sneaker


class ObjectSpawner:
    def __init__(self, game):
        self.game = game
        
        self.spawn()
        
    def spawn(self):
        self.game.objects.append(Key((384, 642), (8, 9)))
        self.game.objects.append(Key((384, 128), (8, 9)))
        self.game.objects.append(Key((628, 154), (8, 9)))
        self.game.objects.append(Door((208, 370)))
        self.game.objects.append(Door((144, 463)))
        self.game.objects.append(Door((176, 191)))
        self.game.objects.append(Chest((177, 128)))
        self.game.objects.append(Sneaker((613, 675), (14, 8)))