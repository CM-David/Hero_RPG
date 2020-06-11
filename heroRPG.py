#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

# hero_health = 10
# hero_power = 5
# goblin_health = 6
# goblin_power = 2



import random

global displayStatus 
displayStatus = False

class Character:
    def __init__(self, health, power, name, coins, armor):
        self.health = health
        self.power = power
        self.name = name
        self.coins = coins
        self.armor = armor

    def attack(self, othercharacter):
        othercharacter.health -= self.power
        print("{} do {} damage to the {}.".format(self.name, self.power, othercharacter.name))
        if othercharacter.health <= 0:
            print("{} has been defeated!".format(othercharacter.name))

    def alive(self):
        while self.health > 0:
            return True
        else:
            return False

    def status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

    def setHealth(self, health):
        self.health = health 

    def getHealth(self):
        return self.health

class Hero(Character):
    def __init__(self, power, health, name, coins, armor):
        super().__init__(power, health, name, coins, armor)

    def attack(self, othercharacter):
        self.damage = self.power * self.crit() - othercharacter.armor
        othercharacter.setHealth(othercharacter.getHealth() - self.damage)
        print(f"{self.name} has dealt {self.damage} to {othercharacter.name}")
        if othercharacter.health <= 0:
            print(f"{othercharacter.name} has been defeated!")
            self.coins += othercharacter.coins
            print(f"You have found {othercharacter.coins} coins!!")
    
    def alive(self):
        while self.health > 0:
            return True
        else:
            print("You suck try again!")
            exit()
            return False

    def crit(self):
        self.critDamage = 1
        critChance = random.randint(1, 5)
        if critChance == 2:
            print(f'{self.name} has landed a critical blow against!')
            self.critDamage = 2
            return self.critDamage
        else:
            self.critDamage = 1
            return self.critDamage

    def buy(self, item):
        if self.coins >= item.cost:
            self.coins -= item.cost
            item.apply(self)
        else:
            print("You don't have enough coins to purchase this item!")

class Goblin(Character):
    pass

class Zombie(Character):
    def __init__(self, power, health, name, coins, armor):
        super().__init__(power, health, name, coins, armor)
    
    def alive(self):
        return True

    def setHealth(self, health):
        return


class Medic(Character):
    def __init__(self, power, health, name, coins, armor):
        super().__init__(power, health, name, coins, armor)

    def heal(self):
        healChance = random.randint(1, 5)
        if healChance == 5:
            self.health += 8
            print('Blessed by RNGsus, doc has healed!\n')

class Shade(Character):
    def __init__(self, power, health, name, coins, armor):
        super().__init__(power, health, name, coins, armor)

class Barbarian(Character):
    def __init__(self, power, health, name, coins, armor):
        super().__init__(power, health, name, coins, armor)

    def attack(self, othercharacter):
        self.power = random.randint(12, 31)
        othercharacter.health -= self.power
        print("{} does {} damage to the {}.".format(self.name, self.power, othercharacter.name))
        if othercharacter.health <= 0:
            print("{} has been defeated!".format(othercharacter.name))

class SuperTonic:
    def __init__(self):
        self.cost = 10
        self.name = "Health Regen"
    def apply(self, character):
        character.health += 25
        print("Your health has increased by 25!")

class Armor:
    def __init__(self):
        self.cost = 10
        self.name = "Spartan armor"
    def apply(self, character):
        character.armor += 4
        print("How did you damage this?")

class Autorifle:
    def __init__(self):
        self.cost = 40
        self.name = "Autorifle"
    def apply(self, character):
        character.power += 15
        print("Who wouldnt want an autorifle with no bullets......")


class Cortana:
    def __init__(self):
        self.cost = 5
        self.name = "Cortana"
    def apply(self, character):
        global displayStatus
        displayStatus = True
        print("Cortana now allows you to see more info on the battlefied")

class Store:
    tonic = SuperTonic()
    armor = Armor()
    autorifle = Autorifle()
    cortana = Cortana()
    items = [tonic, armor, autorifle, cortana]
    def shop(self, PC):
        while True:    
            print("What do you want to do?")
            print("You have {} coins.".format(PC.coins))
            for i in range(len(self.items)):
                item = self.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("0. leave")
            raw_imp = int(input("> "))
            if raw_imp == 0:
                break
            else:
                ItemToBuy = Store.items[raw_imp - 1]
                item = ItemToBuy
                PC.buy(item)
    def shopping(self, character):
        print("You see a shop")
        print("Will you go shopping?")
        print("1. Shop till you drop")
        print("2. Keep kicking ass")
        store_status = int(input())
        if store_status == 1:
            self.shop(character)     

# Obj name = Class(HP, Power, Name, Money, Armor)
masterchief = Hero(100, 12, "Master Chief", 10, 0)
goblin = Goblin(30, 9, "Goblin is a goblin", 50, 0)
rick = Zombie(50, 7, "Rick finally got turned", 25, 4)
doc = Medic(100, 13, "Doc got the heals", 35, 3)
stranger = Shade(1, 18, "Stranger doesnt have time to explain", 50, 0)
conan = Barbarian(150, 0, "Conan the Barbarian", 75, 2)
store = Store()


