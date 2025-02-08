import pygame
from .utils import load_dir

class AudioManager:
    def __init__(self, path='data/sfx/', file_type='.mp3'):
        self.path = path
        self.file_type = file_type
        
        self.sounds = load_dir(path=path, func=self.load_sound)
        self.set_volumes()
    
    def set_volumes(self):
        self.sounds['coin'].set_volume(0.1)
    
    def load_sound(self, path):
        return pygame.mixer.Sound(path)