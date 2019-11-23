class Spell:
    """
    + school -pojedyncza (enumerator szkół)
    +subschool - lista (enumerator + mapa dla szkół)
    +descriptors -lista (enum)
    +poziom czaru - lista tupli  (clasa, level)
    -blood_line = lista tupli
    -domena -lista tupli (enumerator domen)
    -subdomain - lista tupli
    -elementar school - tupla
    -casting time (enum)
    -components - lista (object)
    -range - enum
    -area - object
    -target - string
    -efekt - string
    -duration - object
    -saving throw - obiekt
    -spell resistance - bool
    """
    def __init__(self, school, subschool, descriptors, class_spell_level,
                 bloodline, domain, subdomain, elemental_school,
                 casting_time, components, spell_range, area, target,
                 effect, duration, saving_throw, spell_resistance):
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
        self.area = area
        self.target = target
        self.effect = effect
        self.duration = duration
        self.saving_throw = saving_throw
        self.spell_resistance = spell_resistance

