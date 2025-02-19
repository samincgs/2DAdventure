import random

from .npc import NPC

class OldWizard(NPC):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.direction = random.choice(['up','left', 'right', 'down', 'down'])
        self.animation_timer = 0.25
        self.action_cooldown = 4