class Spell:
    """
    + school -pojedyncza (enumerator szkół)
    +subschool - lista (enumerator + mapa dla szkół)
    +descriptors -lista (enum)
    +poziom czaru - lista tupli  (clasa, level)
    +blood_line = lista tupli
    +domena -lista tupli (enumerator domen)
    +subdomain - lista tupli
    +elemental school - tupla
    +casting time (enum)
    +components - lista (object)
    +range - enum
    +area_and_target - object
    +efekt - string
    +duration - object
    +saving throw - obiekt
    -spell resistance - bool
    """

    def __init__(self, school=None, subschool=None, descriptors=None,
                 class_spell_level=None, bloodline=None, domain=None, subdomain=None,
                 elemental_school=None, casting_time=None, components=None,
                 spell_range=None, area_or_target=None, effect=None,
                 duration=None, dismissible = False, saving_throw=None, spell_resistance=None):
        self.school = school
        self.subschool = subschool
        self.descriptors = descriptors
        self.class_spell_level = class_spell_level
        self.bloodline = bloodline
        self.domain = domain
        self.subdomain = subdomain
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
