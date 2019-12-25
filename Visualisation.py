import networkx as nx
import matplotlib.pyplot as plt
from Graph import Node, Edge, Graph

# Node names must be unique, otherwise the node won't be added to the graph.
labels = ["Istanbul", "Moscow", "London", "Petersburg", "Berlin", "Madrid", "Kyiv", "Rome", "Paris", "Bucharest",
         "Minsk", "Hamburg", "Vienna", "Warsaw", "Budapest", "Barcelona", "Kharkiv", "Munich", "Milan", "Prague"]
node_count = 8


class Visualisation:
    def __init__(self, graph, show_edges=False, show_edge_labels=False):
        self.graph = graph
        self.show_edges = show_edges
        self.show_edge_labels = show_edge_labels

    def run(self):
        self.graph.initialize_all()
        pos = nx.get_node_attributes(self.graph, 'pos')

        if self.show_edges:
            if self.show_edge_labels:
                edge_labels = nx.get_edge_attributes(self.graph, 'weight')
                nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=edge_labels)
            nx.draw(self.graph, pos=pos, with_labels=True)
        else:
            nx.draw(self.graph, pos=pos, with_labels=True)

        plt.xlim(left=-0.02, right=1.02)
        plt.ylim(bottom=-0.02, top=1.02)
        plt.show()

if __name__ == "__main__":
    g = Graph(nx.Graph(), node_count, labels=labels)
    vis = Visualisation(g)
    vis.run()