class EvadeTonic(object):
    cost = 5
    name = 'evadetonic'
    def apply(self, character):
        character.evade += 2
        print("{}'s evade points increased to {}.".format(character.name, character.evade))