import pygame

from scripts.objects.sword import Sword
from scripts.objects.key import Key
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
        self.inventory.append([Sword(game, (0, 0), (16, 16)), ITEM_AMOUNT_DEFAULT])
        
        self.collision_on = True
        
        self.last_movement = 0
        
        self.animation_timer = 0.13
        
        self.attacking = False
        self.attack_index = 0
        self.attack_num = 0
        self.attack_delay_timer = 0
        self.attack_delay = 0.33
        
        self.sword_damage_amt = 1
        self.weapon = 'sword'
        
    @property
    def img(self):
        img = super().img
        return img
    
    @property
    def weapon_img(self):
        img = self.images['attack' + '_' + self.direction][self.attack_index]
        return img
    
    @property
    def weapon_rect(self):
        return pygame.Rect(int(self.pos[0] + WEAPON_RECT[self.weapon]['offset'][self.direction][0]), int(self.pos[1] + WEAPON_RECT[self.weapon]['offset'][self.direction][1]), WEAPON_RECT[self.weapon]['size'][self.direction][0], WEAPON_RECT[self.weapon]['size'][self.direction][1])
    
    @property
    def attack_value(self):
        return self.strength * self.sword_damage_amt
        
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
        if not self.attack_delay_timer:
            self.attacking = True
    
    def reset_attack(self, dt):
        ANIMATION_DURATIONS = [0.08, 0.32]
        if self.attacking:
            self.attack_num += dt
            if self.attack_num <= ANIMATION_DURATIONS[0]:
                self.attack_index = 0
            elif self.attack_num <= ANIMATION_DURATIONS[1]:
                self.attack_index = 1
            else:
                self.attacking = False
                self.attack_index = 0
                self.attack_num = 0
                self.attack_delay_timer = self.attack_delay
        else:
            self.attack_delay = max(0, self.attack_delay_timer - dt)
            
    
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
            
        movement = self.move(dt)
        
        if self.game.input.action:
            self.attack()
    
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
        
        # attacking monsters
        if self.attacking:
            for monster in (monster for monster in self.game.entities if monster.type in MONSTERS): # if player sword hits any enemy
                if self.weapon_rect.colliderect(monster.rect):
                    if not monster.invincible:
                        self.game.ui.draw_ui_message(str(self.attack_value) + ' damage!')
                    monster.damage(self.attack_value)
                    monster.hp_bar_on = True
                    monster.hp_bar_counter = 0
                    opp_directions = {'right': 'left', 'left': 'right', 'up':'down', 'down': 'up'}
                    monster.direction = opp_directions[self.direction]
                    if monster.dead and not monster.death_message_shown:
                        self.exp += monster.exp
                        monster.death_message_shown = True
                        self.game.ui.draw_ui_message('killed the ' + monster.__class__.__name__ + '!')
                        self.game.ui.draw_ui_message('EXP gained: ' + str(monster.exp))
        
        # reset timers
        self.reset_invincible(dt)
        self.reset_attack(dt)
         
        return dead
                    

    def render(self, surf, offset=(0, 0)):
        if self.game.input.debug:
            pygame.draw.rect(surf, WHITE, pygame.Rect(self.rect.x - offset[0], self.rect.y - offset[1], self.rect.size[0], self.rect.size[1])) #debug
            pygame.draw.rect(surf, RED, pygame.Rect(self.weapon_rect.x - offset[0], self.weapon_rect.y - offset[1], self.weapon_rect.size[0], self.weapon_rect.size[1])) #debug
            
        img = self.img.copy()
        
        if self.invincible:
            if self.invincible_counter % 0.20 <= 0.1:
                img.set_alpha(self.alpha)  
            else:
                img.set_alpha(255)
    
        offset = self.render_offset(offset=offset)
 
        if self.dead:
            self.death_animation(img, surf, offset=offset)
        elif self.attacking:
            temp_pos = self.pos.copy()
            if self.direction == 'left':
                temp_pos[0] = self.pos[0] - TILE_SIZE
            elif self.direction == 'up':
                temp_pos[1] = self.pos[1] - TILE_SIZE
            img = self.weapon_img
            surf.blit(img, (int(temp_pos[0] - offset[0]), int(temp_pos[1] - offset[1])))
        else:       
            surf.blit(img, (int(self.pos[0] - offset[0]), int(self.pos[1] - offset[1])))
        
        
        
        
