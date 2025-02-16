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
    
    
    def draw_dialogue(self, surf):
        pass
    
    def render(self, surf):
        if self.game.current_state == self.game.game_states['play']:
            pass
        elif self.game.current_state == self.game.game_states['pause']:
            pause_text = 'PAUSED'
            self.font.render(surf, pause_text, (DISPLAY_WIDTH // 2 - self.font.width(pause_text) // 2, DISPLAY_HEIGHT // 2 - 30 - self.font.base_size[1]))
        elif self.game.current_state == self.game.game_states['dialogue']:
            dialogue_rect = pygame.Rect(50, 10, DISPLAY_WIDTH - 50 * 2, 45)
            outline_rect = pygame.Rect(48, 8, DISPLAY_WIDTH - 50 * 2 + 4, 45 + 4)
            outer_rect = pygame.Rect(47, 7, DISPLAY_WIDTH - 50 * 2 + 6, 45 + 6)
            pygame.draw.rect(surf, (0, 0, 0), outer_rect, 0, 5)
            pygame.draw.rect(surf, (255, 255, 255), outline_rect, 0, 5)
            pygame.draw.rect(surf, (0, 0, 0), dialogue_rect, 0, 5)
        
        
    def render_font(self, surf, dt):
        pass