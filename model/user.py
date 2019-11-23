from model.user_spellbook import UserSpellbook


class User:
    def __init__(self, level, character, prepared=True):
        self.spellbook = UserSpellbook()
        self.level = level
        self.character = character
        self.prepared = prepared

