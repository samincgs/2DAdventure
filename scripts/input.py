import pygame
import sys

from .const import *

class Input:
    def __init__(self, game, state):
        self.game = game
        self.state = state
        
        self.up_pressed = False # UP KEY
        self.down_pressed = False # DOWN KEY
        self.left_pressed = False # LEFT KEY
        self.right_pressed = False # RIGHT KEY
        self.interacted = False # Z KEY
        self.enter_pressed = False # ENTER KEY
        
        self.debug = False # TAB KEY

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
                if self.state.ingame_state:
                    if event.key == pygame.K_UP:
                        self.up_pressed = True
                    if event.key == pygame.K_LEFT:
                        self.left_pressed = True
                    if event.key == pygame.K_DOWN:
                        self.down_pressed = True
                    if event.key == pygame.K_RIGHT:
                        self.right_pressed = True
                    if event.key == pygame.K_z:
                        self.interacted = True
                    if event.key == pygame.K_TAB:
                        self.debug = not self.debug
                    if event.key == pygame.K_p:
                        if self.state.play_state or self.state.dialogue_state:
                            self.state.set_state('pause')
                        elif self.state.pause_state:
                            self.state.current_state = self.state.last_state 
                else:
                    if event.key == pygame.K_UP:
                        self.game.ui.menu_cursor = (self.game.ui.menu_cursor - 1) % 3 
                    if event.key == pygame.K_DOWN:
                        self.game.ui.menu_cursor = (self.game.ui.menu_cursor + 1) % 3
                    if event.key == pygame.K_z:
                        if self.game.ui.menu_cursor == 0:
                            self.state.set_state('play')
                        elif self.game.ui.menu_cursor == 2:
                            self.quit_game()
                  
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.up_pressed = False
                if event.key == pygame.K_LEFT:
                    self.left_pressed = False
                if event.key == pygame.K_DOWN:
                    self.down_pressed = False
                if event.key == pygame.K_RIGHT:
                    self.right_pressed = False
                if event.key == pygame.K_z:
                    self.interacted = False
                if event.key == pygame.K_RETURN:
                    self.enter_pressed = False
                
                    
        if self.debug:
            print(f"POS: {self.game.player.pos}")         
            print(f"RECT: {self.game.player.rect.topleft}")  
            print(f"SCROLL: {self.game.scroll}")            
            print(f"FPS: {self.game.window.clock.get_fps()}") 
            print("-" * 40)
            