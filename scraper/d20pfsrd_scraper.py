from bs4 import BeautifulSoup
from model.spell import Spell
from model.spell_elements import SpellElements
import re
import requests


def get_page_content(page_address):
    request = requests.get(page_address)

    if request.status_code != requests.codes.ok:
        raise ConnectionError("Page", page_address, "returned status code",
                              request.status_code)

    return request.content


def get_spells_urls(page_address):
    """
    Gets list of spells URLs from "main" spell page.
    :param page_address: URL address of page with spell links
    :return: list of strings (URLs)
    """
    text = str(get_page_content(page_address))

    # spell names in hyperlinks may contain:
    # letters, digits, dashes
    urls = re.findall(
        r'<a href="https://www.d20pfsrd.com/magic/all-spells/[a-z]/[a-zA-Z0-9-]*/">',
        text)

    urls = [link[9: len(link) - 2] for link in urls]

    return urls


def parse_header(header):
    header_info = dict()
    header = header.replace(",", "").split(';')

    for elems in header:
        elems = elems.split()

        if elems[0] == "School":  # school, subschool, descriptors
            header_info["school"] = elems[1]

            if len(elems) == 2:
                # (subschool))
                if elems[2].startswith("("):
                    header_info["subschool"] = elems[2]

                # [descriptor1, descriptor2, ...]
                else:
                    descriptors = elems[2][1:-1].split()
                    header_info["descriptors"] = descriptors
            else:  # len(elems) == 3
                descriptors = elems[3][1:-1].split()
                header_info["descriptors"] = descriptors

        elif elems[0] == "Level":
            # check for "unchained summoner" and "vampire hunter" classes
            # space in name produces problems, so resolve it by hand
            new_elems = []
            for val in elems:
                if val == "unchained":
                    new_elems.append("unchained summoner")
                elif val == "vampire":
                    new_elems.append("vampire hunter")
                elif val in {"summoner", "hunter"}:
                    pass
                else:
                    new_elems.append(val)

            elems = new_elems

            class_spell_level = dict()
            i = 1
            while i + 1 < len(elems):
                character_class = elems[i]
                spell_level = elems[i + 1]
                class_spell_level[character_class] = spell_level
                i += 2
            header_info["class_spell_level"] = class_spell_level

        elif elems[0] == "Bloodline":
            bloodlines = dict()
            i = 1
            while i + 1 < len(elems):
                bloodline = elems[i]
                spell_level = elems[i + 1]
                bloodlines[bloodline] = spell_level
                i += 2
            header_info["bloodlines"] = bloodlines

        elif elems[0] == "Domain":
            domains = dict()
            i = 1
            while i + 1 < len(elems):
                domain = elems[i]
                spell_level = elems[i + 1]
                domains[domain] = spell_level
                i += 2
            header_info["domains"] = domains

        elif elems[0] == "Subdomain":
            subdomains = dict()
            i = 1
            while i + 1 < len(elems):
                subdomain = elems[i]
                spell_level = elems[i + 1]
                subdomains[subdomain] = spell_level
                i += 2
            header_info["subdomains"] = subdomains

        elif elems[0] == "Elemental":  # Elemental School
            header_info["elemental_school"] = (elems[2], elems[3])

    return header_info


def parse_casting(casting):
    casting_info = dict()
    elems = casting.split()

    i = 1
    while i < len(elems):
        print(elems[i])


"""
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
"""
def get_spell(page_address):
    text = get_page_content(page_address)
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text()

    spell_name = soup.title.string.split()
    spell_name = spell_name[:-2]  # remove "- D20PFSRD"
    spell_name = ' '.join(spell_name)

    spells = re.findall(r'(School[\s\S]*?)' + spell_name, text)

    spells.extend(
        re.findall(r'(School[\s\S]*?)(?:Section 15:|This is our PF1)', text))

    for spell in spells:
        lines = spell.split("\n")
        header = lines[0]
        casting = []
        effect = []
        description = []

        i = 1
        while "EFFECT" not in lines[i]:
            casting.append(lines[i])
            i += 1

        while "DESCRIPTION" not in lines[i]:
            effect.append(lines[i])
            i += 1

        try:
            while "Mythic" not in lines[i]:
                description.append(lines[i])
                i += 1
        except IndexError:  # no Mythic version:
            mythic = None
        else:
            mythic = '\n'.join((lines[i:])[1:])

        casting = casting[1:]
        effect = effect[1:]
        description = '\n'.join(description[1:])

        #header_info = parse_header(header)
        casting_info = parse_casting(casting)
        #effect_info = parse_effect(effect)



get_spell("https://www.d20pfsrd.com/magic/all-spells/f/fey-form/")
