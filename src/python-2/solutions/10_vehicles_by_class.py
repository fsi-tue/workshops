"""
Exercise 10: Who's in what class?
=================================

𝙂𝙤𝙖𝙡𝙨:
- Group all vehicles by their vehicles classes.

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `collections`
"""
from collections import defaultdict


def vehicles_by_class(data):
    """Get all vehicles grouped by their classes.

    ⚠ Types are just to emphasize the exercise!

    :param data: Starwars dataset

    :return: Grouped vehicles
    :rtype: dict[VehicleClass, list[Vehicle]]
    """
    res = defaultdict(list)
    for vehicle in data["vehicles"].values():
        res[vehicle["vehicle_class"]].append(vehicle)
    return res
