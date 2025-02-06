import pygame

def load_img(path, colorkey=None, alpha=True):
    img = pygame.image.load(path).convert() if not alpha else pygame.image.load(path).convert_alpha()
    if colorkey:
        img.set_colorkey(colorkey)
    return img