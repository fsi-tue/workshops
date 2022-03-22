"""
Exercise 2: Downloading *complicated* things...
===============================================

𝙂𝙤𝙖𝙡𝙨:
- Retrieve a chain of things (e.g. https://swapi.dev/api/people)

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `download_json` (see previous)
"""


def download_chain(url):
    """Download all links in a given chain.

    :param chain_link: function to determin the next link in
                       a chain
    :type chain_link: Callable[[Any], str]

    :return: list of all results in a chain
    :rtype: list[Any]
    """
    res = []
    while url is not None:
        data = download_json(url)
        res.extend(data["results"])
        url = data["next"]
    return res
