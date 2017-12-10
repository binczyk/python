from search.sundayOriginal import SundayOriginal


class Sunday2charOriginal(SundayOriginal):
    def __init__(self, text, pattern):
        super().__init__(text, pattern)

    def _incrementIterator(self, itr):
        if self.dictionary.get(self.text[itr + self._patternLen:itr + self._patternLen + 2]) is None:
            return self._patternLen + 1
        else:
            return self._patternLen - self.dictionary[self.text[itr + self._patternLen:itr + self._patternLen + 2]]

    def _prepareDictionary(self):
        for id, letter in enumerate(self.pattern):
            self.dictionary[self.pattern[id:id + 2]] = id
