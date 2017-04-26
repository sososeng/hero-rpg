from Characters import Character
import Sword
import Tonic
import random
import time

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.bounty = 10
        self.armor =0
        self.evade = 0





    def receive_damage(self, points):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            print("{} is dead.".format(self.name))
        recup = random.choices([0,2],[0.8,0.2])
        if recup[0] == 2:
            self.health += recup[0]
            print("Recuperate 2 health points.")