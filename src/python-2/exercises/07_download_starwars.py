"""
Exercise 7: Loading the entire data set
=======================================

𝙂𝙤𝙖𝙡𝙨:
- Download the entire data set based starting from the APIs roots

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `download_json` (see previous)
- `download_chain` (see previous)
- `do_parallel` (see previous)
- `clean_data` (see previous)
- `functools`
- `operator`
- *default argument values*
"""


def download_starwars(root):
    """Download and clean the entire starwars data set.

    :param root: The APIs root url
    :type root: str

    :return: The starwars data set.
    :rtype: Any
    """
