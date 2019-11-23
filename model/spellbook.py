from model.spell import Spell


class Spellbook:

    def __init__(self):
        self.spells_known = None

    def print_spells(self, level):
        if level:
            for spell in self.spells_known:
                print(spell)
