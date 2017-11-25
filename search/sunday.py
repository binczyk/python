from search.patternSearch import PatternSearch


class Sunday(PatternSearch):
    _patternLen = 0

    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern
        self._patternLen = len(pattern)

    def search(self):
        itr = 0
        while itr <= len(self.text) - self._patternLen - 1:
            self.numberOfLoops += 1
            if self.text[itr:itr + self._patternLen] == self.pattern:
                return itr;
            else:
                itr += self._incrementIterator(itr)
        return 'NaN'

    def _incrementIterator(self, itr):
        if self.text[itr + self._patternLen] not in self.pattern:
            return self._patternLen + 1
        else:
            return self.pattern[self._patternLen - 1::-1].index(self.text[itr + self._patternLen]) + 1
