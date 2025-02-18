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
        
        tiles = self.tile_manager.get_nearby_rects(entity.pos)
        temp_rect = entity.rect
        collisions = self.collision_test(temp_rect, tiles)
        
        for collision_rect in collisions:
            if entity.direction == 'right':
                temp_rect.right = collision_rect.left  
            elif entity.direction == 'left':
                temp_rect.left = collision_rect.right  
            entity.pos[0] = temp_rect.x
            
        tiles = self.tile_manager.get_nearby_rects(entity.pos)
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
        
        collisions = self.collision_obj(entity.rect, self.game.object_spawner.objects)
        temp_rect = entity.rect
        
        for collision_obj in collisions:
            if collision_obj.collision_on:
                if entity.direction == 'right':
                    temp_rect.right = collision_obj.rect.left
                elif entity.direction == 'left':
                    temp_rect.left = collision_obj.rect.right
            obj = collision_obj
            entity.pos[0] = temp_rect.x
            
        collisions = self.collision_obj(entity.rect, self.game.object_spawner.objects)
        temp_rect = entity.rect
        
        for collision_obj in collisions:
            if collision_obj.collision_on:
                if entity.direction == 'up':
                    temp_rect.top = collision_obj.rect.bottom
                elif entity.direction == 'down':
                    temp_rect.bottom = collision_obj.rect.top
            obj = collision_obj
            entity.pos[1] = temp_rect.y
        return obj
    
    def check_entity(self, entity, other):
        
        other_rect = [pygame.Rect(*other.rect)]
        collisions = self.collision_test(entity.rect, other_rect)
        temp_rect = entity.rect
        
        for collision_rect in collisions:
            if entity.direction == 'right':
                temp_rect.right = collision_rect.left  
            elif entity.direction == 'left':
                temp_rect.left = collision_rect.right  
            entity.pos[0] = temp_rect.x
            
        other_rect = [pygame.Rect(*other.rect)]
        collisions = self.collision_test(entity.rect, other_rect)
        temp_rect = entity.rect
        
        for collision_rect in collisions:
            if entity.direction == 'up':
                temp_rect.top = collision_rect.bottom  
            elif entity.direction == 'down':
                temp_rect.bottom = collision_rect.top  
            entity.pos[1] = temp_rect.y
            
    def check_event(self, loc, size, req_direction='any', push=False):
        rect = pygame.Rect(loc[0], loc[1], size, size)
        player = self.game.player
        
        # debug
        # pygame.draw.rect(self.game.window.display, (255, 0, 0), pygame.Rect(rect.x - self.game.scroll[0], rect.y - self.game.scroll[1], size, size))
        
        if player.rect.colliderect(rect) and (player.direction == req_direction or req_direction == 'any'):
            if push:
                if player.direction == 'up':
                    player.pos[1] = rect.bottom + size
                elif player.direction == 'down':
                    player.pos[1] = rect.top - size
                elif player.direction == 'right':
                    player.pos[0] = rect.left - size
                elif player.direction == 'left':
                    player.pos[0] = rect.right + size
            return True

            
            
            
        


    
        
        
        
        
                
                