"""
Exercise 10: Get mean character height per film
===============================================

𝙂𝙤𝙖𝙡𝙨:
- Get the mean character height per film, ignoring those with
  unknown heights.

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `characters_by_film` (see previous)
- `statistics`
"""


def mean_character_height_by_film(data):
    """Get mean character height per film.

    ⚠ Types are just to emphasize the exercise!

    :param data: Starwars dataset

    :return: Mapping between film IDs and the associated
             average height.
    :rtype: dict[FilmId, float]
    """
