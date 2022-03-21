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
from collections import defaultdict


def vehicles_by_film(data):
    """Get all characters by film.

    ⚠ Types are just to emphasize the exercise!

    :param data: Starwars dataset

    :return: Vehicles grouped by films.
    :rtype: dict[str, list[Vehicle]]
    """
    res = defaultdict(list)
    for film_id, film in data["films"].items():
        episode = (int(film_id) + 2) % 6 + 1
        key = f"Episode {episode}: {film['title']}"
        for vehicle_id in film["vehicles"]:
            res[key].append(data["vehicles"][vehicle_id])
    return res
