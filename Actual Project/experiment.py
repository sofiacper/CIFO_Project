'''
This file is dedicated to the development of the evaluation and comparison strategy
    1) Run experiment: run_experiment
        """
        Runs an experiment using a genetic algorithm over multiple runs and returns the median best fitness per generation.

        Parameters:
        -----------
        args : tuple
            A tuple containing the following elements in order:
            - population_size (int): The size of the population.
            - generations (int): The number of generations for the algorithm to run.
            - crossover_probability (float): The probability of crossover occurring.
            - mutation_probability (float): The probability of mutation occurring.
            - selection (function): The selection function to use.
            - mutation (function): The mutation function to use.
            - crossover (function): The crossover function to use.
            - elitism (bool): Whether to use elitism or not.
            - sol_size (int): The size of the solutions in the population.
            - valid_set (list): The set of valid values that solutions can have.

        Returns:
        --------
        median_best_fitness_per_gen : list of float
            A list containing the median best fitness for each generation across all runs.

        Description:
        ------------
        This function performs a genetic algorithm experiment over multiple runs (10 by default) and tracks the best fitness
        value for each generation. It creates a population, evolves it over the specified number of generations, and records
        the best fitness value of each generation for all runs. The function returns the median of these best fitness values
        for each generation across all runs.

        Procedure:
        ----------
        1. Initialize an empty list `all_fitness` to store the best fitness values for each generation for all runs.
        2. Loop over the number of runs (10 by default).
           - Start timing the run.
           - Create an initial population with the specified parameters.
           - Initialize an empty list `generation_fitness` to track the best fitness for each generation in the current run.
           - Loop over the specified number of generations.
             - Evolve the population for one generation.
             - Find and record the best fitness value of the current generation.
           - Append the recorded best fitness values of the current run to `all_fitness`.
           - Print the best fitness value and time taken for the current run.
        3. Transpose `all_fitness` to group the best fitness values by generation.
        4. Compute the median best fitness for each generation across all runs.
        5. Return the list of median best fitness values per generation.

        Example:
        --------
        args = (100, 50, 0.8, 0.1, selection_function, mutation_function, crossover_function, True, 10, valid_values)
        median_fitness = run_experiment(args)
        """

    2) Create labels: create_labels
        """
        Generates labels for a list of experiments based on specific elements.

        Args:
        experiments (list): A list of tuples representing experiments.

        Returns:
        list: A list of labels generated based on elements of each experiment tuple.
        """

    3) Plot: plot_average_best_fitness
        """
        Plots the median best fitness per generation for multiple experiments.

        Args:
        all_median_fitnesses (list): A list of lists containing median best fitness values for each generation.
        labels (list): A list of labels corresponding to each set of median fitness values.
        """
'''

# ----------Imports-----------------
import multiprocessing as mp
import time
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

#Classes
from charles.charles import Population, Individual

# Problem definition
from song import get_fitness

#Selection
from charles.selection import fps, tournament_sel, rank_sel

#Geometric Operators
from charles.geooperators import geometric_mutation, geometric_xo

#Other operators: mutations and crossovers
from charles.xo import single_point_xo, two_point_xo, uniform_xo, blend_xo, blx_alpha_xo, order_one_xo, arithmetic_xo
from charles.mutation import swap_mutation, random_reseting, inversion_mutation, scramble_mutation, centre_inverse_mutation

# Other initializations
from initializations import melody_rules, major_scale, sobol_sequence

# Individual Monkey Patching
Individual.get_fitness = get_fitness

# ----------Experiment Function------
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

    # Transpose all_fitness to have each generation's best fitness in the same list
    all_fitness = list(map(list, zip(*all_fitness)))

    # Compute the median best fitness for each generation across all runs
    median_best_fitness_per_gen = [np.median(gen_fitness) for gen_fitness in all_fitness]

    return median_best_fitness_per_gen


#---------- Tests ----------------
"""Ex: We want to test 2 algorithms that only differ in the existence of elitism, having: 
    Population size= 1000, 
    Generations= 500, 
    cross-over rate= 0.9, 
    mutation rate = 0.5, 
    selection algorithm = tournament, 
    mutation operators= swap mutation , 
    cross-over operators= uniform cross-over
    
"""
experiments = [
    [1000, 500, 0.9, 0.5, tournament_sel, swap_mutation, uniform_xo, True],
    [1000, 500, 0.9, 0.5, tournament_sel, swap_mutation, uniform_xo, False]
]

# Add sol_size and valid_set to each experiment
for exp in experiments:
    exp.extend([312, [i for i in range(127)]])

#---------- Parallelization ----------------
if __name__ == '__main__':
    with mp.Pool(mp.cpu_count()) as pool:
        all_median_fitnesses = pool.map(run_experiment, experiments)

    def create_labels(experiments):
        labels = []
        for exp in experiments:
            label_parts = []
            #label_parts.append(f"{exp[0]}")  # Pop
            #label_parts.append(f"{exp[2]}")  # xo_rate
            #label_parts.append(f"{exp[3]}")  # mutation_rate
            # label_parts.append(f"{exp[4].__name__}")  # Selection
            #label_parts.append(f"{exp[4].__name__}")  # Selection
            #label_parts.append(f"{exp[6].__name__}")  # crossover
            #label_parts.append(f"{exp[5].__name__}") #mutation
            label_parts.append(f"{exp[7]}") #elitism
            labels.append(", ".join(label_parts))

        return labels

    labels = create_labels(experiments)

    def plot_average_best_fitness(all_median_fitnesses, labels):
        for i, median_best_fitness in enumerate(all_median_fitnesses):
            plt.plot(range(1, len(median_best_fitness) + 1), median_best_fitness, marker='', linestyle='-',
                     label=labels[i])

        plt.title('Median Best Fitness per Generation')
        plt.xlabel('Generation')
        plt.ylabel('Median Best Fitness')
        plt.legend()
        plt.grid(True)

        # Automatically adjust y-axis scale with specific intervals
        plt.gca().yaxis.set_major_locator(MultipleLocator(25))

        plt.show()

    plot_average_best_fitness(all_median_fitnesses, labels)
