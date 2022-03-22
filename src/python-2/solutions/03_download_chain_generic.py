"""
Exercise 1: Download *complicated* things... (but more generic)
===============================================================

𝙂𝙤𝙖𝙡𝙨:
- Retrieve a chain of things (e.g. https://swapi.dev/api/people)
- Expose some functionality via function parameters (*callbacks*)

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `download_json` (see previous)
- *higher order functions*
"""


def download_chain(chain_link, get_result, url):
    """Download all links in a given chain.

    :param chain_link: function to determin the next link in
                       a chain
    :type chain_link: Callable[[Any], str]

    :param get_result: function to extract a list of relevant
                       data from each link
    :type get_result: Callable[[Any], list[T]]

    :param url: first link in the chain
    :type url: str

    :return: list of all results in a chain
    :rtype: list[T]
    """
    res = []
    while url is not None:
        data = download_json(url)
        res.extend(get_result(data))
        url = chain_link(data)
    return res
