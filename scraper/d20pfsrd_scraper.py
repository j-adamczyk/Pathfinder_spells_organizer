import re
import requests


def get_spells_urls(page_address):
    """
    Gets list of spells URLs from "main" spell page.
    :param page_address: URL address of page with spell links
    :return: list of strings (URLs)
    """
    request = requests.get(page_address)

    if request.status_code != requests.codes.ok:
        raise ConnectionError("Page", page_address, "returned status code",
                              request.status_code)

    # spell names in hyperlinks may contain:
    # letters, digits, dashes
    urls = re.findall(
        r'<a href="https://www.d20pfsrd.com/magic/all-spells/[a-z]/[a-zA-Z0-9-]*/">',
        request.text)

    urls = [link[9: len(link) - 2] for link in urls]

    return urls





hyperlinks = get_spells_urls("https://www.d20pfsrd.com/magic/all-spells/")

