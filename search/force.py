from search.patternSearch import PatternSearch


class Force(PatternSearch):
    def __init__(self, text, pattern):
        super().__init__(text, pattern)

    def search(self):
        for itr in range(len(self.text) - self._patternLen + 1):
            if self.matchesAt(self.text, itr, self.pattern):
                return itr
        return 'NaN'
