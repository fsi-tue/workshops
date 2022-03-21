"""
Exercise 11: Who's the longest, but per class?!
===============================================

𝙂𝙤𝙖𝙡𝙨:
- Get the biggest vehicle per class.
- Ignore those with unknown size.

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `collections`
"""
from collections import defaultdict


def longest_vehicle_per_class(data):
    """Get biggest vehicle per class.

    ⚠ Types are just to emphasize the exercise!

    :param data: Starwars dataset

    :return: Vehicles counts per class.
    :rtype: dict[VehicleClass, Vehicle]
    """
    res = defaultdict(lambda: {"length": "0"})
    for v in data["vehicles"].values():
        vclass = v["vehicle_class"]
        if (
            v["length"] != "unknown"
            and float(v["length"]) > float(res[vclass]["length"])
        ):
            res[vclass] = v
    return res
