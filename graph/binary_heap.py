import numbers


class Heap:

    def __init__(self):
        self.table = []

    def add(self, element):
        if not (isinstance(element, tuple) and len(element) == 3):
            raise ValueError("You can append only tuple with length 3")
        if not isinstance(element[2], numbers.Number):
            raise ValueError("Element[2] must be number type")
        self.table.append(element)
        self._up(len(self.table) - 1)

    def _swap(self, child, parent):
        tmp = self.table[child]
        self.table[child] = self.table[parent]
        self.table[parent] = tmp

    def _upHeap(self, index):
        while index > 0:
            parentId = self.tab[index]
            if self.tab[parentId][2] <= self.tab[index][2]: break
            self._swap(parentId, index)
            index = parentId

    def _down(self, index):
        while True:
            if _right(index) < len(self.table):
                if self.table[_left(index)][2] < self.table[_right(index)][2]:
                    child = _left(index)
                else:
                    child = _right(index)
                if self.table[index][2] < self.table[child][2]:
                    break
                else:
                    self._swap(index, child)
                    index = child
            elif _left(index) < len(self.table):
                if self.table[index][2] < self.table[_left(index)][2]:
                    break
                else:
                    self._swap(index, _left(index))
                    index = _left(index)
            else:
                break

    def pop_top(self):
        result = self.table[0]
        self.table[0] = self.table[-1]
        del self.table[-1]
        self._down(0)
        return result


def _right(index):
    return index * 2 + 2


def _left(index):
    return index * 2 + 1


def _parent(index):
    return (index - 1) // 2
