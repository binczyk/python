import graphviz

from graph.Edge import Edge


class GraphPrinter:
    _existNodes = []
    _mstList = []

    def __init__(self, graph):
        self.graph = graph

    def _getReversEdge(self, edge):
        return Edge(edge.toVertex, edge.fromVertex, edge.waight)

    def _getMstList(self, graph):
        mstList = []
        for itr, edge in enumerate(graph.getMST()):
            mstList.append((edge.toVertex, edge.fromVertex))
            mstList.append((edge.fromVertex, edge.toVertex))
        return mstList

    def _addAndColorIfInMst(self, graphPrinter, edge):
        edgeVertex = (edge.fromVertex, edge.toVertex)
        edgeVertexRevers = (edge.toVertex, edge.fromVertex)

        if edgeVertex not in self._existNodes and edgeVertexRevers not in self._existNodes:
            if edgeVertex in self._mstList:
                graphPrinter.edge(edge.fromVertex, edge.toVertex, label=str(edge.waight), color='Green', dir='none')
            else:
                graphPrinter.edge(edge.fromVertex, edge.toVertex, label=str(edge.waight), dir='none')

        self._existNodes.append(edgeVertex)
        self._existNodes.append(edgeVertexRevers)

    def _addUniqueEdges(self, graphPrinter):
        self._mstList = self._getMstList(self.graph)
        for index, node in enumerate(self.graph.adjacencyList):
            for edge in self.graph.getEdges(node):
                self._addAndColorIfInMst(graphPrinter, edge)

    def _addVertex(self, graphPrinter):
        for index, node in enumerate(self.graph.adjacencyList):
            graphPrinter.node(node)

    def print(self):
        graphPrinter = graphviz.Digraph(format='svg')
        self._addUniqueEdges(graphPrinter)

        graphPrinter.attr(label=r'\n\nAlgorytm Prima\nMinimalne drzewo rozpinające')
        graphPrinter.attr(fontsize='15')
        graphPrinter.view('image/graph')
