from graph.Edge import Edge
from graph.Graph import Graph
from graph.GraphPrinter import GraphPrinter

graph = Graph(5)

edgesList = []
edgesList.append(Edge('A', 'B', 5))
edgesList.append(Edge('A', 'C', 5))
edgesList.append(Edge('A', 'D', 5))
edgesList.append(Edge('A', 'E', 5))
edgesList.append(Edge('B', 'C', 5))
edgesList.append(Edge('B', 'D', 5))
edgesList.append(Edge('B', 'E', 5))
edgesList.append(Edge('C', 'D', 5))
edgesList.append(Edge('C', 'E', 5))
edgesList.append(Edge('D', 'E', 5))

graph.addEdges(edgesList)

for itr in edgesList:
    itr.print()

graphPrinter = GraphPrinter(graph)
graphPrinter.print()
