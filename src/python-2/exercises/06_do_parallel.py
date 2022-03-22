"""
Exercise 6: Doing things in parallel
====================================

𝙂𝙤𝙖𝙡𝙨:
- Do a given task for a set of parameters *"in parallel"*

𝙍𝙚𝙘𝙤𝙢𝙢𝙚𝙣𝙙𝙚𝙙 𝙡𝙞𝙗𝙧𝙖𝙧𝙞𝙚𝙨:
- `concurrent.futures`
"""

def do_parallel(task, args):
    """Do a single task for different inputs in parallel.

    :param task: function representing the task to do
    :type task: Callable[[Args], T]

    :param args: list of all argument sets to run
    :type args: list[Args]

    :return: dictionary of task results
    :rtype: dict[Args, T]
    """
