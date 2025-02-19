from ..entity import Entity

class GreenSlime(Entity):
    def __init__(self, game, pos, size, type):        
        super().__init__(game, pos, size, type)
        
        self.images = self.game.assets.slime
        self.speed = 20
        self.max_health = 4
        self.health = self.max_health
        
    def update(self, dt):
        pass