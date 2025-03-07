import pygame

from .const import *

FONT_PATH = 'data/fonts/'
BYTEBOUNCE_FONT = FONT_PATH + 'ByteBounce.ttf'
MARUMONICA_FONT = FONT_PATH + 'marumonica.ttf'

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
        'small_text_font' : pygame.font.Font(BYTEBOUNCE_FONT, 27),
        'super_small_text_font' : pygame.font.Font(BYTEBOUNCE_FONT, 22),
        }
        
        self.aa = False
        
        self.current_dialogue = ''
        self.menu_cursor = 0
        
        self.inventory_max_col = 5
        self.inventory_max_row = 2
        self.inventory_slot_col = 0
        self.inventory_slot_row = 0
        self.render_inventory_textbox = False
        
        self.inventory_item_descriptions = ITEM_DESCRIPTIONS
                
        self.ui_messages = [] # message, timer
        
    def draw_ui_message(self, text):
        message_timer = 0
        self.ui_messages.append([text, message_timer])
    
    def draw_box(self, surf, size, loc, alpha=180, width=2, br=5):
        status_surf = pygame.Surface(size, pygame.SRCALPHA)
        status_surf.fill((0, 0, 0, 0))
        
        transparent_rect = pygame.Rect(2, 2, status_surf.get_width() - 4, status_surf.get_height() - 4)
        status_rect = pygame.Rect(0, 0, status_surf.get_width(), status_surf.get_height())
        
        pygame.draw.rect(status_surf, (0, 0, 0, alpha), transparent_rect)
        pygame.draw.rect(status_surf, WHITE, status_rect, width, br)
        
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
        size = (120, 73)
        loc = [20, 12]
        self.draw_box(surf, size, loc)
        
        # text box
        size = (120, 72)
        loc = [20, 100]
        if self.render_inventory_textbox:
            self.draw_box(surf, size, loc)
        
        # inventory slots
        size = (21, 21)
        slot_loc = [27, 36]
        cursor_loc = (slot_loc[0] + (size[0] * self.inventory_slot_col), slot_loc[1] + (size[1] * self.inventory_slot_row))
        self.draw_box(surf, size, cursor_loc, alpha=60, width=1, br=3)
        
        
        
        # draw the inventory cursor
        for idx, item_data in enumerate(self.game.player.inventory):
            item = item_data[0]
            img = item.type
            if item.type == 'sword':
                img = 'sword_ui'
                
            col = idx % self.inventory_max_col
            row = idx // self.inventory_max_col
            x = slot_loc[0] + 1 + col * size[0] + 1.5
            y = slot_loc[1] + 1 + row * size[1] + 2
                            
            surf.blit(self.game.assets.objects[img], (x, y))

    def inventory_font(self, surf):
        inventory_font = self.fonts['medium_title_font']
        inventory_font.set_underline(True)
        
        inventory_text = inventory_font.render('Inventory', self.aa, WHITE)
        surf.blit(inventory_text, (170, 50))
        
        # top half of inventory
        for idx, item_data in enumerate(self.game.player.inventory):
            amount = item_data[1]
            
            size = (21 * RENDER_SCALE, 21 * RENDER_SCALE)
            slot_loc = [27 * RENDER_SCALE, 36 * RENDER_SCALE]
            col = idx % self.inventory_max_col
            row = idx // self.inventory_max_col
            x = slot_loc[0] + 1 + col * size[0] + size[0] - size[0] / 2
            y = slot_loc[1] + 1 + row * size[1] + 1
            
            if amount > 1:
                amount_text = self.fonts['super_small_text_font'].render('x' + str(amount), self.aa, WHITE)    
                surf.blit(amount_text, (x, y))
                                
            # bottom half of inventory item description
            if idx == (self.inventory_slot_col + (self.inventory_slot_row * self.inventory_max_col)):
                self.render_inventory_textbox = True
                size = (120 * RENDER_SCALE, 72 * RENDER_SCALE)
                loc = [20 * RENDER_SCALE, 100 * RENDER_SCALE]
                if item_data[0].type in self.inventory_item_descriptions:
                    item_description_text = self.fonts['medium_text_font'].render(self.inventory_item_descriptions[item_data[0].type], self.aa, WHITE)
                    surf.blit(item_description_text, (loc[0] + 17, loc[1] + 25))
    
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
        menu_options = ['NEW GAME', 'LOAD GAME', 'QUIT']
        
        for idx, menu_option in enumerate(menu_options):
            text = self.fonts['medium_title_font'].render(menu_option, self.aa, WHITE)
            text_pos = (SCREEN_WIDTH // 2 - text.get_width() / 2, SCREEN_HEIGHT // 2 - text.get_height() / 2 + 60 + y_offset)
            surf.blit(text, text_pos)
            y_offset += 50
            if self.menu_cursor == idx:
                surf.blit(self.fonts['medium_title_font'].render('>', self.aa, WHITE), (text_pos[0] - 30, text_pos[1]))
     
    def render(self, surf):
        if self.state.menu_state:  #MENU STATE
            self.draw_menu_character(surf)
        elif self.state.play_state: #PLAY STATE
            # render hearts
            self.draw_player_hearts(surf)
            self.draw_enemy_health(surf)
        elif self.state.pause_state: # PAUSE STATE
            pass
        elif self.state.dialogue_state: # DIALOGUE STATE
            self.draw_player_hearts(surf)
            self.draw_dialogue(surf)
        elif self.state.status_state: # STATUS STATE
            self.draw_player_hearts(surf)
            self.draw_inventory(surf)
            self.draw_character_status(surf)
        
    def render_font(self, surf):
        self.render_inventory_textbox = False
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
            self.inventory_font(surf)
            self.status_dialog_font(surf)