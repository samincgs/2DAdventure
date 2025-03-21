from .objects.axe import Axe
from .objects.potion import HealthPotion
from .objects.key import Key
from .objects.boomerang import Boomerang


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
        
        self.objects.append(HealthPotion(self.game, (400, 162), (16, 16)))
        self.objects.append(Axe(self.game, (212, 170), (16, 16), self.game.player))
        self.objects.append(Boomerang(self.game, (122, 170), (16, 16), self.game.player))
        
    def render(self, surf, offset=(0, 0)):
        for obj in self.objects:
            obj.render(surf, offset=offset)
        
        
        