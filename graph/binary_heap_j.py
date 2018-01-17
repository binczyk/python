import numbers


class BinaryHeap:
    """
    Binary heap where the root is the smallest element.
    Element is the tuple where value of index 2 is compared.
    """

    def __init__(self):
        self.data = []

    def append(self, element):
        if not (isinstance(element, tuple) and len(element) == 3):
            raise ValueError("You can append only tuple with length 3")
        if not isinstance(element[2], numbers.Number):
            raise ValueError("Element[2] must be number type")
        self.data.append(element)
        self._up(len(self.data) - 1)

    def _swap(self, index1, index2):
        tmp = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = tmp

    def _up(self, index):
        while index > 0:
            parent_index = _parent(index)
            if self.data[parent_index][2] <= self.data[index][2]:
                break
            self._swap(parent_index, index)
            index = parent_index

    def _down(self, index):
        while True:
            if _right(index) < len(self.data):
                if self.data[_left(index)][2] < self.data[_right(index)][2]:
                    son_index = _left(index)
                else:
                    son_index = _right(index)
                if self.data[index][2] < self.data[son_index][2]:
                    break
                else:
                    self._swap(index, son_index)
                    index = son_index
            elif _left(index) < len(self.data):
                if self.data[index][2] < self.data[_left(index)][2]:
                    break
                else:
                    self._swap(index, _left(index))
                    index = _left(index)
            else:
                break

    def pop_top(self):
        result = self.data[0]
        self.data[0] = self.data[-1]
        del self.data[-1]
        self._down(0)
        return result


def _left(index):
    return index * 2 + 1


def _right(index):
    return index * 2 + 2


def _parent(index):
    return (index - 1) // 2
