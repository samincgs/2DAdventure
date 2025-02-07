
from .object import Object
from ..const import *
from ..utils import load_img

class Key(Object):
    def __init__(self, pos, name, size):
        super().__init__(pos, name, size)
        self.img = load_img(OBJECT_IMG_PATH + name + '.png')