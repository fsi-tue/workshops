"""
Exercise 9: Who's the longest?!
===============================

𝙂𝙤𝙖𝙡𝙨:
- Get the longest vehicle per class.
- Ignore those with unknown size.

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `max`
"""


def longest_vehicle(data):
    """Get longest vehicle per class.

    ⚠ Types are just to emphasize the exercise!

    :param data: Starwars dataset

    :return: Vehicles counts per class.
    :rtype: Vehicle
    """
    return max(
        (
            vehicle
            for vehicle in data["vehicles"].values()
            if vehicle["length"] != "unknown"
        ),
        key=lambda p: float(p["length"])
    )
