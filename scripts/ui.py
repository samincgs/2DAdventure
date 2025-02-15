import pygame

from .font import Font

from .const import *

class UI:
    def __init__(self, game):
        self.game = game
        self.font = Font(FONT_PATH + 'small_font.png')
        self.roboto_font = pygame.font.Font('data/fonts/roboto.ttf', 28)
        self.roboto_font2 = pygame.font.Font('data/fonts/roboto.ttf', 24)
        self.roboto_font3 = pygame.font.Font('data/fonts/roboto.ttf', 50)
        
        self.message = None
        self.message_timer = 0
        
        self.play_time = 0
    
    def create_message(self, text, aa=True, color=(255, 255, 255)):
        self.message = self.roboto_font2.render(text, aa, color)
        self.message_timer = 0
    
    def render(self, surf):
        if self.game.current_state == self.game.game_states['play']:
            pass
        else:
            pause_text = 'PAUSED'
            self.font.render(surf, pause_text, (DISPLAY_WIDTH // 2 - self.font.width(pause_text) // 2, DISPLAY_HEIGHT // 2 - 30 - self.font.base_size[1]))
            
    def render_font(self, surf, dt):
        pass