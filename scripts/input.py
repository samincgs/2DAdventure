import pygame
import sys

from .const import *

class Input:
    def __init__(self, game):
        self.game = game
        
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        self.interacted = False
        self.debug = False
        
        self.menu_up = False
        self.menu_down = False
        
    
    @property
    def pressed(self):
        return self.up_pressed or self.down_pressed or self.left_pressed or self.right_pressed
    
    def quit_game(self):
        pygame.quit()
        sys.exit()
    
    def update(self):
        self.interacted = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                if self.game.current_state in {self.game.game_states['play'], self.game.game_states['pause'], self.game.game_states['dialogue']}:
                    if event.key == pygame.K_w:
                        self.up_pressed = True
                    if event.key == pygame.K_a:
                        self.left_pressed = True
                    if event.key == pygame.K_s:
                        self.down_pressed = True
                    if event.key == pygame.K_d:
                        self.right_pressed = True
                    if event.key == pygame.K_f:
                        self.interacted = True
                    if event.key == pygame.K_TAB:
                        self.debug = not self.debug
                    if event.key == pygame.K_p:
                        if self.game.play_state or self.game.dialogue_state:
                            self.game.set_state('pause')
                        elif self.game.pause_state:
                            self.game.current_state = self.game.last_state 
                else:
                    if event.key == pygame.K_UP:
                        self.game.ui.menu_cursor = (self.game.ui.menu_cursor - 1) % 3 
                    if event.key == pygame.K_DOWN:
                        self.game.ui.menu_cursor = (self.game.ui.menu_cursor + 1) % 3             
                  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.up_pressed = False
                if event.key == pygame.K_a:
                    self.left_pressed = False
                if event.key == pygame.K_s:
                    self.down_pressed = False
                if event.key == pygame.K_d:
                    self.right_pressed = False
                if event.key == pygame.K_f:
                    self.interacted = False
                
                    
        if self.debug:
            print(f"POS: {self.game.player.pos}")         
            print(f"RECT: {self.game.player.rect.topleft}")  
            print(f"SCROLL: {self.game.scroll}")            
            print(f"FPS: {self.game.window.clock.get_fps()}") 
            print("-" * 40)
    