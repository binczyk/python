from tables.abstractTable import AbstractTable


class SortedTable(AbstractTable):
    def __init__(self):
        super().__init__()

    def add(self, value):
        if not self.exists(value):
            i = self._findIndex(value)
            if i == len(self.table) or self.table[i] != value:
                self.table.insert(i, value)

    def _findIndex(self, value):
        begin = 0
        end = len(self.table) - 1
        while begin <= end:
            middle = (end + begin) // 2
            if value == self.table[middle]:
                return middle
            elif self.table[middle] < value:
                begin = middle + 1
            else:
                end = middle - 1
        return begin

    def exists(self, value):
        i = self._findIndex(value)
        return i < len(self.table) and self.table[i] == value

    def remove(self, value):
        if self.exists(value):
            i = self._findIndex(value)
            del self.table[i]
