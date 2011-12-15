"""
Bin contains a collection of Outcomes which reflect the winning bets that
paid for a particular bin on Roulette wheel
"""


class Bin(object):
    def __init__(self, * outcomes):
        """
        Populate the Bin with one or more Outcomes
        """
        self.outcomes = frozenset(outcomes)

    def add(self, outcome):
        """
        Add and Outcome to the Bin
        """
        self.outcomes |= set([outcome])

    def __str__(self):
        """
        Easy-to-read representation of the list of Outcomes for this Bin
        """
        return ', '.join(map(str, self.outcomes))
