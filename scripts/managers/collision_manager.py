import pygame

from ..const import *

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
    
    def collision_obj(self, entity, obj):
        if entity.rect.colliderect(obj.rect):
            return obj
    
    def check_tile(self, entity):
        
        tiles = self.tile_manager.get_nearby_rects(entity.pos)
        temp_rect = entity.rect
        collisions = self.collision_test(temp_rect, tiles)
        
        tile_collide = False
        for collision_rect in collisions:
            if entity.direction == 'right':
                temp_rect.right = collision_rect.left  
                tile_collide = True
            elif entity.direction == 'left':
                temp_rect.left = collision_rect.right  
                tile_collide = True
            elif entity.direction == 'up':
                temp_rect.top = collision_rect.bottom  
                tile_collide = True
            elif entity.direction == 'down':
                temp_rect.bottom = collision_rect.top
                tile_collide = True      
            entity.pos = [temp_rect.x, temp_rect.y]
            
        return tile_collide
            
        
    def check_object(self, entity, obj):
        
        collided = None
        
        collision_obj = self.collision_obj(entity, obj)
        temp_rect = entity.rect
                
        if collision_obj and collision_obj.collision_on:
            if entity.direction == 'right':
                temp_rect.right = collision_obj.rect.left
            elif entity.direction == 'left':
                temp_rect.left = collision_obj.rect.right
            elif entity.direction == 'up':
                temp_rect.top = collision_obj.rect.bottom
            elif entity.direction == 'down':
                temp_rect.bottom = collision_obj.rect.top
            entity.pos = [temp_rect.x, temp_rect.y]
        
        collided = collision_obj
        return collided
    
    def check_entity(self, entity, other):
        
        collided_entity = None
        
        other_rect = other.rect
        collisions = self.collision_test(entity.rect, [other_rect])
        temp_rect = entity.rect
        
        for collision_rect in collisions:
            if entity.direction == 'right':
                temp_rect.right = collision_rect.left  
            elif entity.direction == 'left':
                temp_rect.left = collision_rect.right   
            elif entity.direction == 'up':
                temp_rect.top = collision_rect.bottom  
            elif entity.direction == 'down':
                temp_rect.bottom = collision_rect.top  
            entity.pos = [temp_rect.x, temp_rect.y]
            collided_entity = other
            return collided_entity
            
        return collided_entity
            
    def check_event(self, loc, size, req_direction='any', push=False):
        rect = pygame.Rect(loc[0], loc[1], size, size)
        player = self.game.player
        
        
        if player.rect.colliderect(rect) and (player.direction == req_direction or req_direction == 'any'):
            if push:
                if player.direction == 'up':
                    player.pos[1] = rect.bottom + push
                elif player.direction == 'down':
                    player.pos[1] = rect.top - push
                elif player.direction == 'right':
                    player.pos[0] = rect.left - push
                elif player.direction == 'left':
                    player.pos[0] = rect.right + push
            return True

            
            
            
        


    
        
        
        
        
                
                