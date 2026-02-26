from scripts.ui import UI

class Renderer:
    def __init__(self, game):
        self.game = game
        self.ui = UI(self.game, self.game.state)
    
    def render(self):
        surf = self.game.window.display
        state = self.game.state
        manager = self.game.manager
        
        self.game.window.create(self.ui)
        if state.ingame_state:
            manager.tm.render_visible(surf, offset=self.game.camera.render_scroll)
            self.game.object_mapper.render(surf, offset=self.game.camera.render_scroll)
            manager.em.render(surf, offset=self.game.camera.render_scroll, ysort=True)
            
            if state.play_state: 
                manager.em.update(self.game.window.dt)
            elif state.dialogue_state:
                state.track_event_and_dialogues()
        
        self.ui.render(surf)   