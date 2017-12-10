from search.sundayCustom import SundayCustom


class Sunday2charCustom(SundayCustom):
    def __init__(self, text, pattern):
        super().__init__(text, pattern)

    def _incrementIterator(self, itr):
        if self.text[itr + self._patternLen:itr + self._patternLen + 2] not in self.pattern:
            return self._patternLen + 1
        else:
            return self.pattern[self._patternLen - 1::-1].index(
                self.text[itr + self._patternLen + 1:itr + self._patternLen - 1:-1]) + 2
