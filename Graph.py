import random
import math
import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, x, y, label=None):
        self.x = x
        self.y = y
        self.label = label


class Edge:
    def __init__(self, node1, node2):
        """
        node1, node2 are objects of class Node
        """
        self.node1 = node1
        self.node2 = node2
        self.weight = round(math.sqrt((self.node2.x-self.node1.x)**2
                                      +(self.node2.y-self.node1.y)**2),2)


class Graph:
    def __init__(self, graph, node_count):
        self.nodes = [Node(x=random.random(), y=random.random(), label=i) for i in range(node_count)]
        self.edges = self.create_edges()
        self.graph = graph

    def create_edges(self):
        edges = []
        for index1 in range(len(self.nodes)):
            index2 = 0
            while index2 < len(self.nodes):
                if index1 == index2 or index2 < index1:
                    pass
                else:
                    edges.append(Edge(self.nodes[index1], self.nodes[index2]))
                index2 += 1
        return edges

    def draw_graph(self, draw_edges=False):
        # Add nodes.
        for node in self.nodes:
            self.graph.add_node(node.label, pos=(node.x, node.y))
        pos = nx.get_node_attributes(self.graph, 'pos')

        if draw_edges:
            # Add edges.
            for edge in self.edges:
                self.graph.add_edge(edge.node1.label, edge.node2.label, weight=edge.weight)
            # Draw edge labels.
            edge_labels = nx.get_edge_attributes(self.graph, 'weight')
            nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=edge_labels)

    def run(self):
        # Draw graph.
        pos = nx.get_node_attributes(self.graph, 'pos')
        nx.draw(self.graph, pos=pos, with_labels=True, edge_color='#000000')
        plt.xlim(left=-0.02, right=1.02)
        plt.ylim(bottom=-0.02, top=1.02)
        plt.show()

if __name__ == "__main__":
    g = Graph(nx.Graph(), 5)
    g.draw_graph(draw_edges=True)
    g.run()
