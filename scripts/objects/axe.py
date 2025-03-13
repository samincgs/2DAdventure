from .object import Object

class Axe(Object):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, 'axe', size)
        self.item_description = '[ Axe ]\n\nA flimsy axe that still\nseems to get the job done.'
        self.is_weapon = True
        
    @property
    def img(self): # image is instead the animation for player sword swing
        img = self.player.images['attack' + '_' + self.player.direction][self.player.attack_index]
        return img
    
    @property
    def ui_img(self):
        return self.game.assets.objects[self.type]