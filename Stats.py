import matplotlib.pyplot as plt

class Stats:
    def __init__(self, best_fitness, average_fitness, generations):
        self.best_fitness = best_fitness
        self.average_fitness = average_fitness
        self.generations = generations

    def plot_stats(self):
        plt.clf()
        plt.xlabel("Generations")
        plt.ylabel("Fitness")
        plt.plot(self.generations, self.best_fitness, 'ro', label="Best fitness", markersize=1.5)
        plt.plot(self.generations, self.average_fitness, 'bo', label = "Average fitness", markersize=1.5)
        plt.legend()
        figure = plt.gcf()
        figure.set_size_inches(13, 7)
        plt.savefig("stats.png", dpi=150)
