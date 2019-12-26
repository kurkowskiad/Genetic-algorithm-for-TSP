import networkx as nx
import Graph
import random

class Solution:
    def __init__(self, nodes):
        # self.chromosome is a list of edges
        self.nodes = nodes
        self.chromosome = self.create_chromosome()
        self.fitness = self.calculate_fitness()

    def create_chromosome(self):
        chromosome = []
        for index in range(len(self.nodes)):
            if index == len(self.nodes)-1:
                chromosome.append(Graph.Edge(self.nodes[index], self.nodes[0]))
            else:
                chromosome.append(Graph.Edge(self.nodes[index], self.nodes[index+1]))
        return chromosome

    def calculate_fitness(self):
        return sum([gene.weight for gene in self.chromosome])


class Population:
    def __init__(self, size, graph):
        self.size = size
        self.graph = graph
        self.solutions = self.create_random()

    def create_random(self):
        solutions = []
        new_list = []
        # This one just creates a sequence of n unique elements - solutions
        for _ in range(self.size):
            node_labels = random.sample(range(1, len(self.graph.nodes)), len(self.graph.nodes)-1)
            node_labels.insert(0,0)
            # These two are to sort things out, literally
            for i in range(len(self.graph.nodes)):
                for node in self.graph.nodes:
                    if node.label == node_labels[i]:
                        new_list.append(node)
                        break
            solutions.append(Solution(nodes=new_list))
        return solutions

    def draw_solution(self):
        for edge in self.solutions[0].chromosome:
            self.graph.graph.add_edge(edge.node1.label, edge.node2.label, weight=edge.weight)
            print(edge.node1.label, edge.node2.label)

if __name__ == "__main__":
    g=Graph.Graph(graph=nx.Graph(), node_count=20)
    pop=Population(size=10, graph=g)
    g.draw_graph(draw_edges=False)
    pop.draw_solution()
    g.run()
