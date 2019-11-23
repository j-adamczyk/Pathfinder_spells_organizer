from model.spellbook import Spellbook
from model.spell import Spell
from exceptions import SpellNotForClassException


class CharacterSpellbook(Spellbook):

    def __init__(self, character):
        super.__init__()
        self.spells_known = {}
        self.character = character
        self.add_spells(self.character)

    def add_spells(self, character_class):
        for spell in spells:
            # TODO
            level = spell.find_spell_level(character_class)
            if level:
                self.spells_known[level].add(spell)
            else:
                raise SpellNotForClassException

    def print_spells(self, level):
        if level:
            for spell in self.spells_known:
                print(spell)
