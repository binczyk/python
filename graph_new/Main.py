from graph_new.Edge import Edge
from graph_new.Graph import Graph

graph = Graph(8)

edgesList = []
edgesList.append(Edge('0', '1', 5))
edgesList.append(Edge('0', '6', 3))
edgesList.append(Edge('0', '3', 9))
edgesList.append(Edge('1', '5', 6))
edgesList.append(Edge('1', '4', 8))
edgesList.append(Edge('1', '7', 7))
edgesList.append(Edge('1', '2', 9))
edgesList.append(Edge('2', '3', 9))
edgesList.append(Edge('2', '4', 4))
edgesList.append(Edge('2', '6', 5))
edgesList.append(Edge('2', '7', 3))
edgesList.append(Edge('3', '6', 8))
edgesList.append(Edge('4', '5', 2))
edgesList.append(Edge('4', '6', 1))
edgesList.append(Edge('5', '6', 6))
edgesList.append(Edge('6', '7', 9))

graph.addEdges(edgesList)

for itr in edgesList:
    itr.print()

graph.getMST()
