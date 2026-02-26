import random

from scripts.entities.npc import NPC

class OldWizard(NPC):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.direction = random.choice(['up','left', 'right', 'down', 'down']) # additional chance to spawn looking downwards
        self.animation_timer = 0.25
        self.action_cooldown = 6
        self.movement_cooldown = 5
        self.keep_moving = 5.5
        
    def update(self, dt):
        if self.on_screen(self, self.game.camera.scroll, self.game.window.display): # check if self is on the screen
        
            movement = super().update(dt)
            
            if any(movement):
                self.movement_timer += dt
                if self.movement_timer > self.movement_cooldown:
                    self.pos[0] += movement[0]
                    self.pos[1] += movement[1]
                    if self.movement_timer > self.keep_moving:
                        self.movement_timer = 0
            
            if self.moving:
                self.animation_update(dt)  
                self.game.manager.cm.check_tile(self)
                self.game.manager.cm.check_entity(self, self.game.manager.em.player)
                
            