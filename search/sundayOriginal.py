from search.patternSearch import PatternSearch


class SundayOriginal(PatternSearch):
    def __init__(self, text, pattern):
        super().__init__(text, pattern)
        self.dictionary = {}
        self._prepareDictionary()

    def search(self):
        itr = 0
        while itr <= len(self.text) - self._patternLen:
            if self.matchesAt(self.text, itr, self.pattern):
                return itr
            else:
                itr += self._incrementIterator(itr)
        return 'NaN'

    def _incrementIterator(self, itr):
        if self.dictionary.get(self.text[itr + self._patternLen]) is None:
            return self._patternLen + 1
        else:
            return self._patternLen - self.dictionary[self.text[itr + self._patternLen]]

    def _prepareDictionary(self):
        for id, letter in enumerate(self.pattern):
            self.dictionary[letter] = id
