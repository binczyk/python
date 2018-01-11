from graph.Graph import Graph

graph = Graph(5)
graph.addEdge(0, 1, 1)
graph.addEdge(0, 2, 2)
graph.addEdge(1, 4, 3)
graph.addEdge(1, 3, 0)
graph.addEdge(2, 3, 4)
graph.addEdge(3, 4, 4)
graph.PrimMST()
