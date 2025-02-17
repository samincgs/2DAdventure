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
    
    @property
    def pressed(self):
        return self.up_pressed or self.down_pressed or self.left_pressed or self.right_pressed
    
    def update(self):
        self.interacted = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
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
                    
            