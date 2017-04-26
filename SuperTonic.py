
class SuperTonic(object):
    cost = 6
    name = 'supertonic'
    def apply(self, character):
        character.health = 10
        print("{}'s health increased to {}.".format(character.name, character.health))