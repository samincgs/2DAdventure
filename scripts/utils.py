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
            if os.path.isfile(full_path):
                dir[file.split('.')[0]] = func(full_path)
        return dir
    
def blit_center(surf, img, pos, offset=(0, 0)):
    surf.blit(img, (pos[0] - img.get_width() // 2 - offset[0], pos[1] - img.get_height() // 2 - offset[1]))

def read_file(path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

def clip(surf, loc, size):
    main_surf = surf.copy()
    clipped_rect = pygame.Rect(loc[0], loc[1], size[0], size[1])
    main_surf.set_clip(clipped_rect)
    img = main_surf.subsurface(main_surf.get_clip())
    return img.copy()

def palette_swap(img, old_color, new_color):
    handle_img = img.copy()
    handle_img.fill(new_color)
    img.set_colorkey(old_color)
    handle_img.blit(img, (0, 0))
    return handle_img 



