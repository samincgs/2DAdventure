import pygame
import os
import json

# load pygame image
def load_img(path, colorkey=None, alpha=False):
    img = pygame.image.load(path).convert_alpha() if alpha else pygame.image.load(path).convert()
    if colorkey:
        img.set_colorkey(colorkey)
    return img

# load a directory of imgs in a list
def load_imgs(path, colorkey=None, alpha=False):
    tiles = []
    for file in sorted(os.listdir(path)):
        img = load_img(path + '/' + file, alpha=True)
        tiles.append(img)
    return tiles

# load a directory of images into a dictionary
def load_dir(path, colorkey=None, alpha=False):
    tiles = {}
    for file in sorted(os.listdir(path)):
        name = file.split('.')[0]
        img = load_img(path + '/' + file, alpha=True)
        tiles[name] = img
    return tiles

# load multiple directories into a dict with lists of images
def load_dir_list(path):
    image_dir = {}
    for folder in os.listdir(path):
        image_dir[folder] = []
        for img in os.listdir(path + '/' + folder):
            image_dir[folder].append(load_img(os.path.join(path, folder, img)))                                       
    return image_dir

def load_map_json(path):
    f = open(path)
    map_data = json.load(fp=f)
    f.close()
    return map_data

def save_map_json(path, data):
    f = open(path, 'w')
    json.dump(data, fp=f)
    f.close()

# load a text file into a 2D list of numbers (can be string or int)
def load_map_txt(path, ints=False):
    map = []
    data = read_file(path)
    data = data.split('\n')
    for row in data:
        if not ints:
            map.append(row.split())
        else:
           map.append([int(num) for num in row.split()])
    return map

# read a text file
def read_file(path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data

# create a smaller subsurface of a bigger surface
def clip(surf, loc, size):
    main_surf = surf.copy()
    clipped_rect = pygame.Rect(loc[0], loc[1], size[0], size[1])
    main_surf.set_clip(clipped_rect)
    img = main_surf.subsurface(main_surf.get_clip())
    return img.copy()

# do a color swap, between an old and new color
def palette_swap(img, old_color, new_color):
    handle_img = img.copy()
    handle_img.fill(new_color)
    img.set_colorkey(old_color)
    handle_img.blit(img, (0, 0))
    return handle_img 

def outline(surf, img, loc, color=(255, 255, 255)):
    mask_img = pygame.mask.from_surface(img)
    mask_img = mask_img.to_surface(setcolor=color, unsetcolor=(0, 0, 0, 0))
    for offset in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        surf.blit(mask_img, (loc[0] + offset[0], loc[1] + offset[1]))