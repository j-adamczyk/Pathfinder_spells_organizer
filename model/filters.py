from model.character_spellbook import CharacterSpellbook
import copy


class Filter:

    def __init__(self, all_spellbooks):
        self.all_spellbooks = all_spellbooks
        self.spellbooks = copy(all_spellbooks)

    def delete_characters(self, characters_list):
        for character in characters_list:
            self.spellbooks.pop(character)

    def add_characters(self, characters_list):
        for character in characters_list:
            self.spellbooks[character] = self.all_spellbooks.get(character)
