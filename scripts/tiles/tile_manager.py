import os

from .tile import Tile
from ..const import *
from ..utils import load_img, read_file

class TileManager:
    def __init__(self, game):
        self.game = game
        self.tile_types = {} # different types of tiles
        
        self.map_data = self.load_map('map_1')
        self.tile_types = self.load_tile_images()
        
        
    def load_map(self, map_id):
        data = read_file(MAP_PATH + map_id + '.txt')
        data = data.split('\n')
        return [list(row) for row in data]
     
    def load_tile_images(self):
        tile_types = {}
        for variant in os.listdir(TILE_IMG_PATH):
            name = variant.split('.')[0]
            tile_types[name] = Tile()
            tile_types[name].img = load_img(TILE_IMG_PATH + variant)
        return tile_types
            
    def render(self, surf):
        for y, col in enumerate(self.map_data):
            for x, row in enumerate(col):
                if row in TILE_VARIANTS:
                    img = self.tile_types[TILE_VARIANTS[row]].img
                    surf.blit(img, (x * TILE_SIZE, y * TILE_SIZE))
            