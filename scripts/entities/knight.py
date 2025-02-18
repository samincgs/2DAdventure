import pygame
from .npc import NPC


class Knight(NPC):
    def __init__(self, game, pos, size, type):
        super().__init__(game, pos, size, type)
        self.images = self.game.assets.knight_imgs
        
        self.interact_range = 13
        self.can_turn = False
        
    def update(self, dt):
        pass