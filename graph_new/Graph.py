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
        keyList = []
        visited = {}
        MST = []
        for index, node in enumerate(self.adjacencyList):
            visited[node] = False
            keyList.append(node)

        currentVertex = 0
        visited[keyList[currentVertex]] = True

        for itr in range(self.numberOfVertex - 1):
            for neighbor in (self.getEdges(keyList[currentVertex])):
                if not visited.get(neighbor.toVertex):
                    heap.add(neighbor)
            while not heap.isEmpty():
                cheapestVertex = heap.pop_top()
                if not visited.get(cheapestVertex.toVertex):
                    MST.append(cheapestVertex)
                    visited[cheapestVertex.toVertex] = True
                    currentVertex = keyList.index(cheapestVertex.toVertex)
                    break

        print('MST:')
        sum = 0
        for itr in MST:
            sum += itr.waight
            print(itr.fromVertex, '->', itr.toVertex, '||', itr.waight)
        print('sum =', sum)
