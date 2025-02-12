import os

from .tile import Tile
from ..const import *
from ..utils import read_file

class TileManager:
    def __init__(self, game):
        self.game = game
        self.tile_size = TILE_SIZE
        
        self.tile_types = {} # different types of tiles
        self.tile_positions = [] # all tile positions on camera screen
        
        self.map_data = self.load_map('world_2')
        self.tile_types = self.load_tile_images()
        
    def get_nearby_tiles(self, pos):
        tiles = []
        tile_pos = [pos[0] // self.tile_size, pos[1] // self.tile_size]
        for offset in [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
            look_pos = (tile_pos[0] + offset[0], tile_pos[1] + offset[1])
            if look_pos in self.tile_positions:
                tiles.append(look_pos)
        return tiles
    
    def load_map(self, map_id):
        data = read_file(MAP_PATH + map_id + '.txt')
        data = data.split('\n')
        return [row.split() for row in data]
     
    def load_tile_images(self):
        tile_types = {}
        for variant in os.listdir(TILE_IMG_PATH):
            name = variant.split('.')[0]
            tile_types[name] = Tile()
            if name in COLLISION_TILES:
                tile_types[name].collision = True
            tile_types[name].img = self.game.assets.tile_imgs[name]

        for variant in os.listdir(WATER_IMG_PATH):
            name = variant.split('.')[0]
            tile_types[name] = Tile()
            tile_type = name.split('_')[0]
            if tile_type in COLLISION_TILES:
                tile_types[name].collision = True   
            tile_types[name].img = self.game.assets.water_imgs[name]              
        return tile_types
            
    def render(self, surf, offset=(0, 0), visible=True):
        if visible:
            for y in range(max(0, offset[1] // self.tile_size), min(WORLD_DIMENSION - 1, (offset[1] + surf.get_height()) // self.tile_size) + 1):
                for x in range(max(0, offset[0] // self.tile_size), min(WORLD_DIMENSION - 1, (offset[0] + surf.get_width()) // self.tile_size) + 1):
                    num = self.map_data[y][x]
                    tile = self.tile_types[TILE_VARIANTS[str(num)]]
                    tile_pos = (x, y)
                    if tile_pos not in self.tile_positions and tile.collision:
                        self.tile_positions.append(tile_pos)
                    surf.blit(tile.img, (x * self.tile_size - offset[0], y * self.tile_size - offset[1]))  
        else:
            for y, col in enumerate(self.map_data): # render whole map (only efficient when the number tiles is less than screen size )
                for x, row in enumerate(col):
                    if row in TILE_VARIANTS:
                        img = self.tile_types[TILE_VARIANTS[row]].img
                        surf.blit(img, (x * self.tile_size - offset[0], y * self.tile_size - offset[1]))
                        
                    