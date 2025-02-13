from .utils import load_sounds

class AudioManager:
    def __init__(self, path='data/sfx/', file_type='.mp3'):
        self.path = path
        self.file_type = file_type
        
        self.sounds = load_sounds(path=path)
        self.set_volumes()
    
    def set_volumes(self):
        self.sounds['coin'].set_volume(0.1)
