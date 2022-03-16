"""
Exercise 5: Loading the entire data set
=======================================

𝙂𝙤𝙖𝙡𝙨:
- Download the entire data set based starting from the APIs
  root
- Save the data set to a file
- Only perform the download if the file doesn't exist,
  otherwise load the file

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙡𝙞𝙗𝙧𝙖𝙧𝙞𝙚𝙨:
- `download_json` (see previous)
- `download_chain` (see previous)
- `do_parallel` (see previous)
- `json`
- `functools`
- `operator`
- `pathlib`
"""
from functools import partial
import json
from pathlib import Path
from operator import itemgetter


def load_starwars(path=Path("starwars.json")):
    """Download (and cache) the entire starwars data set.

    :param path: The path to the cached JSON-file.
    :type path: Path

    :return: The starwars data set.
    :rtype: Any
    """
    if path.is_file():
        with open(path, "r") as f:
            return json.load(f)
    else:
        endpoints = download_json("https://swapi.dev/api")
        data = do_parallel(
            partial(
                download_chain,
                itemgetter("next"),
                itemgetter("results")
            ),
            endpoints.values()
        )
        with open(path, "w+") as f:
            json.dump(data, f)
        return data
