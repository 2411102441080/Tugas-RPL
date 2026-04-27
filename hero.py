# Game Hero sederhana
class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f"{self.name} menyerang {enemy.name} dengan serangan {self.attack}.")
        if enemy.health <= 0:
            print(f"{enemy.name} telah dikalahkan!")
        else:
            print(f"{enemy.name} masih memiliki {enemy.health} health.")
# Contoh penggunaan
hero1 = Hero("Argus", 100, 20)
hero2 = Hero("Badang", 80, 15)
hero1.attack_enemy(hero2)
