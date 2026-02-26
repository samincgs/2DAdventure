class Camera:
    def __init__(self, game):
        self.game = game
        self.scroll = [0, 0] 
        self.render_scroll = [0, 0]
        
    def update(self):
        if self.game.state.ingame_state:
            self.scroll[0] += (self.game.manager.em.player.pos[0] - self.game.window.display.get_width() // 2 - self.scroll[0]) 
            self.scroll[1] += (self.game.manager.em.player.pos[1] - self.game.window.display.get_height() // 2 - self.scroll[1]) 
            self.render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
