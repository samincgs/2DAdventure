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
            dialogue_size_x = 30
            dialogue_size_y = 8
            dialogue_height = 55
            
            dialogue_surf = pygame.Surface((DISPLAY_WIDTH - dialogue_size_x * 2, dialogue_height), pygame.SRCALPHA)
            dialogue_surf.fill((0,0,0))
            
            dialogue_rect = pygame.Rect(4, 4, dialogue_surf.get_width() - 8, dialogue_surf.get_height() - 8)
            outline_rect = pygame.Rect(2, 2, dialogue_surf.get_width() - 4, dialogue_surf.get_height() - 4)
            
            pygame.draw.rect(dialogue_surf, (255, 255, 255, 255), outline_rect)
            pygame.draw.rect(dialogue_surf, (0, 0, 0, 210), dialogue_rect, 0, 5)
            surf.blit(dialogue_surf, (dialogue_size_x, dialogue_size_y))
            
            
        
        
    def render_font(self, surf, dt):
        pass