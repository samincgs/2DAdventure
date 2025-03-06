from .objects.key import Key

class ObjectMapper:
    def __init__(self, game):
        self.game = game
        self.objects = []
        self.setup()
        
    def setup(self):
        
        # KEYS
        self.objects.append(Key(self.game, (352, 144), (16, 16)))
        self.objects.append(Key(self.game, (288, 176), (16, 16)))
        self.objects.append(Key(self.game, (320, 224), (16, 16)))
        
    def render(self, surf, offset=(0, 0)):
        for obj in self.objects:
            obj.render(surf, offset=offset)
        
        
        