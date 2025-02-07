import os
import pygame

from .tile import Tile
from ..const import *
from ..utils import load_img, read_file

class TileManager:
    def __init__(self, game):
        self.game = game
        self.tile_types = {} # different types of tiles
        self.tile_size = TILE_SIZE
        
        self.map_data = self.load_map('world_1')
        self.tile_types = self.load_tile_images()
        
        self.all_tiles = {}
        
    def get_nearby_tiles(self, pos):
        tiles = []
        tile_pos = [pos[0] // self.tile_size, pos[1] // self.tile_size]
        
        for offset in [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
            look_pos = (tile_pos[0] + offset[0], tile_pos[1] + offset[1])
            if look_pos in self.all_tiles:
                tiles.append(look_pos)
        return tiles
    
    def load_map(self, map_id):
        data = read_file(MAP_PATH + map_id + '.txt')
        data = data.replace(' ', '').split('\n')
        return [list(row) for row in data]
     
    def load_tile_images(self):
        tile_types = {}
        for variant in os.listdir(TILE_IMG_PATH):
            name = variant.split('.')[0]
            tile_types[name] = Tile()
            if name in COLLISION_TILES:
                tile_types[name].collision = True
            tile_types[name].img = load_img(TILE_IMG_PATH + variant, alpha=True)
        return tile_types
            
    def render(self, surf, offset=(0, 0), visible=True):
                
        if visible:
            for y in range(offset[1] // self.tile_size, (offset[1] + surf.get_height()) // self.tile_size + 1):
                for x in range(offset[0] // self.tile_size, (offset[0] + surf.get_width()) // self.tile_size + 1):
                    num = self.map_data[y - 1][x - 1]
                    tile = self.tile_types[TILE_VARIANTS[str(num)]]
                    if (x - 1 // self.tile_size, y -1 //self.tile_size) not in self.all_tiles:
                        if tile.collision:
                            self.all_tiles[(x - 1 // self.tile_size, y -1 //self.tile_size)] = tile
                    
                    surf.blit(tile.img, (x * self.tile_size - offset[0], y * self.tile_size - offset[1]))  
        else:
            for y, col in enumerate(self.map_data):
                for x, row in enumerate(col):
                    if row in TILE_VARIANTS:
                        img = self.tile_types[TILE_VARIANTS[row]].img
                        surf.blit(img, (x * self.tile_size - offset[0], y * self.tile_size - offset[1]))
                    
                    