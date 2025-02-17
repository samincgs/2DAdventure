from .utils import load_dir, load_sounds


class Assets:
    def __init__(self, path='data/images/'):
        self.path = path
        
        self.player_imgs = load_dir(path + 'player')
        self.npc_imgs = load_dir(path + 'npc')
        self.object_imgs = load_dir(path + 'objects')
        
        print(self.player_imgs)
        
        self.sounds = load_sounds('data/sfx/')
        
                
        