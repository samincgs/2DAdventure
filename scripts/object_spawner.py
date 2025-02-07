
from .objects.key import Key

class ObjectSpawner:
    def __init__(self, game):
        self.game = game
        
        self.spawn()
        
    
    def spawn(self):
        self.game.objects.append(Key((384, 642), 'key', (5, 9)))
        self.game.objects.append(Key((384, 128), 'key', (5, 9)))