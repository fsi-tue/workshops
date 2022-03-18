"""
Exercise 9: Get all character by film
=====================================

𝙂𝙤𝙖𝙡𝙨:
- Get all character dictionaries for each film.

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `collections`
"""
from collections import defaultdict


def characters_by_film(data):
    """Get all characters by film.

    ⚠ Types are just to emphasize the exercise!

    :param data: Starwars dataset

    :return: Character dictionaries grouped by films.
    :rtype: dict[FilmId, list[CharDict]]
    """
    res = defaultdict(list)
    for film_id, film in data["films"].items():
        for character_id in film["characters"]:
            res[film_id].append(data["people"][character_id])
    return res
