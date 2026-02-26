from scripts.managers.entity_manager import EntityManager
from scripts.managers.tile_manager import TileManager
from scripts.managers.collision_manager import CollisionManager

class Manager:
    def __init__(self, game):
        self.em = EntityManager(game)
        self.tm = TileManager(game)
        self.cm = CollisionManager(game, self.tm)