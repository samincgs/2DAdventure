
from .objects.key import Key

class ObjectSpawner:
    def __init__(self, game):
        self.game = game
        
    
    def spawn(self):
        self.game.objects.append(Key((384, 642), 'key'))
        self.game.objects.append(Key((384, 128), 'key'))