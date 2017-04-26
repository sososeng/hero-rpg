#!/usr/bin/env python3

"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""

import time
from Hero import Hero
from Battle import Battle
from Goblin import Goblin
from Store  import Store
from Wizard import Wizard
from Spider import Spider
from Snake import Snake
from Medic import Medic
from Shadow import Shadow
from Zombie import Zombie





if __name__ == "__main__":
    hero = Hero()
    enemies = [Goblin(), Wizard(),Medic(),Shadow(),Zombie(), Spider(),Snake()]
    battle_engine = Battle()
    shopping_engine = Store()

    for enemy in enemies:
        hero_won = battle_engine.do_battle(hero, enemy)
        if not hero_won:
            print("YOU LOSE!")
            exit(0)
        shopping_engine.do_shopping(hero)

    print("YOU WIN!")