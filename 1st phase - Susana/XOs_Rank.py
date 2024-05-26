import multiprocessing as mp
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from charles.charles import Population, Individual
from song import get_fitness
from charles.selection import rank_sel
from charles.mutation import swap_mutation
from charles.xo import single_point_xo, two_point_xo, uniform_xo, arithmetic_xo, blend_xo, blx_alpha_xo, order_one_xo


# Individual Monkey Patching
Individual.get_fitness = get_fitness


# Function to run a single experiment
def run_experiment(args):
    population_size, generations, crossover_probability, mutation_probability, selection, mutation, crossover, elitism, sol_size, valid_set = args
    all_fitness = []

    for i in range(10):  # Number of runs
        start_time = time.time()

        # Create a population
        pop = Population(size=population_size, optim="min", sol_size=sol_size, valid_set=valid_set, repetition=True)

        # Track fitness for each generation
        generation_fitness = []
        for gen in range(generations):
            pop.evolve(gens=1, xo_prob=crossover_probability, mut_prob=mutation_probability,            
                       select=selection, mutate=mutation, xo=crossover, elitism=elitism)
            best_fitness = min(ind.fitness for ind in pop.individuals)
            generation_fitness.append(best_fitness)

        all_fitness.append(generation_fitness)
        end_time = time.time()
        print(f"Run #{i + 1}, Generation #{gen + 1}: Best Fitness: {best_fitness}, Time: {round(end_time - start_time, 2)} seconds")


    # Transpose all_fitness to have each generation's best fitnesses in the same list
    all_fitness = list(map(list, zip(*all_fitness)))


    # Compute the median best fitness for each generation across all runs
    median_best_fitness_per_gen = [np.median(gen_fitness) for gen_fitness in all_fitness]

    return median_best_fitness_per_gen


# Crossovers
experiments = [
    [500, 300, 0.9, 0.2, rank_sel, swap_mutation, single_point_xo, True],
    [500, 300, 0.9, 0.2, rank_sel, swap_mutation, two_point_xo, True],
    [500, 300, 0.9, 0.2, rank_sel, swap_mutation, uniform_xo, True],
    [500, 300, 0.9, 0.2, rank_sel, swap_mutation, arithmetic_xo, True],
    [500, 300, 0.9, 0.2, rank_sel, swap_mutation, blend_xo, True],
    [500, 300, 0.9, 0.2, rank_sel, swap_mutation, blx_alpha_xo, True],
    [500, 300, 0.9, 0.2, rank_sel, swap_mutation, order_one_xo, True]]


# Add sol_size and valid_set to each experiment
for exp in experiments:
    exp.extend([312, [i for i in range(127)]])

# Run experiments in parallel
if __name__ == '__main__':
    with mp.Pool(mp.cpu_count()) as pool:
        all_median_fitnesses = pool.map(run_experiment, experiments)

    def create_labels(experiments):
        labels = []
        for exp in experiments:
            label_parts = []
            label_parts.append(f"{exp[6].__name__}") # Crossover
            labels.append(", ".join(label_parts))
        return labels

    labels = create_labels(experiments)

    def plot_average_best_fitness(all_median_fitnesses, labels):
        for i, median_best_fitness in enumerate(all_median_fitnesses):
            plt.plot(range(1, len(median_best_fitness) + 1), median_best_fitness, linestyle='-', label=labels[i])


        plt.title('Median Best Fitness per Generation')
        plt.xlabel('Generation')
        plt.ylabel('Median Best Fitness')
        plt.legend()
        plt.grid(True)
        plt.show()

    plot_average_best_fitness(all_median_fitnesses, labels)
