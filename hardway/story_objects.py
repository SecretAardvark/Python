import random






class Skeltal():
    def __init__(self):
        self.type = 'Skeltal'
        self.hp = 40 
        self.min_damage = 1
        self.max_damage = 5
    #def attack_player(self, player):


                
class Giant_rat():
    def __init__(self):
        self. type = 'Giant Rat'
        self.hp = 30
        self.min_damage = 1
        self.max_damage = 5

class Dragon():
    def __init__(self):
        self.type = 'Dragon'
        self.hp = 75
        self.min_damage = 3
        self.max_damage = 10
        self.fire_attack_min = 10
        self.fire_attack_max = 20


class player():
    def __init__(self,):
        self.hp = 100  
        self.has_potion = False
        self.weapon_type = 'Bare fists'
        self.min_damage = 1 
        self.max_damage = 3
    def player_weapon(self):
        weapons = ['sword', 'mace', 'dagger',]
        self.weapon_type = random.choice(weapons)
        if self.weapon_type == 'sword':
            self.damage_type = 'blade'
            self.min_damage = 3 
            self.max_damage = 9
        elif self.weapon_type == 'mace':
            self.damage_type = 'blunt'
            self.min_damage=  3
            self.max_damage = 9

        elif self.weapon_type == 'dagger':
            self.damage_type = 'blade'
            self.min_damage = 2 
            self.max_damage = 5 
    
    def get_potion(self):
        self.has_potion = True


