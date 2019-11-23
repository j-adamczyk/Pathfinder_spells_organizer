from bs4 import BeautifulSoup, SoupStrainer
from model.spell import Spell
from model.spell_elements import SpellElements
import re
import requests


def get_page_text(page_address):
    request = requests.get(page_address)

    if request.status_code != requests.codes.ok:
        raise ConnectionError("Page", page_address, "returned status code",
                              request.status_code)

    return request.text


def get_spells_urls(page_address):
    """
    Gets list of spells URLs from "main" spell page.
    :param page_address: URL address of page with spell links
    :return: list of strings (URLs)
    """
    text = get_page_text(page_address)

    # spell names in hyperlinks may contain:
    # letters, digits, dashes
    urls = re.findall(
        r'<a href="https://www.d20pfsrd.com/magic/all-spells/[a-z]/[a-zA-Z0-9-]*/">',
        text)

    urls = [link[9: len(link) - 2] for link in urls]

    return urls

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
    text = get_page_text(page_address)
    soup = BeautifulSoup(text, 'html.parser')
    text = soup.get_text

    spell_title = soup.title.string.split()[:-2]
    spell_title = spell_title[:-2]  # remove "- D20PFSRD"
    spell_title = ' '.join(spell_title)




get_spell("https://www.d20pfsrd.com/magic/all-spells/f/fey-form/")
