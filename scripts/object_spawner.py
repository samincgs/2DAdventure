
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
        pass