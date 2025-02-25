import pygame

from .const import *

FONT_PATH = 'data/fonts/'
BYTEBOUNCE_FONT = FONT_PATH + 'ByteBounce.ttf'

class UI:
    def __init__(self, game, state):
        self.game = game
        self.state = state
    
        # set the icon of the game to player down
        pygame.display.set_icon(self.game.assets.player['down'][0])
        
        self.fonts = {
        'big_title_font': pygame.font.Font(BYTEBOUNCE_FONT, 84),
        'medium_title_font': pygame.font.Font(BYTEBOUNCE_FONT, 48),
        'medium_text_font': pygame.font.Font(BYTEBOUNCE_FONT, 32),
        'small_text_font' : pygame.font.Font(BYTEBOUNCE_FONT, 26)
        }
        
        self.aa = False
        
        self.current_dialogue = ''
        self.menu_cursor = 0
        
        self.ui_messages = [] # message, timer
        
    def draw_ui_message(self, text):
        message_timer = 0
        self.ui_messages.append([text, message_timer])
    
    
    def draw_box(self, surf, size, loc, alpha=190):
        status_surf = pygame.Surface(size, pygame.SRCALPHA)
        status_surf.fill((0, 0, 0, 0))
        
        transparent_rect = pygame.Rect(2, 2, status_surf.get_width() - 4, status_surf.get_height() - 4)
        status_rect = pygame.Rect(0, 0, status_surf.get_width(), status_surf.get_height())
        
        pygame.draw.rect(status_surf, (0, 0, 0, alpha), transparent_rect)
        pygame.draw.rect(status_surf, WHITE, status_rect, 2, 5)
        
        surf.blit(status_surf, loc)
                
    def draw_dialogue(self, surf):
        dialogue_size_x = 30
        dialogue_height = 55
        dialogue_size_y = 8
        self.draw_box(surf, (DISPLAY_WIDTH - dialogue_size_x * 2, dialogue_height), (dialogue_size_x, dialogue_size_y))
            
    def draw_enemy_health(self, surf):
        for enemy in self.game.entities:
            if enemy.type in MONSTERS and enemy.hp_bar_on:
                health_ratio = enemy.health / enemy.max_health
                outline_rect = pygame.Rect(enemy.pos[0] - self.game.scroll[0] - 1, enemy.pos[1] - self.game.scroll[1] - 8, (1 * 10 + 2), 4)
                health_rect = pygame.Rect(enemy.pos[0] - self.game.scroll[0], enemy.pos[1] - self.game.scroll[1] - 7, (health_ratio * 10), 2)
                if health_rect:
                    pygame.draw.rect(surf, (35, 35, 35), outline_rect, 0, 2)
                    pygame.draw.rect(surf, (255, 0, 30), health_rect)
                
    
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
    
    def draw_character_status(self, surf):
        size = (80, 160)
        loc = (160, 12)
        self.draw_box(surf, size, loc)
    
    def draw_inventory(self, surf):
        # inventory box
        size = (130, 80)
        loc = [20, 12]
        self.draw_box(surf, size, loc)
        
        # text box
        size = (130, 60)
        loc = [20, 100]
        self.draw_box(surf, size, loc)
    
    def status_dialog_font(self, surf):
        font = self.fonts['medium_text_font']
        stats_font = self.fonts['medium_title_font']
        stats_font.set_underline(True)
        
        line_height = 36
        
        stats_text = stats_font.render('Stats', self.aa, WHITE)
        surf.blit(stats_text, (554, 50))
        
        x_pos = 160 * 3 + 14
        y_pos = 100

        status_data = {
            'level': self.game.player.level,
            'health': self.game.player.health,
            'strength': self.game.player.strength,
            'exp': self.game.player.exp,
            'exp required': self.game.player.next_level_exp,
            'strength': self.game.player.strength,
            'coins': self.game.player.coins,
            'weapon': str(self.game.player.weapon_type).title(),
        }
        
        for text, data in status_data.items():
            status_text = font.render(text.title() + ': ' + str(data), self.aa, WHITE)
            surf.blit(status_text, (x_pos, y_pos))
            y_pos += line_height
            
        
        
    def title_menu_font_screen(self, surf):
        title_text = self.fonts['big_title_font'].render('Adventure Game', self.aa, WHITE)
        shadow_title_text = self.fonts['big_title_font'].render('Adventure Game', self.aa, 'gray')
        
        surf.blit(shadow_title_text, (SCREEN_WIDTH// 2 - title_text.get_width() / 2 + 2, SCREEN_HEIGHT // 2 - title_text.get_height() / 2 - 180 + 2))
        surf.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() / 2, SCREEN_HEIGHT // 2 - title_text.get_height() / 2 - 180))
        
        y_offset = 0
        
        new_game_text = self.fonts['medium_title_font'].render('NEW GAME', self.aa, WHITE)
        text_pos = (SCREEN_WIDTH // 2 - new_game_text.get_width() / 2, SCREEN_HEIGHT // 2 - new_game_text.get_height() / 2 + 60 + y_offset)
        surf.blit(new_game_text, text_pos)
        y_offset += 50
        if self.menu_cursor == 0:
            surf.blit(self.fonts['medium_title_font'].render('>', self.aa, WHITE), (text_pos[0] - 30, text_pos[1]))
        
        load_game_text = self.fonts['medium_title_font'].render('LOAD GAME', self.aa, WHITE)
        text_pos = (SCREEN_WIDTH // 2 - load_game_text.get_width() / 2, SCREEN_HEIGHT // 2 - load_game_text.get_height() / 2 + 60 + y_offset)
        surf.blit(load_game_text, text_pos)
        y_offset += 50
        if self.menu_cursor == 1:
            surf.blit(self.fonts['medium_title_font'].render('>', self.aa, WHITE), (text_pos[0] - 30, text_pos[1]))
        
        quit_text = self.fonts['medium_title_font'].render('QUIT', self.aa, WHITE)
        text_pos = (SCREEN_WIDTH // 2 - quit_text.get_width() / 2, SCREEN_HEIGHT // 2 - quit_text.get_height() / 2 + 60 + y_offset)
        surf.blit(quit_text, text_pos)
        y_offset += 50
        if self.menu_cursor == 2:
            surf.blit(self.fonts['medium_title_font'].render('>', self.aa, WHITE), (text_pos[0] - 30, text_pos[1]))
    
    def render(self, surf):
        if self.state.menu_state:  #MENU STATE
            self.draw_menu_character(surf)
        elif self.state.play_state: #PLAY STATE
            # render hearts
            self.draw_player_hearts(surf)
            self.draw_enemy_health(surf)
        elif self.state.pause_state:
            pass
        elif self.state.dialogue_state:
            self.draw_player_hearts(surf)
            self.draw_dialogue(surf)
        elif self.state.status_state:
            self.draw_player_hearts(surf)
            self.draw_inventory(surf)
            self.draw_character_status(surf)

    def render_font(self, surf):
        if self.state.play_state:
            if len(self.ui_messages) >= 4:
                    self.ui_messages.pop(0)
            for idx, msg in enumerate(self.ui_messages.copy(), start=1):
                msg[1] += 1
                if msg[1] >= 200:
                    self.ui_messages.remove(msg)
                    
                y_height = SCREEN_HEIGHT - 150
                font = self.fonts['small_text_font']
                text = font.render(msg[0], self.aa, WHITE)
                shadow_text = font.render(msg[0], self.aa, BLACK)
                surf.blit(shadow_text, (SCREEN_WIDTH - 50 - text.get_width() + 1, y_height + 30 * idx + 1))
                surf.blit(text, (SCREEN_WIDTH - 50 - text.get_width(), y_height + 30 * idx))
                
        elif self.state.menu_state:
            self.title_menu_font_screen(surf)   
        elif self.state.dialogue_state:
            if self.current_dialogue:
                dialogue_text = self.fonts['medium_text_font'].render(self.current_dialogue, self.aa, WHITE)
                surf.blit(dialogue_text, (130, 50))
        elif self.state.status_state:
            self.status_dialog_font(surf)