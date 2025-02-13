import pygame
from .const import *

class CollisionManager:
    def __init__(self, game, tile_manager):
        self.game = game
        self.tile_manager = tile_manager
        
    def collision_test(self, rect, tiles):
        collisions = []
        for tile in tiles:
            if rect.colliderect(tile):
                collisions.append(tile)
        return collisions
    
    def collision_obj(self, rect, objs):
        collisions = []
        for obj in objs:
            if rect.colliderect(obj.rect):
                collisions.append(obj)
        return collisions
    
    def check_tile(self, entity):
        
        tiles = self.tile_manager.collision_rects
        temp_rect = entity.rect
        collisions = self.collision_test(temp_rect, tiles)
        
        for collision_rect in collisions:
            if entity.direction == 'right':
                temp_rect.right = collision_rect.left  
            elif entity.direction == 'left':
                temp_rect.left = collision_rect.right  
        entity.pos[0] = temp_rect.x
            
        tiles = self.tile_manager.collision_rects
        temp_rect = entity.rect
        collisions = self.collision_test(temp_rect, tiles)
        
        for collision_rect in collisions:
            if entity.direction == 'up':
                temp_rect.top = collision_rect.bottom  
            elif entity.direction == 'down':
                temp_rect.bottom = collision_rect.top  
        entity.pos[1] = temp_rect.y
        
    def check_object(self, entity):
        
        obj = None
        
        temp_rect = entity.rect.copy()
        collisions = self.collision_obj(temp_rect, self.game.object_spawner.objects)
        
        for collision_obj in collisions:
            if collision_obj.collision_on:
                if entity.direction == 'right':
                    temp_rect.right = collision_obj.rect.left
                elif entity.direction == 'left':
                    temp_rect.left = collision_obj.rect.right
            obj = collision_obj
            entity.pos[0] = temp_rect.x
            
        temp_rect = entity.rect.copy()
        collisions = self.collision_obj(temp_rect, self.game.object_spawner.objects)
        
        for collision_obj in collisions:
            if collision_obj.collision_on:
                if entity.direction == 'up':
                    temp_rect.top = collision_obj.rect.bottom
                elif entity.direction == 'down':
                    temp_rect.bottom = collision_obj.rect.top
            obj = collision_obj
            entity.pos[1] = temp_rect.y

        
        return obj
        
        
        
        
        
                
                