from .utils import load_dir, load_img


class Assets:
    def __init__(self, path='data/images/', file_type='.png'):
        self.path = path
        
        self.player_imgs = load_dir(path + 'player', load_img)
        self.object_imgs = load_dir(path + 'objects', load_img)
        self.tile_imgs = load_dir(path + 'tiles', load_img)
        
        print(self.player_imgs)
        print(self.object_imgs)
        print(self.tile_imgs)
        