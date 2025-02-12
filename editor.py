import pygame
import os
import sys

from editor.font import Font
from editor.utils import load_dir

WIDTH = 600
HEIGHT = 400
RENDER_SCALE = 2

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
        
        self.tile_list = self.assets[self.tile_names[self.tile_index]]
        
        self.scroll = [0, 0]
        self.movement = [False, False, False, False] # right, left, up, down
        
        self.current_tile = None
        
        self.mpos = None
        self.clicked = False
                
        self.sidebar_surf = pygame.Surface((WIDTH / 6, HEIGHT))
    def load_assets(self, path):
        for dir in os.listdir(path):
            self.assets[dir], self.tile_num = load_dir(path + '/' + dir, num=self.tile_num)    
            
    def run(self):
        while True:
            
            self.display.fill((0, 0, 0))
            self.sidebar_surf.fill((37, 54, 83))
            
            self.mpos = pygame.mouse.get_pos()
            self.mpos = (self.mpos[0] // RENDER_SCALE, self.mpos[1] // RENDER_SCALE)
            
            self.display.blit(self.sidebar_surf, (0, 0))
            
            # sidebar line
            pygame.draw.line(self.display, (255, 255, 255), (100, 0), (100, HEIGHT))
            pygame.draw.line(self.display, (255, 255, 255), (0, 80), (self.sidebar_surf.get_width(), 80))
            
            # self.scroll[0] += (self.player.rect.centerx - surf.get_width() // 2 - self.scroll[0]) 
            # self.scroll[1] += (self.player.rect.centery - surf.get_height() // 2 - self.scroll[1])
            # render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            # top left sidebar
            start_pos = 1
            for idx, tiles in enumerate(self.tile_names):
                x_offset = 0
                font_height = self.font.base_size[1]
                tile_rect = pygame.Rect(start_pos, 2 + idx * font_height, self.sidebar_surf.get_width(), font_height)
                if tile_rect.collidepoint(self.mpos):
                    x_offset = 3
                    if self.clicked:
                        self.tile_index = idx
                self.font.render(self.display, str(tiles), (start_pos + x_offset, 2 + idx * font_height))
            
            # bottom left sidebar
            self.tile_list = self.assets[self.tile_names[self.tile_index]]
            # TODO: fix the code (spaghetti)
            for idx, (num, tile_img) in enumerate(self.tile_list.items()):
                x_offset = 0
                y_offset = 0
                tile_img_pos =  (start_pos + x_offset, 80 + start_pos * 3 + (idx * 1.5 * tile_img.get_height()))
                if tile_img_pos[1] + tile_img.get_height() > self.sidebar_surf.get_height():
                    x_offset = tile_img.get_width() + 5
                    idx = idx % 13
                    tile_img_pos =  (start_pos + x_offset, 80 + start_pos * 3 + (idx * 1.5 * tile_img.get_height()))
                tile_rect = pygame.Rect(*tile_img_pos, *tile_img.get_size())
                if tile_rect.collidepoint(self.mpos):
                    y_offset = 2
                    if self.clicked:
                        self.current_tile = str(num)
                self.display.blit(tile_img, (tile_img_pos[0], tile_img_pos[1] - y_offset))
            
            if self.current_tile and self.mpos[0] > self.sidebar_surf.get_width():
                img = self.assets[self.tile_names[self.tile_index]][self.current_tile].copy()
                img.set_alpha(210)
                self.display.blit(img, (self.mpos[0] - img.get_width() / 2, self.mpos[1] - img.get_height() / 2))
            
            
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
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicked = False
                
                    
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
                        
if __name__ == "__main__":
    Editor().run()