from scripts.ui import UI

class Renderer:
    def __init__(self, game):
        self.game = game
        self.ui = UI(self.game, self.game.state)
    
    def render(self):
        surf = self.game.window.display
        
        self.game.window.create(self.ui)
        if self.game.state.ingame_state:
            self.game.manager.render(surf, offset=self.game.camera.render_scroll)
        self.ui.render(surf)   