from .utils import load_dir, load_dir_list, load_sounds


class Assets:
    def __init__(self, path='data/images/'):
        self.path = path
        
        # self.player_imgs = load_dir(path + 'old_player')
        self.player = load_dir_list(path + 'player', alpha=True)
        self.npc_imgs = load_dir(path + 'npc')
        self.object_imgs = load_dir(path + 'objects')
        
        
        self.sounds = load_sounds('data/sfx/')
        
                
        