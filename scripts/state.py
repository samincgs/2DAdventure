class State:
    def __init__(self, game):
        self.game = game
        
        self.game_states = {'play': 0, 'pause': 1, 'dialogue': 2, 'menu': 3}
        # self.current_state = self.game_states['menu']
        self.current_state = self.game_states['play']
        
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
    def ingame_state(self):
        return self.current_state in {self.game_states['play'], self.game_states['pause'], self.game_states['dialogue']}
    
    def set_state(self, state):
        self.current_state = self.game_states[state]
        
    def return_to_play_state(self):
        self.set_state('play')
        self.current_event = None
        self.interacted_npc = None
    
    def track_last_state(self):
        if not self.pause_state:
            self.last_state = self.current_state
        
    def update(self):
        pass
                        
    def track_event_and_dialogues(self):
        if self.interacted_npc:
            self.interacted_npc.continue_dialogue()
        if self.current_event and self.game.input.interacted:
            self.return_to_play_state()