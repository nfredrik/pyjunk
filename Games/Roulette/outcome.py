"""
Outcome contains a single otcome on which a bet  can be placed.
"""


class Outcome(object):
    def __init__(self, name, odds):
        """
        Sets the instance name and odds from the parameter name and odds
        """
        self.name = name
        self.odds = odds
#        self.hash = self.name ^ self.odds
#        self.hash = int(self.name, 10) & self.odds
        self.hash = odds

    def win_amount(self, amount):
        """
        Multiply this Outcome's odds by the given amount. The product
        is returned.
        """
        return amount * self.odds

    def __eq__(self, other):
        """
        Compare the name attributes of self and other
        """
        return self.name == other

    def __ne__(self, other):
        """
        Compare the name attributes of self and other
        """
        return self.name != other

    def __hash__(self):
        return self.hash

    def __str__(self):
        """
        Easy-to-read representation of this outcome
        """
        return "%s (%d:1)" % (self.name, self.odds)
