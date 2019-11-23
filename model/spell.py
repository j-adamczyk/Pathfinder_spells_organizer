

class Spell:
    """
    + school -pojedyncza (enumerator szkół)
    +subschool - pojedyncza (enumerator + mapa dla szkół)
    +descriptors -set (enum)
    +poziom czaru - dict  (clasa, level)
    +blood_line = set tupli
    +domena -dict(nazwa,poziom czaru)
    +subdomain - dict(nazwa, poziom czaru)
    +elemental school - tupla
    +casting time obiekt
    +components - set (object)
    +range - obj
    +area_and_target - object
    +efekt - string
    +duration - object
    +saving throw - obiekt
    +spell resistance - bool
    """

    def __init__(self, name=None, school=None, subschool=None, descriptors=None,
                 class_spell_level=None, bloodline=None, domain=None,
                 subdomain=None, elemental_school=None, casting_time=None,
                 components=None, spell_range=None, area_or_target=None,
                 effect=None, duration=None, dismissible=False,
                 saving_throw=None, spell_resistance=None, mythic=False):
        self.name = name
        self.school = school
        self.subschool = subschool
        self.descriptors = descriptors
        self.class_spell_levels = class_spell_level
        self.bloodlines = bloodline
        self.domains = domain
        self.subdomains = subdomain
        self.elemental_school = elemental_school
        self.casting_time = casting_time
        self.components = components
        self.spell_range = spell_range
        self.area_or_target = area_or_target
        self.effect = effect
        self.duration = duration
        self.dismissible = dismissible
        self.saving_throw = saving_throw
        self.spell_resistance = spell_resistance
        self.mythic = mythic

    def find_spell_level(self, character_class):
        level = self.class_spell_levels.get(character_class)
        return level

    @staticmethod
    def find_spell(spell_name):
        # TODO
        return Spell()
