class Entity:
    def __init__(self, game, pos):
        self.game = game
        self.pos = list(pos)
        self.x = 368
        self.y = 336
        self.speed = 3
        self.direction = None
        
        self.up1 = None
        self.up2 = None
        self.down1 = None
        self.down2 = None
        self.left1 = None
        self.left2 = None
        self.right1 = None
        self.right2 = None
        
        self.frame_index = 0 # spriteCounter
        self.frame_num = 0

      
    def update(self, dt):
        pass
    
    def render(self, surf, offset=(0, 0)):
        pass
    