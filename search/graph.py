import plotly.graph_objs as go
import plotly.plotly as py


class Graph:
    def __init__(self, numberOfCompersion):
        self.x = [1000, 10000, 100000, 1000000]
        self.y = numberOfCompersion

    def draw(self):
        trace = go.Scatter(x=self.x, y=self.y, mode='markers', name='markers')
        data = [trace]
        py.iplot(data, filename='line-mode')
