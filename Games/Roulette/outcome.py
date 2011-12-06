class Outcome(object):
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds
#        self.hash = self.name ^ self.odds
#        self.hash = int(self.name, 10) & self.odds
        self.hash = odds
    def winAmount(self, amount):
        return amount * self.odds

    def __eq__(self, other):
        return self.name == other

    def __ne__(self, other):
        return self.name != other

    def __hash__(self):
        return self.hash

    def __str__(self):
        return "%s (%d:1)" % (self.name, self.odds)
