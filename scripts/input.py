import pygame
import sys

class Input:
    def __init__(self):
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False
        
        self.debug = False
    
    @property
    def pressed(self):
        return self.up_pressed or self.down_pressed or self.left_pressed or self.right_pressed
    
    def update(self):
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
                if event.key == pygame.K_TAB:
                    self.debug = not self.debug
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.up_pressed = False
                if event.key == pygame.K_a:
                    self.left_pressed = False
                if event.key == pygame.K_s:
                    self.down_pressed = False
                if event.key == pygame.K_d:
                    self.right_pressed = False
                    