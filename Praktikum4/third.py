from random import randint

class Soldier:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def set_name(self, name):
        self.name = name

    def attack(self, enemy):
        damage = randint(1, 10)
        print(f"{self.name} атакует {enemy.name} и наносит {damage} урона.")
        enemy.receive_damage(damage)

    def receive_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} получает урон. Здоровье: {self.health}")

class Battle:
    def __init__(self, soldier1, soldier2):
        self.soldier1 = soldier1
        self.soldier2 = soldier2
        self.result = None

    def battle(self):
        while self.soldier1.health > 0 and self.soldier2.health > 0:
            attacker = randint(1, 2)
            if attacker == 1:
                self.soldier1.attack(self.soldier2)
            else:
                self.soldier2.attack(self.soldier1)

        self.determine_winner()

    def determine_winner(self):
        if self.soldier1.health > self.soldier2.health:
            self.result = f"{self.soldier1.name} побеждает!"
        elif self.soldier2.health > self.soldier1.health:
            self.result = f"{self.soldier2.name} побеждает!"
        else:
            self.result = "Ничья!"

    def who_win(self):
        print(self.result)

soldier1 = Soldier("Солдат1", 50)
soldier2 = Soldier("Солдат2", 50)

battle_instance = Battle(soldier1, soldier2)
battle_instance.battle()
battle_instance.who_win()

soldier1_name = input("Введите имя первого солдата: ")
soldier2_name = input("Введите имя второго солдата: ")
soldier1_health = int(input("Введите начальное здоровье первого солдата: "))
soldier2_health = int(input("Введите начальное здоровье второго солдата: "))

soldier1.set_name(soldier1_name)
soldier1.health = soldier1_health

soldier2.set_name(soldier2_name)
soldier2.health = soldier2_health

battle_instance = Battle(soldier1, soldier2)
battle_instance.battle()
battle_instance.who_win()
