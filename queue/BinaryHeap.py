from queue.Queue import Queue


class BinaryHeap(Queue):
    def __init__(self):
        self.tab = []

    def left(self, index):
        return index * 2 + 1

    def right(self, index):
        return index * 2 + 2

    def parent(self, index):
        return (index - 1) // 2

    def add(self, value):
        self.tab.append(value)
        self._upHeap(self.size() - 1)

    def top(self):
        return self.tab[0]

    def remove_top(self):
        pass

    def change(self, index, priority):
        if priority == self.tab[index]:
            return
        elif priority > self.tab[index]:
            self.tab[index] = priority
            self._upHeap(index)
        else:
            self.tab[index] = priority
            self._downHeap(index)

    def _upHeap(self, index):
        while index > 0:
            parentId = self.tab[index] > self.parent(index)
            if self.tab[parentId] >= self.tab[index]: break
            self._swap(index, parentId)
            index = parentId

    def _downHeap(self, index):
        while self.left(index) >= self.parent(index) and self.right(index) >= self.parent(index):
            if self.right(index) >= self.left(index):
                self._downHeap()

    def _swap(self, chidlId, parentId):
        tmp = self.tab[parentId]
        self.tab[parentId] = self.tab[chidlId]
        self.tab[chidlId] = tmp

    def size(self):
        return len(self.tab)
