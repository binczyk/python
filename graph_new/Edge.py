class Edge:

    def __init__(self, fromVertex, toVertex, waight):
        self.fromVertex = fromVertex
        self.toVertex = toVertex
        self.waight = waight

    def print(self):
        print(self.fromVertex, '-', self.waight, '>', self.toVertex)
