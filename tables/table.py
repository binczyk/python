class Table:
    def __init__(self):
        self.table = []

    def add(self, value):
        if not self.exists(value):
            self.table.append(value);

    def exists(self, value):
        for val in self.table:
            if val == value:
                return True
        return False

    def remove(self, value):
        for itr, val in enumerate(self.table):
            if value == val:
                self.table[itr] = self.table[-1]
                self.table.pop()
                return

    def print(self):
        for val in self.table:
            print(val, end=', ')
