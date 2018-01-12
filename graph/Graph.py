import sys
from collections import defaultdict

from graph.Heap import printArr, Heap


class Graph():

    def __init__(self, numberOfVertex):
        self.numberOfVertex = numberOfVertex
        self.graph = defaultdict(list)

    # Adds an edge to an undirected graph
    def addEdge(self, start, destination, weight):
        # Add an edge from src to dest.  A new node is
        # added to the adjacency list of src. The node
        # is added at the begining. The first element of
        # the node has the destination and the second
        # elements has the weight
        newNode = [destination, weight]
        self.graph[start].insert(0, newNode)

        # Since graph is undirected, add an edge from
        # dest to src also
        newNode = [start, weight]
        self.graph[destination].insert(0, newNode)

    # The main function that prints the Minimum
    # Spanning Tree(MST) using the Prim's Algorithm.
    # It is a O(ELogV) function
    def PrimMST(self):
        # Get the number of vertices in graph
        numberOfVertex = self.numberOfVertex

        # key values used to pick minimum weight edge in cut
        key = []

        # List to store contructed MST
        parent = []

        # minHeap represents set E
        minHeap = Heap()

        #  Initialize min heap with all vertices. Key values of all
        # vertices (except the 0th vertex) is is initially infinite
        for vertex in range(numberOfVertex):
            parent.append(-1)
            key.append(sys.maxsize)
            minHeap.array.append(minHeap.newMinHeapNode(vertex, key[vertex]))
            minHeap.pos.append(vertex)

        # Make key value of 0th vertex as 0 so
        # that it is extracted first
        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0])

        # Initially size of min heap is equal to numberOfVertex
        minHeap.size = numberOfVertex;

        # In the following loop, min heap contains all nodes
        # not yet added in the MST.
        while minHeap.isEmpty() == False:

            # Extract the vertex with minimum distance value
            newHeapNode = minHeap.extractMin()
            heapNode = newHeapNode[0]

            # Traverse through all adjacent vertices of u
            # (the extracted vertex) and update their
            # distance values
            for pCrawl in self.graph[heapNode]:

                v = pCrawl[0]

                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less than
                # its previously calculated distance
                if minHeap.isInMinHeap(vertex) and pCrawl[1] < key[vertex]:
                    key[vertex] = pCrawl[1]
                    parent[vertex] = heapNode

                    # update distance value in min heap also
                    minHeap.decreaseKey(vertex, key[vertex])

        printArr(parent, numberOfVertex)
