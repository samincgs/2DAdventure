import random

from ..entity import Entity

class GreenSlime(Entity):
    def __init__(self, game, pos, size, type):        
        super().__init__(game, pos, size, type)
        
        self.images = self.game.assets.slime
        self.direction = random.choice(['up','left', 'right', 'down'])
        self.speed = 20
        self.max_health = 4
        self.health = self.max_health
        
        self.animation_timer = 0.15
        self.action_cooldown = 3
        
        self.damage_amt = 1
    
    def set_action(self, dt):
        super().set_action(dt)
        
    def update(self, dt):
        self.animation_update(dt)
        
        movement = super().update(dt)
        self.pos[0] += movement[0]
        self.pos[1] += movement[1]
        
        if self.last_movement != self.pos:
            self.game.collision_manager.check_tile(self)
        
        if self.on_screen(self, self.game.scroll, self.game.window.display): # check if self is on the screen
            for entity in self.game.entities:
                if entity.type != self.type and self.on_screen(entity, self.game.scroll, self.game.window.display):
                    collided = self.game.collision_manager.check_entity(self, entity)
                    if collided and collided.type == 'player':
                        collided.damage(self.damage_amt)