import random

from ..entity import Entity

class GreenSlime(Entity):
    def __init__(self, game, pos, size, type):        
        super().__init__(game, pos, size, type)
        
        self.images = self.game.assets.slime
        self.direction = random.choice(['up','left', 'right', 'down'])
        self.speed = 16
        self.max_health = 4
        self.health = self.max_health
        
        self.animation_timer = 0.15
        self.action_cooldown = 3
        self.invincible_time = 0.85
        self.alpha = 50
        
        self.damage_amt = 3
        self.exp = 2
        
        self.hp_bar_cooldown = 10
        
        self.death_message_shown = False
    
    @property
    def attack_value(self):
        return self.damage_amt
    
    def set_action(self, dt):
        super().set_action(dt)
    
    def update(self, dt):
        
        dead = self.check_death(dt)
        
        self.animation_update(dt)
        
        if self.hp_bar_on:
            self.hp_bar_counter += dt
            if self.hp_bar_counter >= self.hp_bar_cooldown:
                self.hp_bar_on = False
                self.hp_bar_counter = 0
        
        if self.on_screen(self, self.game.scroll, self.game.window.display): # check if self is on the screen
            movement = super().update(dt)
            self.pos[0] += movement[0]
            self.pos[1] += movement[1]
            if self.last_movement != self.pos:
                self.game.collision_manager.check_tile(self)
            
            for entity in self.game.entities:
                if entity.type != self.type and self.on_screen(entity, self.game.scroll, self.game.window.display):
                    collided = self.game.collision_manager.check_entity(self, entity)
                    if collided and collided.type == 'player': # collide with player
                        collided.damage(self.damage_amt)
                        
        self.reset_invincible(dt)
        
        return dead
        