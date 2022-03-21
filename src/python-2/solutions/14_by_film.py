"""
Exercise 14: Group anything by films
====================================

𝙂𝙤𝙖𝙡𝙨:
- Make the previous exercise more generic.
    - i.e. make it work for people, starships, etc.

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `collections`
"""
from collections import defaultdict


def by_film(data, film_field, data_field=None):
    """Group things by film.

    ⚠ Types are just to emphasize the exercise!

    :param data: Starwars dataset

    :param film_field: Name of "relation" field on a film.
    :type film_field: str

    :param data_field: Name of "data" field in dataset.
    :type data_field: str

    :return: Things grouped by films.
    :rtype: dict[str, list[Thing]]
    """
    data_field = data_field or film_field
    res = defaultdict(list)
    for film_id, film in data["films"].items():
        episode = (int(film_id) + 2) % 6 + 1
        key = f"Episode {episode}: {film['title']}"
        for vehicle_id in film[film_field]:
            res[key].append(data[data_field][vehicle_id])
    return res
