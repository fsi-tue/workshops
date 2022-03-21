"""
Exercise 16: 𝗙𝗜𝗡𝗔𝗟𝗟𝗬! Which film is the "uniquest"?
===================================================

𝙂𝙤𝙖𝙡𝙨:
- Calculate which starwars film is the most unique.

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `uniqueness_per_film` (see previous)
- `max`
- *Python's Data Model*
"""


def uniquest_film(data):
    """Get the uniquest film of them all!

    :param data: Starwars dataset

    :return: The name of the uniquest starwars film.
    :rtype: str
    """
    inidivdual_uniquenesses = [
        uniqueness_per_film(data, "vehicles"),
        uniqueness_per_film(data, "starships"),
        uniqueness_per_film(data, "planets"),
        uniqueness_per_film(data, "species"),
        uniqueness_per_film(data, "characters", "people"),
    ]
    res = inidivdual_uniquenesses[0]
    for uniquenesses in inidivdual_uniquenesses[1:]:
        for key, value in uniquenesses.items():
            res[key] += value
    return max(
        res.keys(),
        key=res.__getitem__
    )
