"""
Exercise 14: Group vehicles by films
====================================

𝙂𝙤𝙖𝙡𝙨:
- Get all vehicles grouped by films.
- Use a "human readable" key format
    - e.g. `Episode ⟨𝘌𝘗𝘐𝘚𝘖𝘋𝘌#⟩: ⟨𝘛𝘐𝘛𝘓𝘌⟩`

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `collections`
- *f-strings*
"""


def vehicles_by_film(data):
    """Get all characters by film.

    ⚠ Types are just to emphasize the exercise!

    :param data: Starwars dataset

    :return: Vehicles grouped by films.
    :rtype: dict[str, list[Vehicle]]
    """
