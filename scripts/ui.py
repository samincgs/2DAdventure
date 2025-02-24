import pygame

from .font import Font
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
        
        # self.font = Font(FONT_PATH + 'small_font.png')
        # self.maru_monica_font = pygame.font.Font('data/fonts/marumonica.ttf', 28)
        # self.maru_monica_font2 = pygame.font.Font('data/fonts/marumonica.ttf', 32)
        
        
        self.current_dialogue = ''
        self.menu_cursor = 0
                
    def draw_dialogue(self, surf):
        dialogue_size_x = 30
        dialogue_size_y = 8
        dialogue_height = 55
        
        dialogue_surf = pygame.Surface((DISPLAY_WIDTH - dialogue_size_x * 2, dialogue_height), pygame.SRCALPHA)
        dialogue_surf.fill((0, 0, 0, 190))
        
        dialogue_rect = pygame.Rect(4, 4, dialogue_surf.get_width() - 8, dialogue_surf.get_height() - 8)
        outline_rect = pygame.Rect(2, 2, dialogue_surf.get_width() - 4, dialogue_surf.get_height() - 4)
        
        pygame.draw.rect(dialogue_surf, (255, 255, 255, 255), outline_rect)
        pygame.draw.rect(dialogue_surf, (0, 0, 0, 190), dialogue_rect, 0, 5)
        
        surf.blit(dialogue_surf, (dialogue_size_x, dialogue_size_y))
    
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
        status_surf = pygame.Surface((80, 160), pygame.SRCALPHA)
        status_surf.fill((0, 0, 0, 0))
        
        transparent_rect = pygame.Rect(2, 2, status_surf.get_width() - 4, status_surf.get_height() - 4)
        status_rect = pygame.Rect(0, 0, status_surf.get_width(), status_surf.get_height())
        
        pygame.draw.rect(status_surf, (0, 0, 0, 190), transparent_rect)
        pygame.draw.rect(status_surf, (255, 255, 255, 255), status_rect, 2, 5)

        surf.blit(status_surf, (160, 12))
    
    def status_dialog_font(self, surf):
        font = self.fonts['medium_text_font']
        line_height = 36
        
        stats_font = self.fonts['medium_title_font']
        stats_font.set_underline(True)
        stats_text = stats_font.render('Stats', self.aa, (255, 255, 255))
        
        surf.blit(stats_text, (554, 50))
        
        x_pos = 160 * 3 + 14
        y_pos = 100

        status_data = {
            'level': self.game.player.level,
            'health': self.game.player.health,
            'strength': self.game.player.strength,
            'exp': self.game.player.exp,
            'next_level_exp': self.game.player.next_level_exp,
            'strength': self.game.player.strength,
            'coins': self.game.player.coins,
            'weapon': self.game.player.weapon_type,
        }
        
        level_text = font.render('Level: ' + str(status_data['level']), self.aa, (255, 255, 255))
        surf.blit(level_text, (x_pos, y_pos))
        y_pos += line_height
        
        health_text = font.render('Health: ' + str(status_data['health']), self.aa, (255, 255, 255))
        surf.blit(health_text, (x_pos, y_pos))
        y_pos += line_height
                
        strength_text = font.render('Strength: ' + str(status_data['strength']), self.aa, (255, 255, 255))
        surf.blit(strength_text, (x_pos, y_pos))
        y_pos += line_height
        
        dex_text = font.render('Dexterity: ', self.aa, (255, 255, 255))
        surf.blit(dex_text, (x_pos, y_pos))
        y_pos += line_height
        
        exp_text = font.render('EXP: ' + str(status_data['exp']), self.aa, (255, 255, 255))
        surf.blit(exp_text, (x_pos, y_pos))
        y_pos += line_height
        
        exp_needed_text = font.render('EXP Needed: ' + str(status_data['next_level_exp']), self.aa, (255, 255, 255))
        surf.blit(exp_needed_text, (x_pos, y_pos))
        y_pos += line_height
        
        coin_text = font.render('Coin: ' + str(status_data['coins']), self.aa, (255, 255, 255))
        surf.blit(coin_text, (x_pos, y_pos))
        y_pos += line_height
        
        weapon_text = font.render('Weapon: ' + str(status_data['weapon']).title(), self.aa, (255, 255, 255))
        surf.blit(weapon_text, (x_pos, y_pos))
        y_pos += line_height
        
        
    
    def title_menu_font_screen(self, surf):
        title_text = self.fonts['big_title_font'].render('Adventure Game', self.aa, (255, 255, 255))
        shadow_title_text = self.fonts['big_title_font'].render('Adventure Game', self.aa, 'gray')
        
        surf.blit(shadow_title_text, (SCREEN_WIDTH// 2 - title_text.get_width() / 2 + 2, SCREEN_HEIGHT // 2 - title_text.get_height() / 2 - 180 + 2))
        surf.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() / 2, SCREEN_HEIGHT // 2 - title_text.get_height() / 2 - 180))
        
        y_offset = 0
        
        new_game_text = self.fonts['medium_title_font'].render('NEW GAME', self.aa, (255, 255, 255))
        text_pos = (SCREEN_WIDTH // 2 - new_game_text.get_width() / 2, SCREEN_HEIGHT // 2 - new_game_text.get_height() / 2 + 60 + y_offset)
        surf.blit(new_game_text, text_pos)
        y_offset += 50
        if self.menu_cursor == 0:
            surf.blit(self.fonts['medium_title_font'].render('>', self.aa, (255, 255, 255)), (text_pos[0] - 30, text_pos[1]))
        
        load_game_text = self.fonts['medium_title_font'].render('LOAD GAME', self.aa, (255, 255, 255))
        text_pos = (SCREEN_WIDTH // 2 - load_game_text.get_width() / 2, SCREEN_HEIGHT // 2 - load_game_text.get_height() / 2 + 60 + y_offset)
        surf.blit(load_game_text, text_pos)
        y_offset += 50
        if self.menu_cursor == 1:
            surf.blit(self.fonts['medium_title_font'].render('>', self.aa, (255, 255, 255)), (text_pos[0] - 30, text_pos[1]))
        
        quit_text = self.fonts['medium_title_font'].render('QUIT', self.aa, (255, 255, 255))
        text_pos = (SCREEN_WIDTH // 2 - quit_text.get_width() / 2, SCREEN_HEIGHT // 2 - quit_text.get_height() / 2 + 60 + y_offset)
        surf.blit(quit_text, text_pos)
        y_offset += 50
        if self.menu_cursor == 2:
            surf.blit(self.fonts['medium_title_font'].render('>', self.aa, (255, 255, 255)), (text_pos[0] - 30, text_pos[1]))
    
    def render(self, surf):
        if self.state.menu_state:  #MENU STATE
            self.draw_menu_character(surf)
        elif self.state.play_state: #PLAY STATE
            # render hearts
            self.draw_player_hearts(surf)
            self.draw_enemy_health(surf)
        elif self.state.pause_state:
            pause_text = 'PAUSED'
        elif self.state.dialogue_state:
            self.draw_player_hearts(surf)
            self.draw_dialogue(surf)
        elif self.state.status_state:
            self.draw_player_hearts(surf)
            self.draw_character_status(surf)

    def render_font(self, surf):
        if self.state.menu_state:
            self.title_menu_font_screen(surf)   
        elif self.state.dialogue_state:
            if self.current_dialogue:
                dialogue_text = self.fonts['medium_text_font'].render(self.current_dialogue, self.aa, (255, 255, 255))
                surf.blit(dialogue_text, (130, 50))
        elif self.state.status_state:
            self.status_dialog_font(surf)