from Characters import Character
import random
import time
class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.bounty = 50
        self.armor =0
        self.evade = 0

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("{} swaps power with {} during attack".format(self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power