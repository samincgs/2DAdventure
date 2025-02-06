import os

from .tile import Tile
from ..const import *
from ..utils import load_img

class TileManager:
    def __init__(self, game):
        self.game = game
        self.tile = [] # different types of tiles
        
        for variant in os.listdir(TILE_IMG_PATH):
            self.tile.append(Tile())
            self.tile[-1].img = load_img(TILE_IMG_PATH + variant)
            
    def render(self, surf):
        surf.blit(self.tile[0].img, (0, 0))
            