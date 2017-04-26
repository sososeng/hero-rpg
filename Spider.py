from Characters import Character
import Sword
import Tonic
import random
import time

class Spider(Character):
    def __init__(self):
        self.name = 'spider'
        self.health = 20
        self.power = 5
        self.coins = 20
        self.bounty = 100
        self.armor =0
        self.evade = 0

    def attack(self, enemy):
        if not self.alive():
            return
        damage = random.choices([self.power,self.power*5],[0.9,0.1])
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(damage[0])
        time.sleep(1.5)
        