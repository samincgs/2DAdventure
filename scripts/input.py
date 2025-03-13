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
        self.action = False # X KEY
        self.enter_pressed = False # ENTER KEY
        
        self.debug = False # TAB KEY

    @property
    def pressed(self):
        return self.up_pressed or self.down_pressed or self.left_pressed or self.right_pressed
    
    def quit_game(self):
        pygame.quit()
        sys.exit()
    
    def reset_keys(self):
        self.interacted = False
        self.action = False
        self.enter_pressed = False
    
    def update(self):
        self.reset_keys()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()  
                # in ingame state    
                if self.state.ingame_state:
                    if event.key == pygame.K_UP:
                        self.up_pressed = True
                        if self.state.status_state:
                            self.game.ui.inventory_slot_row = (self.game.ui.inventory_slot_row - 1 ) % self.game.ui.inventory_max_row
                    if event.key == pygame.K_LEFT:
                        self.left_pressed = True
                        if self.state.status_state:
                            self.game.ui.inventory_slot_col = (self.game.ui.inventory_slot_col - 1 ) % self.game.ui.inventory_max_col
                    if event.key == pygame.K_DOWN:
                        self.down_pressed = True
                        if self.state.status_state:
                            self.game.ui.inventory_slot_row = (self.game.ui.inventory_slot_row + 1 ) % self.game.ui.inventory_max_row
                    if event.key == pygame.K_RIGHT:
                        self.right_pressed = True
                        if self.state.status_state:
                            self.game.ui.inventory_slot_col = (self.game.ui.inventory_slot_col + 1 ) % self.game.ui.inventory_max_col
                    if event.key == pygame.K_z:
                        self.interacted = True
                        self.action = True
                    if event.key == pygame.K_RETURN:
                        if self.state.play_state:
                            self.state.set_state('status')
                        elif self.state.status_state:
                            self.state.set_state('play')
                    if event.key == pygame.K_TAB:
                        self.debug = not self.debug
                    if event.key == pygame.K_p:
                        if self.state.play_state or self.state.dialogue_state:
                            self.state.set_state('pause')
                        elif self.state.pause_state:
                            self.state.current_state = self.state.last_state 
                            
                elif self.state.menu_state:
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
                if event.key == pygame.K_RETURN:
                    self.enter_pressed = False
        
            
            