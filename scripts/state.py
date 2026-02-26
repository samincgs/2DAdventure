from scripts.const import START_STATE, GAME_STATES




class State:
    def __init__(self, game):
        self.game = game
        
        self.game_states = GAME_STATES
        self.current_state = self.game_states[START_STATE]
        
        self.last_state = self.current_state
        
        self.interacted_npc = None
        self.current_event = None
        
    @property
    def play_state(self):
        return self.current_state == self.game_states['play']
    
    @property
    def pause_state(self):
        return self.current_state == self.game_states['pause']
    
    @property
    def dialogue_state(self):
        return self.current_state == self.game_states['dialogue']
    
    @property
    def menu_state(self):
        return self.current_state == self.game_states['menu']
    
    @property
    def status_state(self):
        return self.current_state == self.game_states['status']
    
    @property
    def ingame_state(self):
        return self.current_state in {self.game_states['play'], self.game_states['pause'], self.game_states['dialogue'], self.game_states['status']}
    
    def set_state(self, state):
        self.current_state = self.game_states[state]
    
    # needed for smaller dialogue messages
    def set_event(self, event_name):
        self.current_event = event_name
        
    def create_dialogue(self, message, event):
        self.set_state('dialogue')
        self.set_event(event)
        self.game.renderer.ui.current_dialogue = message
        
    def return_to_play_state(self):
        self.set_state('play')
        self.current_event = None
        self.interacted_npc = None
    
    def track_last_state(self):
        if not self.pause_state:
            self.last_state = self.current_state
        
    def update(self):
        self.track_last_state()
        
        if self.play_state: 
            self.game.manager.em.update(self.game.window.dt)
        elif self.dialogue_state:
            self.track_event_and_dialogues()
                        
    def track_event_and_dialogues(self):
        if self.interacted_npc and self.game.input.interacted:
            self.interacted_npc.continue_dialogue()
            
        # one line dialog box
        if self.current_event and self.game.input.interacted:
            self.return_to_play_state()