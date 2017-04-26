from Tonic import Tonic
from SuperTonic import SuperTonic
from EvadeTonic import EvadeTonic
from Sword import Sword
from Hero import Hero

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic(), Sword(), SuperTonic(), EvadeTonic()]
    def do_shopping(self, hero):
        while True:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            count =1
            for item in self.items:
                print("{}. buy {} ({})".format(count, item.name, item.cost))
                count +=1
            print("10. leave")
            keyinput = int(input("> "))
            if keyinput == 10:
                break
            else: 
                hero.buy(self.items[keyinput-1])