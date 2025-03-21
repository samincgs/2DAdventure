from .object import Object

class HealthPotion(Object):
    def __init__(self, game, pos, size):
        super().__init__(game, pos, 'health_potion', size)
        self.value = 4
        self.name = 'Health Potion'
        self.item_description = f'[ Health Potion ]\n\nA magical potion that heals\nfor {self.value} HP.'
        self.is_consumable = True
    
    def use(self):
        # item effect
        self.game.player.health = min(self.game.player.max_health, self.game.player.health + self.value)
        
        # potion dialogue
        self.game.state.create_dialogue(message='You drank the ' + self.name + '!\nYou recovered some HP!', event='Heal up')