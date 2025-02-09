import pygame

from .const import *

class UI:
    def __init__(self, game):
        self.game = game
        # self.font = Font(FONT_PATH + 'small_font.png')
        self.roboto_font = pygame.font.Font('data/fonts/roboto.ttf', 28)
        self.roboto_font2 = pygame.font.Font('data/fonts/roboto.ttf', 24)
        
        self.message = None
        self.message_timer = 0
    
    def create_message(self, text, aa=True, color=(255, 255, 255)):
        self.message = self.roboto_font2.render(text, aa, color)
        self.message_timer = 0
    
    def render(self, surf):
        key = self.game.assets.object_imgs['key']
        surf.blit(key, (2, 2))
    
    def render_font(self, surf, dt):
        key_text = self.roboto_font.render('x ' + str(self.game.player.has_keys), True, (255, 255, 255))
        surf.blit(key_text, (42, 10))
        
        if self.message:
            surf.blit(self.message, (20, SCREEN_HEIGHT// 3)) 
            self.message_timer += dt
            if self.message_timer > 1.5:
                self.message = None
                self.message_timer = 0    
        