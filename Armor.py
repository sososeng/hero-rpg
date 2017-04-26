
class Armor(object):
    cost = 6
    name = 'armor'
    def apply(self, character):
        character.armor = 2
        print("{}'s armor increased to {}.".format(character.name, character.armor))