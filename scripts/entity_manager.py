from .entities.player import Player
from .entities.old_wizard import OldWizard
from .entities.knight import Knight
from .monsters.green_slime import GreenSlime
from .objects.sword import Sword
from .objects.axe import Axe


class EntityManager:
    def __init__(self, game):
        self.game = game
        self.entities = []
        
        self.load_entities()
        
    def spawn_enemies(self):
        # reset monsters if they alr exist
        self.entities = [entity for entity in self.entities if not entity.is_monster]
        
        # monsters
        self.entities.append(GreenSlime(self.game, (636, 348), (11, 10), 'green_slime')) 
        self.entities.append(GreenSlime(self.game, (650, 363), (11, 10), 'green_slime')) 
        self.entities.append(GreenSlime(self.game, (610, 358), (11, 10), 'green_slime')) 
        self.entities.append(GreenSlime(self.game, (688, -176), (11, 10), 'green_slime')) 
        
    def load_entities(self):
        self.entities.append(Player(self.game, (326, 165), (8,8), 'player'))
        self.player = self.entities[-1]
        self.player.inventory.append(Sword(self.game, (0, 0), (16, 16), self.player))
        self.player.inventory.append(Axe(self.game, (0, 0), (16, 16), self.player))
        self.player.weapon = self.player.inventory[0]
         
        #npcs
        self.entities.append(OldWizard(self.game, (275, 150), (14, 10), 'old_wizard'))
        self.entities.append(Knight(self.game, (404, 367), (12, 14), 'knight'))
        
        # monsters
        self.spawn_enemies()
        
    def update(self, dt):
        for entity in self.entities.copy():
            kill = entity.update(dt)
            if kill:
                self.entities.remove(entity)
                self.player.check_level_up()
    
    
    def render(self, surf, offset=(0, 0), ysort=True):
        if ysort:
            for entity in sorted(self.entities, key=lambda x: x.pos[1]): # sprite ordering
                entity.render(surf, offset=offset)
        else:
            for entity in self.entities: # sprite ordering
                entity.render(surf, offset=offset)