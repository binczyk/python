import graphviz


class GraphPrinter:

    def __init__(self, graph):
        self.graph = graph

    def print(self):
        g2 = graphviz.Digraph(format='svg')
        g2.node('A')
        g2.node('B')
        g2.edge('A', 'B')
        g2.render('img/g2')
