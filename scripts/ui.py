import pygame

from .font import Font
from .const import *

class UI:
    def __init__(self, game, state):
        self.game = game
        self.state = state
        
        self.font = Font(FONT_PATH + 'small_font.png')
        self.maru_monica_font = pygame.font.Font('data/fonts/marumonica.ttf', 28)
        self.byte_bounce_font = pygame.font.Font('data/fonts/ByteBounce.ttf', 84)
        self.byte_bounce_font2 = pygame.font.Font('data/fonts/ByteBounce.ttf', 48)
        
        self.current_dialogue = ''
        self.menu_cursor = 0
                
    def draw_dialogue(self, surf):
        dialogue_size_x = 30
        dialogue_size_y = 8
        dialogue_height = 55
        
        dialogue_surf = pygame.Surface((DISPLAY_WIDTH - dialogue_size_x * 2, dialogue_height), pygame.SRCALPHA)
        dialogue_surf.fill((0, 0, 0))
        
        dialogue_rect = pygame.Rect(4, 4, dialogue_surf.get_width() - 8, dialogue_surf.get_height() - 8)
        outline_rect = pygame.Rect(2, 2, dialogue_surf.get_width() - 4, dialogue_surf.get_height() - 4)
        
        pygame.draw.rect(dialogue_surf, (255, 255, 255, 255), outline_rect)
        pygame.draw.rect(dialogue_surf, (0, 0, 0, 190), dialogue_rect, 0, 5)
        
        surf.blit(dialogue_surf, (dialogue_size_x, dialogue_size_y))
    
    def draw_player_hearts(self, surf):
        full_heart_img = self.game.assets.objects['full_heart']
        half_heart_img = self.game.assets.objects['half_heart']
        empty_heart_img = self.game.assets.objects['empty_heart']
        
        total_hearts = self.game.player.max_health / 2
        player_hearts = self.game.player.health
        
        
        for i in range(int(total_hearts)):
            if player_hearts >= 2:
                surf.blit(full_heart_img, (4 + i * 18, 4))
                player_hearts -= 2
            elif player_hearts == 1:
                surf.blit(half_heart_img, (4 + i * 18, 4))
                player_hearts -= 1
            else:
                surf.blit(empty_heart_img, (4 + i * 18, 4))
        
     
    def draw_menu_character(self, surf):
        char_img = self.game.assets.player['down'][0]
        char_img = pygame.transform.scale(char_img, (char_img.get_width() * 2, char_img.get_height() * 2))
        surf.blit(char_img, (DISPLAY_WIDTH // 2 - char_img.get_width() / 2, DISPLAY_HEIGHT // 2 - char_img.get_height() / 2 - 20))
    
    def render(self, surf):
        if self.state.menu_state:  #MENU STATE
            self.draw_menu_character(surf)
        elif self.state.play_state: #PLAY STATE
            # render hearts
            self.draw_player_hearts(surf)
        elif self.state.pause_state:
            pause_text = 'PAUSED'
            self.font.render(surf, pause_text, (DISPLAY_WIDTH // 2 - self.font.width(pause_text) // 2, DISPLAY_HEIGHT // 2 - 30 - self.font.base_size[1]))
        elif self.state.dialogue_state:
            self.draw_player_hearts(surf)
            self.draw_dialogue(surf)
                
    def render_font(self, surf):
        if self.state.menu_state:
            title_text = self.byte_bounce_font.render('Adventure Game', False, (255, 255, 255))
            shadow_title_text = self.byte_bounce_font.render('Adventure Game', False, 'gray')
            
            surf.blit(shadow_title_text, (SCREEN_WIDTH// 2 - title_text.get_width() / 2 + 2, SCREEN_HEIGHT // 2 - title_text.get_height() / 2 - 180 + 2))
            surf.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() / 2, SCREEN_HEIGHT // 2 - title_text.get_height() / 2 - 180))
            
            y_offset = 0
            
            new_game_text = self.byte_bounce_font2.render('NEW GAME', False, (255, 255, 255))
            text_pos = (SCREEN_WIDTH // 2 - new_game_text.get_width() / 2, SCREEN_HEIGHT // 2 - new_game_text.get_height() / 2 + 60 + y_offset)
            surf.blit(new_game_text, text_pos)
            y_offset += 50
            if self.menu_cursor == 0:
                surf.blit(self.byte_bounce_font2.render('>', False, (255, 255, 255)), (text_pos[0] - 30, text_pos[1]))
            
            load_game_text = self.byte_bounce_font2.render('LOAD GAME', False, (255, 255, 255))
            text_pos = (SCREEN_WIDTH // 2 - load_game_text.get_width() / 2, SCREEN_HEIGHT // 2 - load_game_text.get_height() / 2 + 60 + y_offset)
            surf.blit(load_game_text, text_pos)
            y_offset += 50
            if self.menu_cursor == 1:
                surf.blit(self.byte_bounce_font2.render('>', False, (255, 255, 255)), (text_pos[0] - 30, text_pos[1]))
            
            quit_text = self.byte_bounce_font2.render('QUIT', False, (255, 255, 255))
            text_pos = (SCREEN_WIDTH // 2 - quit_text.get_width() / 2, SCREEN_HEIGHT // 2 - quit_text.get_height() / 2 + 60 + y_offset)
            surf.blit(quit_text, text_pos)
            y_offset += 50
            if self.menu_cursor == 2:
                surf.blit(self.byte_bounce_font2.render('>', False, (255, 255, 255)), (text_pos[0] - 30, text_pos[1]))
            
        elif self.state.dialogue_state:
            if self.current_dialogue:
                dialogue_text = self.maru_monica_font.render(self.current_dialogue, False, (255, 255, 255))
                surf.blit(dialogue_text, (130, 50))