#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

# hero_health = 10
# hero_power = 5
# goblin_health = 6
# goblin_power = 2

class Character:
    def __init__(self, name, health = 10, power = 5):
        self.name = name
        self.health = health
        self.power = power
        
    def attack(self, enemy):
        enemy.health -= self.power
        if enemy.name == "goblin":
            print(f"You do {self.power} damage to the {enemy.name}.")
        elif enemy.name == "hero":
            print(f"The {self.name} does {self.power} damage to you.")
        if enemy.health <= 0:
            print(f"The {enemy.name} is dead.")
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        if self.name == "hero":
            print(f"You have {self.health} health and {self.power} power")
        if self.name == "goblin":
            print(f"The goblin has {self.health} health and {self.power} power")


class Hero(Character):
    def __init__(self, name = "hero", health = 10, power = 5):
        super().__init__(name = name, health = health, power = power)
    


class Goblin(Character):
    def __init__(self, name = "goblin", health = 6, power = 2):
        super().__init__(name = name, health = health, power = power)




def main():

    goblin = Goblin("goblin")
    
    hero = Hero("hero")

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
        if goblin.health <= 0:
            return (None)

main()


