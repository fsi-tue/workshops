"""
Exercise 8: Loading the entire data set (but less annoying for swapi.dev)
=========================================================================

𝙂𝙤𝙖𝙡𝙨:
- Download the data and store it as a file
- Load the data from a file instead of downloading it if the
  file exists.

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `download_starwars` (see previous)
- `pathlib`
- `json`
- `open`
"""
from pathlib import Path
import json


def load_starwars(path="starwars.json", root="https://swapi.dev/api"):
    """Download and clean the entire starwars data set.

    :param path: File path to JSON file.
    :type path: str

    :param root: The APIs root url
    :type root: str

    :return: The starwars data set.
    :rtype: Any
    """
    if Path(path).is_file():
        with open(path, "r") as f:
            return json.load(f)
    else:
        data = download_starwars(root)
        with open(path, "w+") as f:
            json.dump(data, f)
    return data
