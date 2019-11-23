
class SpellElements:
    schools = {"abjuration", "conjuration", "divination", "enchantment",
               "evocation", "illusion", "necromancy", "transmutation"}

    subschools = {"calling", "creation", "healing", "summoning",
                  "teleportation", "scrying", "charm", "compulsion", "figment",
                  "glamer", "pattern", "phantasm", "shadow", "polymorph"}

    descriptors = {"acid", "air", "chaotic", "cold", "curse", "darkness",
                   "death", "disease", "draconic", "earth", "electricity",
                   "emotion", "evil", "force", "good", "language-dependent",
                   "lawful", "light", "mediative", "mind-affecting", "pain",
                   "poison", "ruse", "shadow", "sonic", "water"}

    classes = {"bard", "cleric", "druid", "paladin", "ranger", "sorcerer",
               "wizard", "inquisitor", "magus", "omdura", "oracle", "summoner",
               "witch", "vampire hunter", "arcanist", "bloodrager", "hunter",
               "shaman", "skald", "warpriest", "medium", "mesmerist",
               "occultist", "psychic", "spiritualist", "antipaladin"}

    bloodlines = {"unicorn sorcerer", "phoenix sorcerer", "salamander",
                  "shapechanger", "vestige sorcerer", "astral", "deep earth",
                  "aberrant", "abyssal", "accursed", "aquatic", "arcane",
                  "boreal", "celestial", "daemon", "destined","div", "djinni",
                  "draconic", "dreamspun", "ectoplasm", "efreeti", "elemental",
                  "fey", "ghoul", "harrow", "imperious", "impossible",
                  "infernal", "kobold", "maestro", "marid", "martyred",
                  "nanite", "oni", "orc", "pestilence", "possessed", "protean",
                  "psychic", "rakshasa", "scorpion", "serpentine", "shadow",
                  "shaitan", "solar", "starsoul", "stormborn", "undead",
                  "verdant", "vestige"}

    domains = {"air", "animal", "artifice", "chaos", "charm", "community",
               "darkness", "death", "destruction", "earth", "erosion", "evil",
               "fire", "glory", "good", "healing", "knowledge", "law",
               "liberation", "luck", "madness", "magic", "nobility", "plant",
               "protection", "repose", "rune", "scalykind", "strength", "sun",
               "travel", "trickery", "vermin", "vermin", "void", "war",
               "water", "weather"}

    subdomains = {"cloud", "lightning", "wind", "feather", "fur", "insect",
                  "alchemy", "construct", "industry", "toil", "trap", "azata",
                  "demodand", "demon", "entropy", "protean", "revelry", "riot",
                  "whimsy", "captivation", "love", "lust", "cooperation",
                  "education", "family", "home", "loss", "moon", "night",
                  "murder", "plague", "psychopomp", "undead", "catastrophe",
                  "hatred", "rage", "torture", "caves", "metal",
                  "petrification", "radiation", "cannibalism", "corruption",
                  "daemon", "devil", "fear", "kyton", "arson", "ash", "smoke",
                  "heroism", "honor", "hubris", "legend", "agathion", "archon",
                  "friendship", "redemption", "medicine", "resurrection",
                  "aeon", "espionage", "memory", "thought", "inevitable",
                  "judgment", "legislation", "loyalty", "slavery", "tyranny",
                  "freedom", "revolution", "self-realization", "curse", "fate",
                  "imagination", "insanity", "nightmare", "truth", "arcane",
                  "divine", "rites", "aristocracy", "leadership", "martyr",
                  "leshy", "decay", "growth", "thorns", "defense",
                  "fortifications", "purity", "solitude", "ancestors", "souls",
                  "ruins", "language", "wards", "dragon", "saurian", "venom",
                  "competition", "ferocity", "fist", "resolve", "day", "light",
                  "revelation", "thirst", "exploration", "portal", "trade",
                  "ambush", "deception", "greed", "innuendo", "thievery",
                  "dark tapestry", "isolation", "stars", "blood", "duels",
                  "tactics", "flotsam", "flowing", "ice", "oceans", "rivers",
                  "monsoon", "seasons", "storms"}

    elemental_schools = {"aether, air", "earth", "fire",
                         "metal", "void", "water", "wood"}

    casting_times = {"standard action", "move action", "full-round action",
                     "swift action", "immediate action", "free action"}

    component_letters = {"V", "S", "M", "F", "DF"}

    range_types = {"personal", "touch", "close",
                   "medium", "long", "unlimited", "other"}

    target_areas = {"single", "multiple", "area"}

    durations_names = {"instantaneous", "permanent", "concentration",
                       "discharge", "round", "minute", "hour"}

    saving_throw_types = {"fortitude", "reflex", "well"}

    saving_throw_effects = {"negates", "partial", "half", "disbelief"}


class Component:
    def __init__(self, letter, decription):
        self.letter = letter
        self.description = decription


class Range:
    def __init__(self, range_type, description):
        self.range_type = range_type
        self.description = description


class AreaOrTarget:
    def __init__(self, target, description):
        self.target = target
        self.description = description


class Duration:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration


class SavingThrow:
    def __init__(self, saving_throw_type, effect):
        self.saving_throw_type = saving_throw_type
        self.effect = effect




