"""
Exercise 4: URLs are ugly data...
=================================

𝙂𝙤𝙖𝙡𝙨:
- Get rid of those ugly URLs...

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `re`
"""
import re


def url_to_id(string):
    """Extract the ID out of a given string.

    :param string: The string to extract the ID from.
    :type string: str

    :return: Either the extracted ID or the original string
    :rtype: str
    """
    if (m := re.match(
        r"^https://swapi\.dev/api/[^/]+/(\d+)+/$",
        string
    )):
        return m.groups()[0]
    else:
        return string