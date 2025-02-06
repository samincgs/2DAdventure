import pygame

def load_img(path, colorkey=None, alpha=True):
    img = pygame.image.load(path).convert() if not alpha else pygame.image.load(path).convert_alpha()
    if colorkey:
        img.set_colorkey(colorkey)
    return img

def read_file(path):
    f = open(path, 'r')
    data = f.read()
    f.close()
    return data
