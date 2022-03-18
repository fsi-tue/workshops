"""
Exercise 11: Count vehicles by their class
==========================================

𝙂𝙤𝙖𝙡𝙨:
- Count the number of vehicles for all vehicle classes.

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `collections`
"""
from collections import Counter


def vehicles_per_class(data):
    """Count vehicles by their class.

    ⚠ Types are just to emphasize the exercise!

    :param data: Starwars dataset

    :return: Vehicles counts per class.
    :rtype: dict[VehicleClass, int]
    """
    return Counter(
        v["vehicle_class"]
        for v in data["vehicles"].values()
    )
