import random




class Weapon():
    def __init__(self): 
        weapons = ['sword', 'mace', 'dagger',]
        self.type = random.choice(weapons)
        if type == 'sword':
            self.damage_type = 'blade'
            self.min_damage = 2 
            self.max_damage = 9
        elif type == 'mace':
            self.damage_type = 'blunt'
            self.min_damage=  2
            self.max_damage = 9

        elif type == 'dagger':
            self.damage_type = 'blade'
            self.min_damage = 2 
            self.max_damage = 5 

class Monster(monster):
    
    def __init__(self):
        monsters = ['skeltals', 'giant rat', 'dragon']
        self.type = monster
        if type == 'skeltal':
            self.hp = 50 
            self.min_damage = 1
            self.max_damage = 5
        elif type == 'giant rat':
            self.hp = 30 
            self.min_damage = 1
            self.max_damage = 5
        else:
            self.hp = 100
            self.min_damage = 5
            self.max_damage = 12
            self.fire_attack_min = 20
            self.fire_attack_max = 40
                
