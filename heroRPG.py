#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

hero_health = 10
hero_power = 5
goblin_health = 6
goblin_power = 2

class Hero:
    def __init__(self, name):
        self.name = name
        self.hero_health = 10
        self.hero_power = 5
    def attack(self):
        global goblin_health
        goblin_health -= hero_power
        print("You do {} damage to the goblin.".format(hero_power))
        if goblin_health <= 0:
            print("The goblin is dead.")
    def alive(self):
        if self.hero_health > 0:
            return True
        else:
            return False


class Goblin:
    def __init__(self, name):
        self.name = name
        self.goblin_health = 6
        self.goblin_power = 2 
        
    def attack(self):
        global hero_health
        hero_health -= goblin_power
        print("The goblin does {} damage to you.".format(goblin_power))
        if hero_health <= 0:
            print("You are dead.")
    def alive(self):
        if self.goblin_health > 0:
            return True
        else:
            return False







def main():

    goblin = Goblin("goblin")
    hero = Hero("hero")

    while goblin.alive() and hero.alive():
        print("You have {} health and {} power.".format(hero_health, hero_power))
        print("The goblin has {} health and {} power.".format(
            goblin_health, goblin_power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            Hero.attack(Goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin_health > 0:
            # Goblin attacks hero
            Goblin.attack(Hero)

main()
