from scripts.objects.object import Object

class Key(Object):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, 'key', size)
        self.item_description = '[ Key ]\n\nA rusty key which is used\nto open doors.'
        