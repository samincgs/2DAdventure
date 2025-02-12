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
        
        self.font = Font('data/fonts/small_font.png')
        
        self.assets = {}
        self.load_assets('data/images/tiles')
        
        self.tile_list = list(self.assets)
        
        self.scroll = [0, 0]
        self.movement = [False, False, False, False] # right, left, up, down
        
        self.clicked = False
        
        self.sidebar_surf = pygame.Surface((WIDTH / 6, HEIGHT))
                
    def load_assets(self, path):
        for dir in os.listdir(path):
            self.assets[dir] = load_dir(path + '/' + dir)    
            
    def run(self):
        while True:
            
            self.display.fill((0, 0, 0))
            self.sidebar_surf.fill((37, 54, 83))
            
            self.display.blit(self.sidebar_surf, (0, 0))
            
            # sidebar line
            pygame.draw.line(self.display, (255, 255, 255), (100, 0), (100, HEIGHT))
            
            pygame.draw.line(self.display, (255, 255, 255), (0, 80), (self.sidebar_surf.get_width(), 80))
            
            # self.scroll[0] += (self.player.rect.centerx - surf.get_width() // 2 - self.scroll[0]) 
            # self.scroll[1] += (self.player.rect.centery - surf.get_height() // 2 - self.scroll[1])
            # render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            for x, tiles in enumerate(self.tile_list):
                self.font.render(self.display, str(tiles), (2, 4 + x * 12))
            
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
                
                    
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
                        
if __name__ == "__main__":
    Editor().run()