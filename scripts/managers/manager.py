from scripts.managers.entity_manager import EntityManager
from scripts.managers.tile_manager import TileManager
from scripts.managers.collision_manager import CollisionManager
from scripts.object_mapper import ObjectMapper
from scripts.events import Events

class Manager:
    def __init__(self, game):
        self.em = EntityManager(game)
        self.tm = TileManager(game)
        self.cm = CollisionManager(game, self.tm)
        self.om = ObjectMapper(game, self.em)
        self.events = Events(game, self.cm, self.em)
        
    def render(self, surf, offset):
        self.tm.render_visible(surf, offset=offset) # fix y sort when user is behind the tree
        self.om.render(surf, offset=offset)
        self.em.render(surf, offset=offset, ysort=True)