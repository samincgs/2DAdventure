import pygame
from .utils import load_map_json, save_map_json, load_dir_list, outline

TILE_SIZE = 16

class TileManager:
    def __init__(self, game):
        self.game = game
        self.tile_size = TILE_SIZE
        
        self.tile_map = {} # '5;3: {'type': '', 'var}
        self.load_map('data/maps/test.json')
        
        self.tile_assets = load_dir_list('data/images/tiles')
        self.collision_rects = []
                                
    def get_nearby_tiles(self, pos):
        tiles = []
        tile_pos = [pos[0] // self.tile_size, pos[1] // self.tile_size]
        for offset in [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
            look_pos = (tile_pos[0] + offset[0], tile_pos[1] + offset[1])
            if look_pos in self.tile_positions:
                tiles.append(look_pos)
        return tiles
    
    def add_tile(self, tile_pos, tile_data):
        str_pos = str(tile_pos[0]) + ';' + str(tile_pos[1])
        self.tile_map[str_pos] = tile_data
        
    def remove_tile(self, tile_pos):
        str_pos = str(tile_pos[0]) + ';' + str(tile_pos[1])
        if str_pos in self.tile_map:
            del self.tile_map[str_pos]
    
    def load_map(self, path):
        tile_data = load_map_json(path)
        self.tile_map = tile_data['tilemap']
    
    def write_map(self, path, map_data):
        save_map_json(path, map_data)
    
    def remove_map(self):
        self.tile_map = {}
    
    def render(self, surf, offset=(0, 0), visible=False):
        if visible:
            pass
        else:
            for tile_loc in self.tile_map:
                tile = self.tile_map[tile_loc]
                img = self.tile_assets[tile['type']][tile['variant']].copy()
                loc = (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1])
                if tile['collision']:
                    rect = pygame.Rect(tile['pos'][0], tile['pos'][1], self.tile_size, self.tile_size)
                    if rect not in self.collision_rects:
                        self.collision_rects.append(rect)
                surf.blit(img, loc)
                
        # for col in self.collision_rects:
        #     pygame.draw.rect(surf, (255, 0, 0), pygame.Rect(col[0] - offset[0], col[1] - offset[1], col[2], col[3]), 1)
    
    def render_editor(self, surf, offset=(0, 0)): # assume new_tile_size is smaller than usual tile size
        for tile_loc in self.tile_map:
            tile = self.tile_map[tile_loc]
            img = self.tile_assets[tile['type']][tile['variant']].copy()
            loc = (tile['pos'][0] - offset[0], tile['pos'][1] - offset[1])
            if tile['collision']:
                outline(surf, img, loc, (255, 0, 0))
            surf.blit(img, loc)
                        
                    