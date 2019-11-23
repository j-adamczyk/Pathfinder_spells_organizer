from model.spellbook import Spellbook
from model.spell import Spell
from exceptions import SpellNotForClassException


class UserSpellbook(Spellbook):

    def add_spell(self, spell_name, character_class):
        spell = Spell.find_spell(spell_name)
        level = spell.find_spell_level(character_class)
        if level:
            self.spells_known[level].add(spell)
        else:
            raise SpellNotForClassException

    def print_spells(self, level):
        if level:
            for spell in self.spells_known:
                print(spell)
