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
        # summ = 0
        # for gene in self.chromosome:
        #     summ += gene.weight
        # return summ


class Population:
    def __init__(self, size, nodes):
        self.size = size
        self.nodes = nodes
        self.solutions = self.create_random()

    def create_random(self):
        solutions = []
        new_list = []
        # This one just creates a sequence of n unique elements
        for _ in range(self.size):
            node_labels = random.sample(range(1, self.size), self.size-1)
            node_labels.insert(0,0)
            # These two are to sort things out, literally
            for i in range(self.size):
                for node in self.nodes:
                    if node.label == node_labels[i]:
                        new_list.append(node)
                        break
            solutions.append(Solution(nodes=new_list))
        return solutions


if __name__ == "__main__":
    g=Graph.Graph(nx.Graph(), 5)
    pop=Population(5, g.nodes)
    g.draw_graph(draw_edges=False)
    g.run()
