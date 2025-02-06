class Entity:
    def __init__(self, game):
        self.game = game
        self.x = 100
        self.y = 100
        self.speed = 4
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
    
    def render(self, surf):
        pass
    