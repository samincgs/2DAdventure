import pygame

from .font import Font
from .const import *

class UI:
    def __init__(self, game):
        self.game = game
        # self.font = Font(FONT_PATH + 'small_font.png')
        self.font = pygame.font.Font('data/fonts/roboto.ttf', 40)
        
        
    def render(self, surf):
        # self.font.render(surf, 'Keys: ' + str(self.game.player.has_keys), (5, 5))
        self.text = self.font.render('Keys: ' + str(self.game.player.has_keys), True, (255, 255, 255))
        surf.blit(self.text, (5, 5))