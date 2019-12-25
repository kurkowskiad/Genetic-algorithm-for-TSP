import random
import math

class Node:
    def __init__(self, x, y, label=""):
        self.x = x
        self.y = y
        self.label = label


class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = round(weight,2)


class Graph:
    def __init__(self, graph, count, labels):
        self.graph = graph
        self.nodes = [Node(x=random.random(), y=random.random(), label=labels[i]) for i in range(count)]
        self.edges = self.create_edges()

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

    def initialize_all(self):
        # Add nodes.
        for node in self.nodes:
            self.graph.add_node(node.label, pos=(node.x, node.y))
        # Add edges.
        for edge in self.edges:
            self.graph.add_edge(edge.node1.label, edge.node2.label, weight=edge.weight)
