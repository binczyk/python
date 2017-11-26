from search.sunday import Sunday


class Sunday2char(Sunday):
    def __init__(self, text, pattern):
        super().__init__(text, pattern)

    # TODO coś tu nie działa do sprawdzenia. itr przeskakuje za koniec tekstu i się wypierdala
    def _incrementIterator(self, itr):
        if self.text[itr + self._patternLen:itr + self._patternLen + 2] not in self.pattern:
            return self._patternLen + 2
        else:
            return self.pattern[self._patternLen - 1::-1].index(
                self.text[itr + self._patternLen + 1:itr + self._patternLen - 1:-1]) + 2
