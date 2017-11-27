from tables.abstractTable import AbstractTable


class HashTable(AbstractTable):
    def __init__(self, LEN=16):
        self.LEN = LEN
        self.table = [[] for _ in range(LEN)]

    def _hash(self, value):
        return abs(hash(value)) % self.LEN

    def add(self, value):
        if not self.exists(value):
            self.table[self._hash(value)].append(value)

    def exists(self, value):
        for val in self.table[self._hash(value)]:
            if val == value:
                return True
        return False

    def remove(self, value):
        if self.exists(value):
            self.table[self._hash(value)].remove(value)
