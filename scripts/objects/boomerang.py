
from scripts.objects.object import Object

class Boomerang(Object):
    def __init__(self, game, pos, size, player):
        super().__init__(game, pos, 'boomerang', size)
        self.player = player
        self.item_description = "[ Blue Boomerang ]\n\nA cool looking boomerang\nthat feels amazing to throw."
        self.damage_amt = 1
        self.is_weapon = True
        self.animation_timer = [0, 0.65]
        self.attack_delay = 0.18
        
        self.speed = 100
        self.total_time = 1.2
        self.timer = 0
        
        self.rotation = 0
        
    @property
    def img(self):
        return self.game.assets.objects[self.type]
    
    @property
    def attack_img(self): # image is instead the animation for player sword swing
        pass
    
    def use(self):
        self.pos = self.player.pos.copy()
        self.rotation = 0
        self.timer = 0
    
    def update(self, dt):
        self.timer += dt

    def render(self, surf, offset=(0, 0)):
        pass
    
    
    