def main():

    while masterchief.alive() and goblin.alive():
        print("What do you want to do?")
        print("1. Fight {}".format(goblin.name))
        print("2. Do Nothing")
        print("3. Flee from {}".format(goblin.name))
        if displayStatus == True:
            print("4. Ask cortana")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1": 
            masterchief.attack(goblin)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("You flee from {}.".format(goblin.name))
            break
        elif raw_input == "4":
            if displayStatus == True:
                print(masterchief.status())
                print(goblin.status())
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0:
            goblin.attack(masterchief)


    store.shopping(masterchief)

    while masterchief.alive() and rick.alive():    
        print("What do you want to do?")
        print("1. Fight {}".format(rick.name))
        print("2. Do nothing")
        print("3. Flee from {}".format(rick.name))
        if displayStatus == True:
            print("4. Ask cortana")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            masterchief.attack(rick)
        elif raw_input == "2":
            pass
            print("{} is trying figure out where carl is".format(rick.name))
        elif raw_input == "3":
            print("You flee from {}.".format(rick.name))
            break    
        elif raw_input == "4":
            if displayStatus == True:
                print(masterchief.status())
                print(rick.status())
        else:
            print("Invalid input {}".format(raw_input))
        if rick.health > 0:
            rick.attack(masterchief)

    store.shopping(masterchief)


    while masterchief.alive() and doc.alive():
        print("What do you want to do?")
        print("1. Fight {}".format(doc.name))
        print("2. Do Nothing")
        print("3. Flee from {}".format(doc.name))
        if displayStatus == True:
            print("4. Ask cortana")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            masterchief.attack(doc)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("You flee from {}.".format(doc.name))
            break
        elif raw_input == "4":
            if displayStatus == True:
                print(masterchief.status())
                print(doc.status())


        else:
            print("Invalid input {}".format(raw_input))

        if doc.health > 0:
            doc.attack(masterchief)
            doc.heal()

    store.shopping(masterchief)

    while masterchief.alive() and stranger.alive():    
        print("What do you want to do?")
        print("1. Fight {}".format(stranger.name))
        print("2. Do nothing")
        print("3. Flee from {}".format(stranger.name))
        if displayStatus == True:
            print("4. Ask cortana")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            dodgeChance = random.randint(1, 10)
            if dodgeChance == 2:
                masterchief.health -= stranger.power
                masterchief.attack(stranger)
            else: print("{} swung and {} dodged!".format(masterchief.name, stranger.name))
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("You flee from {}.".format(stranger.name))
            break
        elif raw_input == "4":
            if displayStatus == True:
                print(masterchief.status())
                print(stranger.status())
        else:
            print("Invalid input {}".format(raw_input))
        
        if stranger.health > 0:
            stranger.attack(masterchief)

    store.shopping(masterchief)


    while masterchief.alive() and conan.alive():
        print("What do you want to do?")
        print("1. Fight {}".format(conan.name))
        print("2. Do nothing")
        print("3. Flee from {}".format(conan.name))
        if displayStatus == True:
            print("4. Ask cortana")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            masterchief.attack(conan)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("You flee from {}.".format(conan.name))
            break
        elif raw_input == "4":
            if displayStatus == True:
                print(masterchief.status())
                print(conan.status()) 
        else:
            print("Invalid input {}".format(raw_input))

        if conan.health > 0:
            conan.attack(masterchief)
        elif conan.health <= 0:
            print("congrats you have defeated everyone, go get so rest and prepare for the sequel")
            print('''                              ,.        ,.      ,.
                                ||        ||      ||  ()
 ,--. ,-. ,.,-.  ,--.,.,-. ,-.  ||-.,.  ,.|| ,-.  ||-.,. ,-. ,.,-.  ,--.
//`-'//-\\||/|| //-||||/`'//-\\ ||-'||  ||||//-\\ ||-'||//-\\||/|| ((`-'
||   || |||| ||||  ||||   || || ||  || /|||||| || ||  |||| |||| ||  ``.
\\,-.\\-//|| || \\-||||   \\-|| ||  ||//||||\\-|| ||  ||\\-//|| || ,-.))
 `--' `-' `' `'  `-,|`'    `-^-``'  `-' `'`' `-^-``'  `' `-' `' `' `--'
                  //           .--------.
              ,-.//          .: : :  :___`.
              `--'         .'!!:::::  \\_\ `.
                      : . /%O!!::::::::\\_\. \
                     [""]/%%O!!:::::::::  : . \
                     |  |%%OO!!::::::::::: : . |
                     |  |%%OO!!:::::::::::::  :|
                     |  |%%OO!!!::::::::::::: :|
            :       .'--`.%%OO!!!:::::::::::: :|
          : .:     /`.__.'\%%OO!!!::::::::::::/
         :    .   /        \%OO!!!!::::::::::/
        ,-'``'-. ;          ;%%OO!!!!!!:::::'
        |`-..-'| |   ,--.   |`%%%OO!!!!!!:'
        | .   :| |_.','`.`._|  `%%%OO!%%'
        | . :  | |--'    `--|    `%%%%'
        |`-..-'| ||   | | | |     /__\`-.
        \::::::/ ||)|/|)|)|\|           /
---------`::::'--|._ ~**~ _.|----------( -----------------------
           )(    |  `-..-'  |           \    ______
           )(    |          |,--.       ____/ /  /\\ ,-._.-'
        ,-')('-. |          |\`;/   .-()___  :  |`.!,-'`'/`-._
       (  '  `  )`-._    _.-'|;,|    `-,    \_\__\`,-'>-.,-._
        `-....-'     ````    `--'      `-._       (`- `-._`-.")''')
    


main()


