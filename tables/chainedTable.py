class ChainedTable:
    _EMPTY = 'EMPTY'
    _REMOVED = 'REMOVED'

    def __init__(self, LEN=16):
        self.LEN = LEN
        self.table = []
        for _ in range(LEN):
            self.table.append(self._EMPTY)

    def _hash(self, value):
        return abs(hash(value)) % self.LEN

    def exists(self, value):
        valueHash = self._hash(value)
        for itr in range(valueHash, self.LEN):
            if self.table[itr] == self._EMPTY:
                return
            if self.table[itr] == value:
                return True
        for itr in range(valueHash - 1):
            if self.table[itr] == self._EMPTY:
                return
            if self.table[itr] == value:
                return True
        return False

    def add(self, value):
        valueHash = self._hash(value)
        if not self.exists(value):
            for itr in range(valueHash, self.LEN):
                if self.chcekIfEmptyOrRemoved(itr):
                    self.table[itr] = value
                    return
            for itr in range(valueHash - 1):
                if self.chcekIfEmptyOrRemoved(itr):
                    self.table[itr] = value
                    return

    def remove(self, value):
        valueHash = self._hash(value)
        if self.exists(value):
            for itr in range(valueHash, self.LEN):
                if self.table[itr] == value and (not self.chcekIfEmptyOrRemoved(itr)):
                    self.table[itr] = self._REMOVED
                    return
            for itr in range(valueHash - 1):
                if self.table[itr] == value and (not self.chcekIfEmptyOrRemoved(itr)):
                    self.table[itr] = self._REMOVED
                    return

    def print(self):
        for val in self.table:
            print(val, end=', ')

    def chcekIfEmptyOrRemoved(self, itr):
        return self.table[itr] == self._EMPTY or self.table[itr] == self._REMOVED
