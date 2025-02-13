import pygame
import os
import sys
import tkinter as tk
from tkinter import filedialog

from editor.font import Font
from editor.utils import load_dir, load_map

WIDTH = 600
HEIGHT = 400
RENDER_SCALE = 2
SIDEBAR_WIDTH = 64 # 1 for the tiles to align properly

INITIAL_DIR = 'editor/data/maps'

class Editor:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((WIDTH * RENDER_SCALE, HEIGHT * RENDER_SCALE))
        pygame.display.set_caption('Level Editor')
        self.display = pygame.Surface((WIDTH, HEIGHT))
        
        self.font = Font('editor/data/fonts/small_font.png')
        
        self.assets = {}
        self.tile_num = 0
        self.load_assets('editor/data/images/tiles')
        
        
        self.tile_names = list(self.assets)
        self.tile_index = 0
        self.tile_size = 16
        
        self.tile_list = self.assets[self.tile_names[self.tile_index]]
        
        self.map_change = 0
        self.map_sizes = [10, 25, 50, 100]
        self.map_size = self.map_sizes[self.map_change]
        
        self.map = [[None for j in range(self.map_size)] for i in range(self.map_size)]
        
        self.scroll = [0, 0]
        self.movement = [False, False, False, False] # right, left, up, down
        
        self.current_tile = list(self.tile_list)[0] # placeholder first tile
        self.current_grid_pos = None
        
        self.current_map = None
        
        self.mpos = None
        self.clicked = False
        self.right_clicked = False
        
        self.grid_rects = {}
        
        
                
        self.sidebar_surf = pygame.Surface((SIDEBAR_WIDTH, HEIGHT))
    def load_assets(self, path):
        for dir in os.listdir(path):
            self.assets[dir], self.tile_num = load_dir(path + '/' + dir, num=self.tile_num)    
            
    def run(self):
        while True:
            
            self.display.fill((0, 0, 0))
            self.sidebar_surf.fill((37, 54, 83))
            
            self.scroll[0] += (self.movement[0] - self.movement[1]) * 2
            self.scroll[1] += (self.movement[3] - self.movement[2]) * 2
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            self.mpos = pygame.mouse.get_pos()
            self.mpos = (int(self.mpos[0] // RENDER_SCALE), int(self.mpos[1] // RENDER_SCALE))
            grid_pos = (int(self.mpos[0]) // self.tile_size, int(self.mpos[1]) // self.tile_size)
            scaled_pos = (int(grid_pos[0]) * self.tile_size, int(grid_pos[1]) * self.tile_size)
            
            self.display.blit(self.sidebar_surf, (0, 0))
            
            # sidebar line
            line_color = (79, 82, 119)
            pygame.draw.line(self.display, line_color, (SIDEBAR_WIDTH - 1, 0), (SIDEBAR_WIDTH - 1, HEIGHT))
            pygame.draw.line(self.display, line_color, (0, SIDEBAR_WIDTH), (self.sidebar_surf.get_width(), SIDEBAR_WIDTH))

            # top left sidebar
            start_pos = 1
            for idx, tiles in enumerate(self.tile_names):
                x_offset = 0
                font_height = self.font.base_size[1]
                tile_rect = pygame.Rect(start_pos, 2 + idx * font_height, self.sidebar_surf.get_width(), font_height)
                if tile_rect.collidepoint(self.mpos):
                    x_offset = 3
                    if self.clicked and self.tile_index != idx:
                        self.tile_index = idx
                        self.current_tile = list(self.assets[tiles])[0]
                self.font.render(self.display, str(tiles), (start_pos + x_offset, 2 + idx * font_height))
            
            # bottom left sidebar
            self.tile_list = self.assets[self.tile_names[self.tile_index]]
            index_limit = 14
            # TODO: fix the code (spaghetti)
            for idx, (num, tile_img) in enumerate(self.tile_list.items()):
                x_offset = 0
                y_offset = 0
                tile_img_pos =  (start_pos + x_offset, SIDEBAR_WIDTH + start_pos * 3 + (idx * 1.2 * tile_img.get_height()))
                if tile_img_pos[1] + tile_img.get_height() > self.sidebar_surf.get_height():
                    x_offset = tile_img.get_width() + 5
                    idx = idx % index_limit
                    tile_img_pos =  (start_pos + x_offset, SIDEBAR_WIDTH + start_pos * 3 + (idx * 1.2 * tile_img.get_height()))
                tile_rect = pygame.Rect(*tile_img_pos, *tile_img.get_size())
                if tile_rect.collidepoint(self.mpos):
                    y_offset = 2
                    if self.clicked:
                        self.current_tile = str(num)
                self.display.blit(tile_img, (tile_img_pos[0], tile_img_pos[1] - y_offset))
            
            # draw grid
            for row in range(self.map_size):
                for col in range(self.map_size):
                    rect = pygame.Rect(SIDEBAR_WIDTH + col * self.tile_size, row * self.tile_size, self.tile_size, self.tile_size)
                    if (row, col) not in self.grid_rects:
                        self.grid_rects[(row, col)] = rect
                    pygame.draw.line(self.display, (150, 150, 150), (SIDEBAR_WIDTH + col * self.tile_size, row * self.tile_size), (SIDEBAR_WIDTH + col * self.tile_size + 16, row * self.tile_size))
                    pygame.draw.line(self.display, (150, 150, 150), (SIDEBAR_WIDTH + col * self.tile_size, row * self.tile_size), (SIDEBAR_WIDTH + col * self.tile_size, row * self.tile_size + 16))
            
            # last lines
            pygame.draw.line(self.display, (150, 150, 150), (SIDEBAR_WIDTH + self.map_size * self.tile_size, 0), (SIDEBAR_WIDTH + self.map_size * self.tile_size, self.map_size * self.tile_size))
            pygame.draw.line(self.display, (150, 150, 150), (SIDEBAR_WIDTH, self.map_size * self.tile_size), (SIDEBAR_WIDTH + self.map_size * self.tile_size, self.map_size * self.tile_size))

            # display tiles
            for name in self.tile_names:
                for y, row in enumerate(self.map):
                    for x, col in enumerate(row):
                        if col is None:
                            continue
                        if col in self.assets[name]:
                            self.display.blit(self.assets[name][col], (SIDEBAR_WIDTH + x * self.tile_size, y * self.tile_size))   
            
            # show tile hover when placing blocks
            if self.current_tile:
                if self.mpos[0] > self.sidebar_surf.get_width():
                    img = self.assets[self.tile_names[self.tile_index]][self.current_tile].copy()
                    img.set_alpha(210)
                    self.display.blit(img, scaled_pos)
            
            # add and remove tiles from the map
            for coord, rect in self.grid_rects.items():
                if self.mpos[0] > SIDEBAR_WIDTH and rect.collidepoint(self.mpos):
                    self.current_grid_pos = coord
                    if self.clicked:
                        self.map[coord[0]][coord[1]] = self.current_tile
                    elif self.right_clicked:
                        self.map[coord[0]][coord[1]] = None
                        
                     
            # text ui
            selected_text ='selected: ' + str(self.current_tile) if self.current_tile else 'selected: None' 
            self.font.render(self.display, selected_text, (WIDTH - self.font.width(selected_text, extra_space=2), 1))
            
            col_text = 'col: ' + str(self.current_grid_pos[1]) if self.current_grid_pos else 'col: None'
            self.font.render(self.display, col_text, (WIDTH - self.font.width(col_text, extra_space=2), 11))
            
            row_text = 'row: ' + str(self.current_grid_pos[0]) if self.current_grid_pos else 'row: None'
            self.font.render(self.display, row_text, (WIDTH - self.font.width(row_text, extra_space=2), 21))
            
            map_text = 'map size: ' + str(self.map_size) + 'x' + str(self.map_size)
            self.font.render(self.display, map_text, (WIDTH - self.font.width(map_text, extra_space=16), HEIGHT - 22))
            
           
             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.movement[0] = True
                    if event.key == pygame.K_LEFT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.movement[2] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = True
                    if event.key == pygame.K_m: # change grid dimensions
                        self.map_change = (self.map_change + 1) % len(self.map_sizes)
                        self.map_size = self.map_sizes[self.map_change]
                        self.map = [[None for j in range(self.map_size)] for i in range(self.map_size)] # TODO: figure out how to keep the active drawing while changing maps
                    if event.key == pygame.K_i: # load a map
                        root = tk.Tk()
                        root.withdraw()
                        filename = filedialog.askopenfilename(initialdir=INITIAL_DIR, title='Select A Map', filetypes=[('txt files', '*.txt')])
                        self.current_map = load_map(filename)
                        filename.close()
                    if event.key == pygame.K_o: # save a map
                        root = tk.Tk()
                        root.withdraw()
                        filename = filedialog.asksaveasfile(defaultextension='.txt', initialdir=INITIAL_DIR, filetypes=[('txt files', '*.txt')], title='Save A Map')
                        if filename:
                            for col in self.map:
                                tile_num = " ".join(str(num) for num in col)
                                filename.write(tile_num + '\n')
                        filename.close()
                    if event.key == pygame.K_f:
                        for y, row in enumerate(self.map):
                            for x, col in enumerate(row):
                                self.map[y][x] = self.current_tile
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.movement[0] = False
                    if event.key == pygame.K_LEFT:
                        self.movement[1] = False
                    if event.key == pygame.K_UP:
                        self.movement[2] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[3] = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.clicked = True
                    if event.button == 3:
                        self.right_clicked = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicked = False
                    if event.button == 3:
                        self.right_clicked = False
                
                    
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
                        
if __name__ == "__main__":
    Editor().run()