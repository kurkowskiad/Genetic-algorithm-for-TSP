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
        """Creates random solutions to TSP,
         as a list of Solution objects containing chromosome (list of edges) and nodes"""
        solutions = []
        # This one just creates a sequence of n unique elements - solutions
        for _ in range(self.size):
            nodes = []
            node_labels = random.sample(range(1, len(self.graph.nodes)), len(self.graph.nodes)-1)
            node_labels.insert(0,0)
            # These two are to sort things out, literally
            for i in range(len(self.graph.nodes)):
                for node in self.graph.nodes:
                    if node.label == node_labels[i]:
                        nodes.append(node)
                        break
            solutions.append(Solution(nodes=nodes))
        return solutions

    def draw_solution(self, index):
        for edge in self.solutions[index].chromosome:
            self.graph.graph.add_edge(edge.node1.label, edge.node2.label, weight=edge.weight)

    def crossover(self):
        """See Standard Decomposition on http://www.permutationcity.co.uk/projects/mutants/tsp.html"""
        # Randomly choosing parents
        parent1 = random.choice(self.solutions)
        parent2 = random.choice(self.solutions)
        while parent1 == parent2:
            if len(self.solutions) == 1:
                raise Exception("Needs bigger population than 1 for crossover reasons")
            parent2 = random.choice(self.solutions)
        if len(parent1.chromosome) != len(parent2.chromosome):
            raise Exception("Parents are of different chromosome length. The code is buggy")

        # Offspring initially a copy of parent1
        offspring = [node.label for node in parent1.nodes]
        # print("Parent1: " + str([node.label for node in parent1.nodes]))
        # print("Parent2: " + str([node.label for node in parent2.nodes]))
        index_list = []
        # Note indices of randomly chosen characters in offspring
        for index, label in enumerate(offspring):
            if random.random() >= 0.5:
                index_list.append(index)
        # Values(node labels) on corresponding positions in index_list
        values = [offspring[index] for index in index_list]
        # print("Index list: "+ str(index_list))
        # print("Values: " + str(values))
        # print()
        # It's complicated ok?
        for index in index_list:
            for label in [node.label for node in parent2.nodes]:
                if label in values:
                    # print(str(label) + " is in " + str(values))
                    # print("Replacing " + str(offspring[index]) + " with " + str(label))
                    offspring[index] = label
                    values.remove(label)
                    break

        print("Offspring: " + str(offspring))

if __name__ == "__main__":
    g=Graph.Graph(graph=nx.Graph(), node_count=7)
    pop=Population(size=3, graph=g)
    g.draw_graph(draw_edges=True)
    pop.crossover()
    #g.run()
