class BinaryHeap:

    def __init__(self):
        self.heapTable = []

    def add(self, edge):
        self.heapTable.append(edge)
        self._upHeap(len(self.heapTable) - 1)

    def _swap(self, parent, child):
        self.heapTable[self.heapTable.index(child)] = parent
        self.heapTable[self.heapTable.index(parent)] = child

    def _upHeap(self, index):
        while index > 0:
            parent = self.heapTable[self._parent(index)]
            child = self.heapTable[index]
            if parent.waight <= child.waight: break
            self._swap(parent, child)
            index = self.heapTable.index(child)

    def _down(self, index):
        while True:
            parent = self.heapTable[index]
            if self._right(index) < len(self.heapTable):
                if self.heapTable[self._left(index)].waight <= self.heapTable[self._right(index)].waight:
                    child = self.heapTable[self._left(index)]
                else:
                    child = self.heapTable[self._right(index)]
                if parent.waight <= child.waight:
                    break
                else:
                    self._swap(parent, child)
                    index = self.heapTable.index(parent)

            elif self._left(index) <= len(self.heapTable):
                child = self.heapTable[self._left(index)]
                if parent.waight < child.waight:
                    break
                else:
                    self._swap(parent, child)
                    index = self.heapTable.index(parent)
            else:
                break

    def pop_top(self):
        result = self.heapTable[0]
        self.heapTable[0] = self.heapTable[-1]
        del self.heapTable[-1]
        self._down(0)
        return result

    def isEmpty(self):
        return len(self.heapTable) == 0

    def _right(self, index):
        return index * 2 + 2

    def _left(self, index):
        return index * 2 + 1

    def _parent(self, index):
        return (index - 1) // 2

    def print(self):
        for itr in self.heapTable:
            print(itr.waight, end='|')
