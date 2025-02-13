import pygame
import os
import sys
import tkinter as tk
from tkinter import filedialog

from editor.font import Font
from editor.tile_manager import TileManager, TILE_SIZE
from editor.utils import load_map_txt

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
        
        self.tile_manager = TileManager(self)
        self.font = Font('editor/data/fonts/small_font.png')
      
        self.assets = self.tile_manager.tile_assets
        
        self.tile_names = list(self.assets)
        self.tile_group = 0 # for names of tiles
        self.tile_index = 0 # for num of variant
        self.tile_size = TILE_SIZE
                
        self.map_sizes = [10, 25, 50, 100]
        self.map_change = 0
        self.map_size = self.map_sizes[self.map_change]
        
        # self.clear_map()
        
        self.scroll = [0, 0]
        self.movement = [False, False, False, False] # right, left, up, down
        
        self.current_tile = self.assets[self.tile_names[self.tile_group]][self.tile_index] # placeholder first tile
        self.current_grid_pos = None
        
        self.collision_on = False
        
        self.mpos = None
        self.clicked = False
        self.right_clicked = False
        
        self.current_file = None
        self.grid_rects = {}
        
        self.sidebar_surf = pygame.Surface((SIDEBAR_WIDTH, HEIGHT))
  
    def clear_map(self):
        self.map = [[None for j in range(self.map_size)] for i in range(self.map_size)]
    
    def map_reset(self):
        self.map_size = self.map_sizes[self.map_change]
        self.clear_map() # TODO: figure out how to keep the active drawing while changing maps
        self.current_grid_pos = None
        self.grid_rects = {}
         
    def run(self):
        while True:
            
            self.display.fill((0, 0, 0))
            self.sidebar_surf.fill((37, 54, 83))
            
            self.scroll[0] += (self.movement[0] - self.movement[1]) * 2
            self.scroll[1] += (self.movement[3] - self.movement[2]) * 2
            
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
            for idx, tile_name in enumerate(self.tile_names):
                x_offset = 0
                font_height = self.font.base_size[1]
                tile_rect = pygame.Rect(start_pos, 2 + idx * font_height, self.sidebar_surf.get_width(), font_height)
                if tile_rect.collidepoint(self.mpos):
                    x_offset = 3
                    if self.clicked and self.tile_group != idx:
                        self.tile_group = idx
                        self.tile_index = 0
                self.font.render(self.display, str(tile_name), (start_pos + x_offset, 2 + idx * font_height))
            
            # # bottom left sidebar
            self.tile_list = self.assets[self.tile_names[self.tile_group]]
            # index_limit = 14
            # TODO: fix the code (spaghetti)
            for idx, tile_img in enumerate(self.tile_list):
                x_offset = 0
                y_offset = 0
                tile_img_pos =  (start_pos + x_offset, SIDEBAR_WIDTH + start_pos * 3 + (idx * 1.2 * tile_img.get_height()))
                if tile_img_pos[1] + tile_img.get_height() > self.sidebar_surf.get_height():
                    x_offset = tile_img.get_width() + 5
                    tile_img_pos =  (start_pos + x_offset, SIDEBAR_WIDTH + start_pos * 3 + (idx * 1.2 * tile_img.get_height()))
                tile_rect = pygame.Rect(*tile_img_pos, *tile_img.get_size())
                if tile_rect.collidepoint(self.mpos):
                    y_offset = 2
                    if self.clicked:
                        self.tile_index = idx
                self.display.blit(tile_img, (tile_img_pos[0], tile_img_pos[1] - y_offset))
            
            
            # # display tiles
            # for name in self.tile_names:
            #     for y, row in enumerate(self.map):
            #         for x, col in enumerate(row):
            #             if col is None:
            #                 continue
            #             if col in self.assets[name]:
            #                 self.display.blit(self.assets[name][col], (SIDEBAR_WIDTH + x * self.tile_size, y * self.tile_size))   
            
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
            
            # # show tile hover when placing blocks
            if self.mpos[0] > self.sidebar_surf.get_width():
                img = self.assets[self.tile_names[self.tile_group]][self.tile_index].copy()
                img.set_alpha(210)
                self.display.blit(img, scaled_pos)
            
            # add and remove tiles from the map
            for coord, rect in self.grid_rects.items():
                if self.mpos[0] > SIDEBAR_WIDTH and rect.collidepoint(self.mpos):
                    self.current_grid_pos = coord
                    # TODO
                        
            # # text ui
            text_height = 5
            
            file_text = 'file: ' + str(self.current_file) if self.current_file else 'file: None'
            self.font.render(self.display, file_text, (WIDTH - self.font.width(file_text, extra_space=3), text_height))
            text_height += 10
            
            map_text = 'map size: ' + str(self.map_size) + 'x' + str(self.map_size)
            self.font.render(self.display, map_text, (WIDTH - self.font.width(map_text, extra_space=3), text_height))
            text_height += 10
            
            # selected_text ='selected: ' + str(self.current_tile) if self.current_tile else 'selected: None' 
            # self.font.render(self.display, selected_text, (WIDTH - self.font.width(selected_text, extra_space=3), text_height))
            # text_height += 10
            
            col_text = 'col: ' + str(self.current_grid_pos[1]) if self.current_grid_pos else 'col: None'
            self.font.render(self.display, col_text, (WIDTH - self.font.width(col_text, extra_space=3), text_height))
            text_height += 10
            
            row_text = 'row: ' + str(self.current_grid_pos[0]) if self.current_grid_pos else 'row: None'
            self.font.render(self.display, row_text, (WIDTH - self.font.width(row_text, extra_space=3), text_height))
            text_height += 10
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_d:
                        self.movement[0] = True
                    if event.key == pygame.K_a:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                    if event.key == pygame.K_c:
                        self.collision_on = not self.collision_on
                    if event.key == pygame.K_m: # change grid dimensions
                        self.map_change = (self.map_change + 1) % len(self.map_sizes)
                        self.map_reset()
                    # if event.key == pygame.K_i: # load a map
                    #     root = tk.Tk()
                    #     root.withdraw()
                    #     filename = filedialog.askopenfilename(initialdir=INITIAL_DIR, title='Select A Map', filetypes=[('txt files', '*.txt')])
                    #     self.map = load_map(filename)
                    #     self.map_size = len(self.map) - 1
                    # if event.key == pygame.K_o: # save a map
                    #     root = tk.Tk()
                    #     root.withdraw()
                    #     filename = filedialog.asksaveasfile(defaultextension='.txt', initialdir=INITIAL_DIR, filetypes=[('txt files', '*.txt')], title='Save A Map')
                    #     if filename:
                    #         for col in self.map:
                    #             tile_num = " ".join(str(num) for num in col)
                    #             filename.write(tile_num + '\n')
                    #     filename.close()
                    # if event.key == pygame.K_f:
                    #     for y, row in enumerate(self.map):
                    #         for x, col in enumerate(row):
                    #             self.map[y][x] = self.current_tile
                    # if event.key == pygame.K_x:
                    #     self.map = self.clear_map()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.movement[0] = False
                    if event.key == pygame.K_a:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
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