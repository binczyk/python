import sys

from graph.Heap import printArr, Heap


class Graph():

    def __init__(self, numberOfVertex):
        self.numberOfVertex = numberOfVertex
        self.graph = {}

    def _connect(self, vertex, node):
        if vertex in self.graph:
            self.graph[vertex].append(node)
        else:
            self.graph[vertex] = []
            self.graph[vertex].append(node)

    def addEdge(self, start, destination, weight):
        newNode = [destination, weight]
        self._connect(start, newNode)
        newNode = [start, weight]
        self._connect(destination, newNode)

    def PrimMST(self):
        minWeight = []
        finalMST = []
        minHeap = Heap()
        minHeap.size = self.numberOfVertex;

        for vertex in range(self.numberOfVertex):
            finalMST.append(-1)
            minWeight.append(sys.maxsize)
            minHeap.array.append(minHeap.newMinHeapNode(vertex, minWeight[vertex]))
            minHeap.position.append(vertex)

        # Make key value of 0th vertex as 0 so
        # that it is extracted first
        minHeap.position[0] = 0
        minWeight[0] = 0
        minHeap.decreaseKey(0, minWeight[0])

        # Initially size of min heap is equal to numberOfVertex

        # In the following loop, min heap contains all nodes
        # not yet added in the MST.
        while minHeap.isEmpty() == False:

            # Extract the vertex with minimum distance value
            newHeapNode = minHeap.extractMin()
            heapNode = newHeapNode[0]

            # Traverse through all adjacent vertices of u
            # (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph.get(heapNode):

                v = pCrawl[0]

                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less than
                # its previously calculated distance
                if minHeap.isInMinHeap(vertex) and pCrawl[1] < minWeight[vertex]:
                    minWeight[vertex] = pCrawl[1]
                    finalMST[vertex] = heapNode

                    # update distance value in min heap also
                    minHeap.decreaseKey(vertex, minWeight[vertex])

        printArr(finalMST, self.numberOfVertex)
