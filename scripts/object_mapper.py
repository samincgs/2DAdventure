from scripts.objects.axe import Axe
from scripts.objects.potion import HealthPotion
from scripts.objects.key import Key
from scripts.objects.boomerang import Boomerang


class ObjectMapper:
    def __init__(self, game, em):
        self.game = game
        self.em = em
        
        self.objects = []
        self.load_objects()
        
    def load_objects(self):
        
        # KEYS
        self.objects.append(Key(self.game, (352, 144), (16, 16)))
        self.objects.append(Key(self.game, (288, 176), (16, 16)))
        self.objects.append(Key(self.game, (320, 224), (16, 16)))
        
        self.objects.append(HealthPotion(self.game, (400, 162), (16, 16)))
        self.objects.append(Axe(self.game, (212, 170), (16, 16), self.em.player))
        
    def render(self, surf, offset=(0, 0)):
        for obj in self.objects:
            obj.render(surf, offset=offset)
        
        
        