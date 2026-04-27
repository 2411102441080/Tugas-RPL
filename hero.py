# Game Hero sederhana
class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f"{self.name} menyerang {enemy.name} dengan serangan {self.attack}.")
        print(f"{enemy.name} memiliki sisa health {enemy.health}.")
# Contoh penggunaan
hero1 = Hero("Hero A", 100, 20)
hero2 = Hero("Hero B", 120, 15)
hero1.attack_enemy(hero2)
