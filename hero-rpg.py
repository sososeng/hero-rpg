#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character:

    def alive(self):
            if self.health > 0:
                return True
            else:
                return False

    def attack(self, enermy):
        enermy.health -= self.power
        print("You do {} damage to the {}.".format(self.power, enermy.__class__.__name__))
        if enermy.health <= 0:
            print("The {} is dead.".format(enermy.__class__.__name__))

    def print_status(self):
        print("{} have {} health and {} power.".format(self.__class__.__name__,self.health, self.power))


class Hero(Character):

    def __init__(self, health, power):
        self.health = health
        self.power = power



 

class Goblin(Character):

    def __init__(self, health, power):
        self.health = health
        self.power = power





def main():
    hero = Hero(10,5)

    goblin = Goblin(6,2)


    while goblin.alive() and hero.alive():

        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt == "1":
            # Hero attacks goblin
            hero.attack(goblin)

        elif inpt == "2":
            pass
        elif inpt == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid inpt {}".format(inpt))

        if goblin.health > 0:
            # Goblin attacks hero
           goblin.attack(hero)

if __name__ == "__main__":
  main()
