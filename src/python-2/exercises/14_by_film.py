"""
Exercise 14: Group anything by films
====================================

𝙂𝙤𝙖𝙡𝙨:
- Make the previous exercise more generic.
    - i.e. make it work for people, starships, etc.

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `collections`
"""


def by_film(data, film_field, data_field):
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
