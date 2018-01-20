from graph.Edge import Edge
from graph.Graph import Graph
from graph.GraphPrinter import GraphPrinter

graph = Graph(8)

edgesList = []
edgesList.append(Edge('A', 'B', 5))
edgesList.append(Edge('A', 'F', 3))
edgesList.append(Edge('A', 'C', 9))
edgesList.append(Edge('B', 'E', 6))
edgesList.append(Edge('B', 'D', 8))
edgesList.append(Edge('B', 'G', 7))
edgesList.append(Edge('B', 'H', 9))
edgesList.append(Edge('H', 'C', 9))
edgesList.append(Edge('H', 'D', 4))
edgesList.append(Edge('H', 'F', 5))
edgesList.append(Edge('H', 'G', 3))
edgesList.append(Edge('C', 'F', 8))
edgesList.append(Edge('D', 'E', 2))
edgesList.append(Edge('D', 'F', 1))
edgesList.append(Edge('E', 'F', 6))
edgesList.append(Edge('F', 'G', 9))

graph.addEdges(edgesList)

for itr in edgesList:
    itr.print()

graphPrinter = GraphPrinter(graph)
graphPrinter.print()
