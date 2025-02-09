
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
        self.objects.append(Key(self.game, (384, 642), (8, 9)))
        self.objects.append(Key(self.game, (384, 128), (8, 9)))
        self.objects.append(Key(self.game, (628, 154), (8, 9)))
        self.objects.append(Door(self.game, (208, 370)))
        self.objects.append(Door(self.game, (144, 463)))
        self.objects.append(Door(self.game, (176, 191)))
        self.objects.append(Chest(self.game, (177, 128)))
        self.objects.append(Sneaker(self.game, (613, 675), (14, 8)))