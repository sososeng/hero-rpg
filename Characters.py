import random
import time
class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor =0
        self.evade = 0

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        evadevalue = 1*(1/(0.1 + self.evade))
        evadevalue = round(evadevalue)
        evading = random.choices([0,1],[evadevalue,1-evadevalue])
        if evading[0]:
            print("{} evaded the attack. ".format(self.name))
        else:
            self.health -= (points - self.armor)
            print("{} received {} damage.".format(self.name, points))
            if self.health <= 0:
                print("{} is dead.".format(self.name))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))