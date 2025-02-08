import pygame
import os

def load_img(path, colorkey=None, alpha=True):
    img = pygame.image.load(path).convert() if not alpha else pygame.image.load(path).convert_alpha()
    if colorkey:
        img.set_colorkey(colorkey)
    return img

def load_dir(path, func):
        dir = {}
        for file in os.listdir(path):
            full_path = path + '/' + file
            dir[file.split('.')[0]] = func(full_path)
        return dir
    
def blit_center(surf, img, pos, offset=(0, 0)):
    surf.blit(img, (pos[0] - img.get_width() // 2 - offset[0], pos[1] - img.get_height() // 2 - offset[1]))

def read_file(path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data
