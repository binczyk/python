import graphviz

from graph.Graph import Graph

dot = graphviz.Digraph()

dot.node('0', '0')
dot.node('1', '1')
dot.node('2', '2')
dot.node('3', '3')
dot.node('4', '4')

dot.edge('0', '1')
dot.edge('0', '2')
dot.edge('1', '4')
dot.edge('1', '3')
dot.edge('2', '3')
dot.edge('3', '4')

dot.render()

graph = Graph(5)
graph.addEdge(0, 1, 1)
graph.addEdge(0, 2, 2)
graph.addEdge(1, 4, 3)
graph.addEdge(1, 3, 0)
graph.addEdge(2, 3, 4)
graph.addEdge(3, 4, 4)
graph.PrimMST()
