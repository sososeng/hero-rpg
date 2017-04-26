from Characters import Character
import Sword
import Tonic
import random
import time

class Snake(Character):
    def __init__(self):
        self.name = 'snake'
        self.health = 20
        self.power = 5
        self.coins = 20
        self.bounty = 100
        self.armor =0
        self.evade = 0


    def attack(self, enemy):
        if not self.alive():
            return
        attacktwice = random.choices([0,1],[0.5,0.5])
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(self.power)
        if attacktwice[0]:
            print("{} attacks again{}".format(self.name, enemy.name))
            enemy.receive_damage(self.power)
        time.sleep(1.5)