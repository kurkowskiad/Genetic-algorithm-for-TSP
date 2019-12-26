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
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = round(weight,2)


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
                    edges.append(Edge(self.nodes[index1], self.nodes[index2],
                                           weight=math.sqrt((self.nodes[index2].x-self.nodes[index1].x)**2
                                                            +(self.nodes[index2].y-self.nodes[index1].y)**2)))
                index2 += 1
        return edges

    def create_vis(self, edges=False):
        # Add nodes.
        for node in self.nodes:
            self.graph.add_node(node.label, pos=(node.x, node.y))
        pos = nx.get_node_attributes(self.graph, 'pos')

        if edges:
            # Add edges.
            for edge in self.edges:
                self.graph.add_edge(edge.node1.label, edge.node2.label, weight=edge.weight)
            edge_labels = nx.get_edge_attributes(self.graph, 'weight')
            # Draw edges with labels.
            nx.draw_networkx_edge_labels(self.graph, pos=pos, edge_labels=edge_labels)

        # Draw nodes.
        nx.draw(self.graph, pos=pos, with_labels=True)

        plt.xlim(left=-0.02, right=1.02)
        plt.ylim(bottom=-0.02, top=1.02)
        plt.show()

if __name__ == "__main__":
    g = Graph(nx.Graph(), 5)
    g.create_vis(True)
