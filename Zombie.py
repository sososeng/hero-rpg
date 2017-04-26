from Characters import Character
import Sword
import Tonic
import random
import time

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.bounty = 5
        self.armor =0
        self.evade = 0


    def alive(self):
        return True