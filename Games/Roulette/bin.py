class Bin(object):
    def __init__(self, * outcomes):
        self.outcomes = frozenset(outcomes)
    
    def add(self, outcome):
        self.outcomes |= set([outcome])

    def __str__(self):
        return ', '.join(map(str, self.outcomes))
