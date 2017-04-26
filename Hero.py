from Characters import Character
from Sword import Sword
from Tonic import Tonic
from Armor import Armor
import random
import time

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.armor =0
        self.evade = 0

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to {}!".format(self.health))
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

    def attack(self, enemy):
        if not self.alive():
            return
        damage = random.choices([self.power,self.power*2],[0.8,0.2])
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(damage[0])
        time.sleep(1.5)

    def loot(self, money):
        self.coins= self.coins + money