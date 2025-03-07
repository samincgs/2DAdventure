from scripts.tools.sword import Sword
from scripts.objects.key import Key
from scripts.objects.sneaker import Sneaker
from scripts.entities.npc import NPC
from ..entity import Entity
from ..const import *


class Player(Entity):
    def __init__(self, game, pos, size, type):        
        super().__init__(game, pos, size, type)
        
        self.direction = 'down'
        self.speed = 110
        
        self.max_health = 6 # 2 health equals one whole heart, 1 equals half heart
        self.health = self.max_health
        self.strength = 1
        self.dexterity = 1 #use when there is a shield
        self.level = 1
        self.exp = 0
        self.next_level_exp = 5
        self.coins = 0
        self.inventory = []
        self.inventory.append([Sword(self, self.game.assets.sword), ITEM_AMOUNT_DEFAULT])
        
        self.collision_on = True
        
        self.last_movement = 0
        
        self.animation_timer = 0.13
        
        self.weapon_type = 'sword'
        self.weapon = None
        self.attacking = False
        self.attack_timer = 0
        
    @property
    def img(self):
        img = super().img
        return img
    
    @property
    def attack_value(self):
        return self.strength * Sword.damage_amt
        
    def move(self, dt):
        movement = [0, 0]
        if self.game.input.up_pressed:
            self.direction = 'up'
            movement[1] -= self.speed * dt 
        elif self.game.input.down_pressed:
            self.direction = 'down'
            movement[1] += self.speed * dt
        elif self.game.input.left_pressed:
            self.direction = 'left'
            movement[0] -= self.speed * dt
        elif self.game.input.right_pressed:
            self.direction = 'right'
            movement[0] += self.speed * dt
        return movement

    
    def pickup(self, item):
        if len(self.inventory) <= MAX_INVENTORY_SIZE:
            for inv_item in self.inventory:
                if type(inv_item[0]) is type(item):
                    inv_item[1] += ITEM_AMOUNT_DEFAULT
                    self.game.object_mapper.objects.remove(item)
                    return
                
        self.inventory.append([item, ITEM_AMOUNT_DEFAULT])
        self.game.object_mapper.objects.remove(item)
        
            
    def attack(self):
        if not self.attacking and self.weapon_type == 'sword':
            self.attacking = True
            self.attack_timer = 0
            self.frame_index = 3
            self.weapon = Sword(self, self.game.assets.sword)
    
    def reset_attack(self, dt, timer):
        if self.attacking:
            self.attack_timer += dt
            if self.attack_timer >= timer:
                self.attacking = False
                self.attack_timer = 0
                return True
    
    def check_level_up(self):
        if self.exp >= self.next_level_exp:
            self.level += 1
            self.exp = 0
            self.next_level_exp *= 2
            self.max_health += 2 # one health
            self.strength += 1
            self.dexterity += 1
            # level up dialogue
            self.game.state.set_state('dialogue')
            self.game.state.set_event('Level up')
            self.game.ui.current_dialogue = 'You are now level ' + str(self.level) + '!\nYou feel stronger than before!'
            
    def interact_with_npc(self, npc):
        dis = self.get_distance(npc)
        if dis <= npc.interact_range:
            if self.game.input.interacted:
                self.game.state.set_state('dialogue')
                if npc.can_turn: 
                    npc.turn_to_player(self)
                npc.speak()
                self.game.state.interacted_npc = npc
        
    def animation_update(self, dt):
        if self.game.input.pressed: 
            super().animation_update(dt)
        else:
            self.frame_num = 0
            self.frame_index = 0
    
    def update(self, dt):
        dead = self.check_death(dt)
            
        if not self.attacking:
            movement = self.move(dt)
        
            self.pos[0] += movement[0]
            self.pos[1] += movement[1]
            self.pos = [round(self.pos[0]), round(self.pos[1])]
            
            self.animation_update(dt)
            
            self.game.collision_manager.check_tile(self)
            self.game.events.events()
            
            for obj in self.game.object_mapper.objects:
                if self.on_screen(obj, self.game.scroll, self.game.window.display):
                    collided_obj = self.game.collision_manager.check_object(self, obj)
                    if collided_obj:
                        self.pickup(collided_obj)
                        self.game.ui.draw_ui_message('x1 ' + str(collided_obj.type).title() + '!')
            
            other_entities = (npc for npc in self.game.entities if npc.type != 'player')
            for entity in other_entities:
                if self.on_screen(entity, self.game.scroll, self.game.window.display):
                    collided = self.game.collision_manager.check_entity(self, entity)
                    if collided and collided.type in MONSTERS and not collided.death_timer: # if monster collides with player
                        self.damage(collided.attack_value)
                    if isinstance(entity, NPC):
                        self.interact_with_npc(entity)
                        
            self.reset_invincible(dt)
                    
            if self.game.input.action:
                self.attack()
        else:  
            if self.weapon:
                remove = self.weapon.update(dt)
                if remove:
                    self.weapon = None
    
        return dead
                    

    def render(self, surf, offset=(0, 0)):
        if self.direction in {'up', 'left', 'right'} and self.weapon:
            self.weapon.render(surf, offset=offset)
        super().render(surf, offset=offset)
        if self.direction == 'down' and self.weapon:
            self.weapon.render(surf, offset=offset) 
        
        
        
        
