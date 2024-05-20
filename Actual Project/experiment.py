import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from charles.charles import Population, Individual
from song import get_fitness
from charles.selection import fps, tournament_sel
from charles.mutation import swap_mutation
from charles.xo import single_point_xo

# Individual Monkey Patching
Individual.get_fitness = get_fitness

#fitness_experiments = []

# Improved Experiment Labeling
def create_labels(experiments):
    labels = []
    for exp in experiments:
        label_parts = []
        #label_parts.append(f"{exp[5].__name__}") #mutation
        label_parts.append(f"{exp[6].__name__}") #crossover
        labels.append(", ".join(label_parts))
    return labels

def run_experiment(population_size, generations, crossover_probability, mutation_probability, selection, mutation,
                   crossover, elitism, sol_size=312, valid_set=[i for i in range(127)]):
    all_fitness = []
    best_fitnesses = []

    for i in range(10):
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
        best_fitnesses.append(min(generation_fitness))

        end_time = time.time()
        iteration_time = end_time - start_time
        print(f"Iteration {i + 1} time: {round(iteration_time, 2)} seconds")

    return all_fitness, best_fitnesses

def plot_average_best_fitness(all_fitness):
    # Calculate the average best fitness per generation
    avg_best_fitness = np.mean(all_fitness, axis=0)

    # Plot the average best fitness per generation
    plt.plot(range(1, len(avg_best_fitness) + 1), avg_best_fitness, marker='o', linestyle='-')
    plt.title('Average Best Fitness per Generation')
    plt.xlabel('Generation')
    plt.ylabel('Average Best Fitness')
    plt.grid(True)
    plt.show()

# Run the experiments and store results
all_fitness, best_fitnesses = run_experiment(population_size=10, generations=10, crossover_probability=0.9,
                                             mutation_probability=0.2, selection=tournament_sel, mutation=swap_mutation,
                                             crossover=single_point_xo, elitism=True)

# Plot the average best fitness per generation
plot_average_best_fitness(all_fitness)

#experiments configurations
experiments = [
    [10, 10, 0.9, 0.2, tournament_sel, swap_mutation, single_point_xo, True, True, True],
    [10, 10, 0.9, 0.2, fps, swap_mutation, single_point_xo, True, True, False]
]

#create labels for experiments
labels = create_labels(experiments)

# Print the labels for verification
for i, label in enumerate(labels):
    print(f"Experiment {i + 1}: {label}")

#run the experiments and store results
experiment_results = []
for exp in experiments:
    print(f"Running experiment: {experiments.index(exp) + 1}")
    avg_fitness, std_fitness = run_experiment(population_size=exp[0],
                                              generations=exp[1],
                                              crossover_probability=exp[2],
                                              mutation_probability=exp[3],
                                              selection=exp[4],
                                              mutation=exp[5],
                                              crossover=exp[6],
                                              elitism=exp[7],
                                              sol_size=312,
                                              valid_set=[i for i in range(127)])

    experiment_results.append([avg_fitness, std_fitness])
    print(f"Experiment {experiments.index(exp) + 1} finished")
    print("--------------------------------------------------")

# Create a DataFrame to store the results
df_results = pd.DataFrame(experiment_results, columns=["Average Fitness", "Standard Deviation"])
df_results["Experiment"] = labels

print(df_results)

def plot_average_best_fitness(all_fitnesses, labels):
    # Plot the average best fitness per generation for each experiment
    for i, fitness in enumerate(all_fitnesses):
        avg_best_fitness = np.mean(fitness, axis=0)
        plt.plot(range(1, len(avg_best_fitness) + 1), avg_best_fitness, marker='o', linestyle='-', label=labels[i])

    plt.title('Average Best Fitness per Generation')
    plt.xlabel('Generation')
    plt.ylabel('Average Best Fitness')
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the experiments and store results
all_fitnesses = []
labels = []

for exp in experiments:
    avg_best_fitness, _ = run_experiment(population_size=exp[0], generations=exp[1], crossover_probability=exp[2],
                                         mutation_probability=exp[3], selection=exp[4], mutation=exp[5],
                                         crossover=exp[6], elitism=exp[7])
    all_fitnesses.append(avg_best_fitness)
    labels.append(create_labels([exp])[0])

# Plot the average best fitness per generation for each experiment
plot_average_best_fitness(all_fitnesses, labels)


'''
def run_experiment(population_size, generations, crossover_probability, mutation_probability, selection, mutation,
                   crossover, elitism, sol_size=312, valid_set=[i for i in range(127)]):
    iterations_fitness = []
    for i in range(10):
        start_time = time.time()

        #create a population
        pop = Population(size=population_size, optim="min", sol_size=sol_size, valid_set=valid_set, repetition=True)

        # Evolve the population for the specified number of generations
        pop.evolve(gens=generations, xo_prob=crossover_probability, mut_prob=mutation_probability,
                   select=selection, mutate=mutation, xo=crossover, elitism=elitism)


        best_fitness = min(ind.fitness for ind in pop.individuals)
        iterations_fitness.append(best_fitness)

        end_time = time.time()
        iteration_time = end_time - start_time
        print(f"Iteration {i + 1} time: {round(iteration_time, 2)} seconds")

    average_fitness = np.mean(iterations_fitness)
    std_fitness = np.std(iterations_fitness)

    return average_fitness, std_fitness

plt.figure(figsize=(10, 6))
plt.errorbar(df_results["Experiment"].values, df_results["Average Fitness"].values, yerr=df_results["Standard Deviation"].values, fmt='o')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Experiment')
plt.ylabel('Average Fitness')
plt.title('Average Fitness of Experiments')
plt.tight_layout()
plt.show()

'''
