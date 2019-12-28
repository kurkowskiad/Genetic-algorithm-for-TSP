import networkx as nx
import Graph
import random
import matplotlib.pyplot as plt
import time

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

    def match_node_labels_to_nodes(self, labels):
        nodes = []
        for i in range(len(self.graph.nodes)):
            for node in self.graph.nodes:
                if node.label == labels[i]:
                    nodes.append(node)
                    break
        return nodes

    def create_random(self):
        """Creates random solutions to TSP,
         as a list of Solution objects containing chromosome (list of edges) and nodes"""
        solutions = []
        # This one just creates a sequence of n unique elements - solutions
        for _ in range(self.size):
            node_labels = random.sample(range(1, len(self.graph.nodes)), len(self.graph.nodes)-1)
            node_labels.insert(0,0)
            nodes = self.match_node_labels_to_nodes(node_labels)
            solutions.append(Solution(nodes=nodes))
        return solutions

    def draw_solution(self, index):
        for edge in self.solutions[index].chromosome:
            self.graph.graph.add_edge(edge.node1.label, edge.node2.label)

    def remove_all_edges(self):
        self.graph.graph.remove_edges_from(self.graph.graph.edges())

    def crossover(self, parent1, parent2):
        """See Standard Decomposition on http://www.permutationcity.co.uk/projects/mutants/tsp.html"""
        if parent1 == parent2:
            raise Exception("Parent1 and parent2 are the same objects.")
        if len(parent1.chromosome) != len(parent2.chromosome):
            raise Exception("Parents are of different chromosome length. The code is buggy")

        # Offspring initially a copy of parent1
        offspring = [node.label for node in parent1.nodes]
        index_list = []

        # Note indices of randomly chosen characters in offspring
        for index, label in enumerate(offspring):
            if random.random() >= 0.5:
                index_list.append(index)

        # Values(node labels) on corresponding positions in index_list
        values = [offspring[index] for index in index_list]

        # Changing indices of index_list in offspring to fit parent2 order
        for index in index_list:
            for label in [node.label for node in parent2.nodes]:
                if label in values:
                    offspring[index] = label
                    values.remove(label)
                    break

        nodes = self.match_node_labels_to_nodes(offspring)
        return Solution(nodes=nodes)

    def mutate(self, parent, mutation_chance, swap_with_neighbour=True):
        offspring = [node.label for node in parent.nodes]

        if swap_with_neighbour:
            for index, _ in enumerate(offspring):
                if index == 0:
                    pass
                elif random.random() <= mutation_chance:
                    try:
                        offspring[index], offspring[index + 1] = offspring[index + 1], offspring[index]
                    except IndexError:
                        offspring[index], offspring[index - 1] = offspring[index - 1], offspring[index]
        else:
            for index, _ in enumerate(offspring):
                if index == 0:
                    pass
                elif random.random() <= mutation_chance:
                    random_index = random.randint(1, len(offspring) - 1)
                    offspring[index], offspring[random_index] = offspring[random_index], offspring[index]

        nodes = self.match_node_labels_to_nodes(offspring)
        return Solution(nodes=nodes)

    def kill_population(self, percent_of_solutions_to_remove):
        # Sort solutions by their fitness value - list starts with worst solutions and ends with best
        self.solutions = sorted(self.solutions, key=lambda x: x.fitness, reverse=True)
        while len(self.solutions) > self.size * percent_of_solutions_to_remove:
            self.solutions.pop(0)

    def repopulate(self):
        while len(self.solutions) < self.size:
            parent1=random.choice(self.solutions)
            parent2=random.choice(self.solutions)
            while parent1 == parent2:
                if len(self.solutions) == 1:
                    raise Exception("Population is too small. Make starting population bigger.")
                parent2=random.choice(self.solutions)
            self.solutions.append(self.mutate(self.crossover(parent1, parent2), .05))


class GA:
    def __init__(self, graph, population):
        self.graph = graph
        self.population = population

    def run(self):
        best_fitness = []
        average_fitness = []
        for i in range(1000):
            self.graph.add_nodes_edges()
            best_fitness.append(pop.solutions[0].fitness)
            average_fitness.append(sum([sol.fitness for sol in pop.solutions])/pop.size)
            if i%5==0:
                print("GENERATION " + str(i) + ", best fitness: " + str(best_fitness[i]), end=", ")
                print("average fitness: " + str(average_fitness[i]))
            self.population.kill_population(.5)
            pop.repopulate()
            pop.draw_solution(0)
            self.graph.update_graph()
            # If difference between average fitness of 100 iterations and current fitness smaller than .01
            if len(best_fitness) > 100 and sum(best_fitness[-100:])/100 - best_fitness[i] < .01:
                print("FINISHED IN GENERATION " + str(i))
                plt.pause(20)
            plt.pause(.001)
            pop.remove_all_edges()
            plt.clf()

if __name__ == "__main__":
    g=Graph.Graph(graph=nx.Graph(), node_count=30)
    pop=Population(size=50, graph=g)
    algorithm = GA(graph=g, population=pop)
    algorithm.run()
