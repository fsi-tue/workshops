"""
Exercise 15: How unique is a category in a film?
================================================

𝙂𝙤𝙖𝙡𝙨:
- Calculate the uniqueness of things in film.
- Show the results per film.

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `by_film` (see previous)
- `collections`
- `statistics`
- `decimal`
- `round`
"""


def uniqueness_per_film(data, film_field, data_field=None):
    """Get the uniqueness a things in a film by films.

    ⚠ Types are just to emphasize the exercise!

    :param data: Starwars dataset

    :param film_field: Name of "relation" field on a film.
    :type film_field: str

    :param data_field: Name of "data" field in dataset.
    :type data_field: str

    :return: Uniqueness or things by films.
    :rtype: dict[str, list[Thing]]
    """
    data_field = data_field or film_field
    return {
        film: round(mean(
            1 / Decimal(len(thing["films"]))
            for thing in things
        ), 2)
        for film, things in by_film(
            data,
            film_field,
            data_field
        ).items()
    }
