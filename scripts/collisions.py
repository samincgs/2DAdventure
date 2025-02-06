class CollisionManager:
    def __init__(self, game, tile_manager):
        self.game = game
        self.tile_manager = tile_manager
        
        
    def check_tile(self, entity):
        tiles = self.tile_manager.get_nearby_tiles(entity.pos)
        
        temp_rect = entity.rect
        collisions = self.tile_manager.collision_test(temp_rect, tiles)
        
        for collision_rect in collisions:
            if entity.direction == 'right':
                temp_rect.right = collision_rect.left  
            elif entity.direction == 'left':
                temp_rect.left = collision_rect.right  
        entity.pos[0] = temp_rect.x
            
                    
        temp_rect = entity.rect
        collisions = self.tile_manager.collision_test(temp_rect, tiles)
        for collision_rect in collisions:
            if entity.direction == 'up':
                temp_rect.top = collision_rect.bottom  
            elif entity.direction == 'down':
                temp_rect.bottom = collision_rect.top  
        entity.pos[1] = temp_rect.y
                