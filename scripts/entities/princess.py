from scripts.entities.npc import NPC

class Princess(NPC):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.blocked = False

    def follow_player(self, player):
        distance_to_player = self.get_distance(player)
        if distance_to_player <= 35:
            if player.moving:
                self.direction = player.direction
                self.pos[0] += (player.pos[0] - self.pos[0]) / 13
                self.pos[1] += (player.pos[1] - self.pos[1]) / 13
                if self.direction == 'up':
                    self.pos[1] += (player.pos[1] - self.pos[1]) / 5
    
    def update(self, dt):
        pass
        
        
        