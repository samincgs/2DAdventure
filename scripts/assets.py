from scripts.utils import load_dir, load_dir_list, load_sounds


class Assets:
    def __init__(self, path='data/images/'):
        self.path = path
        
        entity_path = path + 'entities/'
        alpha=True
        
        # entities
        self.player = load_dir_list(entity_path + 'player', alpha=alpha)
        self.old_wizard = load_dir_list(entity_path + 'old_wizard', alpha=alpha)
        self.knight = load_dir_list(entity_path + 'knight', alpha=alpha)
        self.princess = load_dir_list(entity_path + 'princess', alpha=alpha)
        self.slime = load_dir_list(entity_path + 'slime', alpha=alpha)
        
        # objects
        self.objects = load_dir(path + 'objects', alpha=alpha)
        
        # tools
        self.sword = load_dir(path + 'tools/sword', alpha=alpha)
        
        
        # sounds
        self.sounds = load_sounds('data/sfx/')
        self.limit_volume()
    
    
    
    def limit_volume(self):
        for sound in self.sounds:
            self.sounds[sound].set_volume(0.1)
        
                
        