from Characters import Character
import Sword
import Tonic
import random
import time

class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 5
        self.coins = 20
        self.bounty = 15
        self.armor =0
        self.evade = 0




    def receive_damage(self, points):
        takedamage = random.choices([0,1],[0.9,0.1])
        if takedamage[0] == 1:
            self.health -= points
            print("{} received {} damage.".format(self.name, points))
            if self.health <= 0:
                print("{} is dead.".format(self.name))
        if takedamage[0] == 0:
            print("Missed.")