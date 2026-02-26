from scripts.entities.npc import NPC

class Knight(NPC):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)        
        self.interact_range = 13
        self.can_turn = False
        self.can_move = False
        
    def update(self, dt):
        pass
        
    