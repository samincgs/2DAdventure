import random

from .npc import NPC

class OldWizard(NPC):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.images = self.game.assets.npc
        self.direction = random.choice(['up', 'left', 'right', 'down'])