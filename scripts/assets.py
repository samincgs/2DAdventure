from .utils import load_dir, load_dir_list, load_sounds


class Assets:
    def __init__(self, path='data/images/'):
        self.path = path
        
        
        # self.player_imgs = load_dir(path + 'old_player')
        self.player = load_dir_list(path + 'player', alpha=True)
        self.npc = load_dir_list(path + 'npc', alpha=True)
        self.knight = load_dir_list(path + 'knight', alpha=True)
        self.slime = load_dir_list(path + 'slime', alpha=True)
        
        self.objects = load_dir(path + 'objects', alpha=True)
        
        
        
        
        self.sounds = load_sounds('data/sfx/')
        
                
        