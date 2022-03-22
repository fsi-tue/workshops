"""
Exercise 5: Cleaning up our data
================================

𝙂𝙤𝙖𝙡𝙨:
- Map the URL removal over all our data
- Transform from list to dictionary (keyed by ID)
- Rename "url"-field to "id"-field

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙗𝙖𝙩𝙩𝙚𝙧𝙞𝙚𝙨:
- `url_to_id` (see previous)
- `isinstance`
- `del`
- *dictionary view objects*
"""


def clean_data(data):
    """Clean up and transform a given data set.

    :param data: Data set to clean and transform
    :type data: list[Any]

    :return: Cleaned and transformed data set.
    :rtype: dict[str, Any]
    """
