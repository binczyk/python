from graph_new.Edge import Edge
from graph_new.Graph import Graph

graph = Graph(4)

edgesList = []
edgesList.append(Edge('A', 'C', 5))
edgesList.append(Edge('B', 'A', 7))
edgesList.append(Edge('C', 'B', 4))
edgesList.append(Edge('A', 'E', 8))
edgesList.append(Edge('E', 'C', 7))
graph.addEdges(edgesList)
graph.getMST()
