from graph_new.BinaryHeap import BinaryHeap
from graph_new.Edge import Edge


class Graph:

    def __init__(self, numberOfVertex):
        self.numberOfVertex = numberOfVertex
        self.adjacencyList = {}

    def _add(self, edgeName, edge):
        if edgeName in self.adjacencyList:
            self.adjacencyList[edgeName].append(edge)
        else:
            self.adjacencyList[edgeName] = []
            self.adjacencyList[edgeName].append(edge)

    def addEdges(self, edgesList):
        for edge in edgesList:
            self._add(edge.fromVertex, edge)
            self._add(edge.toVertex, Edge(edge.toVertex, edge.fromVertex, edge.waight))

    def getEdges(self, vertexFrom):
        return self.adjacencyList.get(vertexFrom)

    def getMST(self):
        heap = BinaryHeap()

        for itr, node in enumerate(self.adjacencyList):
            for vertex in self.adjacencyList.get(node):
                heap.add(vertex)

        heap.print()
        print()
        heap.pop_top()
        heap.print()
        print()
        heap.pop_top()
        heap.print()
        print()
        heap.pop_top()
        heap.print()
        # while not heap.isEmpty():
        #     cheapestVertex = heap.pop_top()
