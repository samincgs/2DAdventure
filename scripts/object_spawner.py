
from .objects.key import Key
from .objects.chest import Chest
from .objects.door import Door
from .objects.sneaker import Sneaker

class ObjectSpawner:
    def __init__(self, game):
        self.game = game
        
        self.objects = []
        
        self.spawn()
        
    def spawn(self):
        self.objects.append(Key(self.game, (368, 626), (8, 9)))
        self.objects.append(Key(self.game, (368, 112), (8, 9)))
        self.objects.append(Key(self.game, (612, 138), (8, 9)))
        self.objects.append(Door(self.game, (192, 354)))
        self.objects.append(Door(self.game, (128, 447)))
        self.objects.append(Door(self.game, (160, 175)))
        self.objects.append(Chest(self.game, (161, 112)))
        self.objects.append(Sneaker(self.game, (597, 675), (14, 8)))