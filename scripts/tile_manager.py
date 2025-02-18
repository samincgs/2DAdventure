import pygame

from .utils import load_json, save_json, load_dir_list, outline

TILE_SIZE = 16

class TileManager:
    def __init__(self, game):
        self.game = game
        self.tile_size = TILE_SIZE
        self.tile_assets = load_dir_list('data/images/tiles')
        
        self.tile_map = {} # '5;3: {'type': '', 'var}
                             
    def get_nearby_rects(self, pos):
        rects = []
        tile_pos = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        check_locs = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        for loc in check_locs:
            tile_loc = [tile_pos[0] + loc[0], tile_pos[1] + loc[1]]
            for str_loc in self.tile_map:
                if tile_loc == self.tile_map[str_loc]['tile_pos'] and self.tile_map[str_loc]['collision']:
                    rects.append(pygame.Rect(tile_loc[0] * self.tile_size, tile_loc[1] * self.tile_size, self.tile_size, self.tile_size))
        return rects
    
    def add_tile(self, tile_pos, tile_data):
        str_pos = str(tile_pos[0]) + ';' + str(tile_pos[1])
        self.tile_map[str_pos] = tile_data
        
    def remove_tile(self, tile_pos):
        str_pos = str(tile_pos[0]) + ';' + str(tile_pos[1])
        if str_pos in self.tile_map:
            del self.tile_map[str_pos]
    
    def load_map(self, path):
        tile_data = load_json(path)
        self.tile_map = tile_data['tilemap']
    
    def write_map(self, path, map_data):
        save_json(path, map_data)
    
    def remove_map(self):
        self.tile_map = {}
    
    def render_visible(self, surf, offset=(0, 0)):
        for x in range(offset[0] // self.tile_size, ((offset[0] + surf.get_width()) // self.tile_size) + 1):
            for y in range(offset[1] // self.tile_size, ((offset[1] + surf.get_height()) // self.tile_size) + 1):
                loc = str(x * self.tile_size) + ';' + str(y * self.tile_size)
                if loc in self.tile_map:
                    tile = self.tile_map[loc]
                    img = self.tile_assets[tile['type']][tile['variant']]
                    loc = (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1])
                    surf.blit(img, loc)
                
    def render_all(self, surf, offset=(0, 0)):
         for tile_loc in self.tile_map:
            tile = self.tile_map[tile_loc]
            img = self.tile_assets[tile['type']][tile['variant']].copy()
            loc = (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1])
            surf.blit(img, loc)
                
    def render_editor(self, surf, offset=(0, 0)): # assume new_tile_size is smaller than usual tile size
        for tile_loc in self.tile_map:
            tile = self.tile_map[tile_loc]
            img = self.tile_assets[tile['type']][tile['variant']].copy()
            loc = (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1])
            if tile['collision']:
                outline(surf, img, loc, (255, 0, 0))
            surf.blit(img, loc)
                        
                    