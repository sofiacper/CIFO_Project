import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from charles.charles import Population, Individual
from song import get_fitness
<<<<<<< Updated upstream
from charles.selection import fps, tournament_sel, rank
=======
from charles.selection import fps, tournament_sel, rank_sel
>>>>>>> Stashed changes
from charles.mutation import swap_mutation, random_reseting, inversion_mutation, scramble_mutation, centre_inverse_mutation
from charles.xo import single_point_xo, two_point_xo, uniform_xo, arithmetic_xo, blend_xo, blx_alpha_xo, order_one_xo
from charles.geooperators import geometric_mutation, geometric_xo
# Individual Monkey Patching
Individual.get_fitness = get_fitness

# Improved Experiment Labeling
def run_experiment(population_size, generations, crossover_probability, mutation_probability, selection, mutation,
                   crossover, elitism, sol_size=312, valid_set=[i for i in range(127)]):
    all_fitness = []

    for i in range(5):  #number of runs
        start_time = time.time()

        #Create a population
        pop = Population(size=population_size, optim="min", sol_size=sol_size, valid_set=valid_set, repetition=True)

        #track fitness for each generation
        generation_fitness = []
        for gen in range(generations):
            pop.evolve(gens=generations, xo_prob=crossover_probability, mut_prob=mutation_probability,
                       select=selection, mutate=mutation, xo=crossover, elitism=elitism)
            best_fitness = min(ind.fitness for ind in pop.individuals)
            generation_fitness.append(best_fitness)

            #print best fitness for the current generation and the run (podemos tirar isto se ficar pesado era so para eu ver s estava bem)
            print(f"Run #{i + 1}, Generation #{gen + 1}: Best Fitness: {best_fitness}")

        all_fitness.append(generation_fitness)

        end_time = time.time()
        iteration_time = end_time - start_time
        print(f"Iteration {i + 1} time: {round(iteration_time, 2)} seconds")

    #transpose all_fitness to have each generation's best fitnesses in the same list
    all_fitness = list(map(list, zip(*all_fitness)))

    #compute the median best fitness for each generation across all runs
    median_best_fitness_per_gen = [np.median(gen_fitness) for gen_fitness in all_fitness]

    return median_best_fitness_per_gen

#population_size, generations, crossover_probability, mutation_probability, selection, mutation, crossover

<<<<<<< Updated upstream
#quando testarem os crossovers, deixar o codigo abaixo comentado (so o das configurações)
#crossovers (é so alterar o algoritmo de seleção)

=======
#_______________________Possible tests:_________________________

#  1) xo: To test xo's uncomment the code bellow
'''
#Nota: Aqui só está o exemplo de fps, para testar tudo mudar o algoritmo de seleção
>>>>>>> Stashed changes
experiments = [
    [100, 300, 0.9, 0.2, fps, swap_mutation, single_point_xo, True],
    [100, 300, 0.9, 0.2, fps, swap_mutation, two_point_xo, True],
    [100, 300, 0.9, 0.2, fps, swap_mutation, uniform_xo, True],
    [100, 300, 0.9, 0.2, fps, swap_mutation, arithmetic_xo, True],
    [100, 300, 0.9, 0.2, fps, swap_mutation, blend_xo, True],
    [100, 300, 0.9, 0.2, fps, swap_mutation, blx_alpha_xo, True],
    [100, 300, 0.9, 0.2, fps, swap_mutation, order_one_xo, True]
]
<<<<<<< Updated upstream

"""
#quando testarem as mutations, comentar o codigo acima (so o das configurações) e descomentar este
#mutations (é so alterar o algoritmo de seleção)
=======
'''

#  2) mutation: To test mutation uncomment the code bellow
'''
#Nota: Aqui só está o exemplo de fps, para testar tudo mudar o algoritmo de seleção
>>>>>>> Stashed changes
experiments = [
    [100, 300, 0.9, 0.2, fps, swap_mutation, single_point_xo, True],
    [100, 300, 0.9, 0.2, fps, random_reseting, single_point_xo, True],
    [100, 300, 0.9, 0.2, fps, inversion_mutation, single_point_xo, True],
    [100, 300, 0.9, 0.2, fps, scramble_mutation, single_point_xo, True],
    [100, 300, 0.9, 0.2, fps, centre_inverse_mutation, single_point_xo, True]
]
<<<<<<< Updated upstream
""""
=======
'''
# 3) geometric operators:  To test mutation uncomment the code bellow

experiments = [
    [250, 50, 0.9, 0.2, fps, geometric_mutation, geometric_xo, True],
    [250, 50, 0.9, 0.2, rank_sel, geometric_mutation, geometric_xo, True],
    [250, 50, 0.9, 0.2, tournament_sel, geometric_mutation, geometric_xo, True],
]

>>>>>>> Stashed changes

#run the experiments and store results
all_median_fitnesses = []

for exp in experiments:
    all_median_fitnesses.append(run_experiment(population_size=exp[0], generations=exp[1], crossover_probability=exp[2],
                                        mutation_probability=exp[3], selection=exp[4], mutation=exp[5],
                                        crossover=exp[6], elitism=exp[7]))

def create_labels(experiments):
    labels = []
    for exp in experiments:
        label_parts = []
        label_parts.append(f"{exp[4].__name__}") #selection
        #label_parts.append(f"{exp[5].__name__}") #mutation
        #label_parts.append(f"{exp[6].__name__}") #crossover
        labels.append(", ".join(label_parts))
    return labels

#create as labels para os graficos
labels = create_labels(experiments)


#function to automatically plot the graph
def plot_average_best_fitness(all_median_fitnesses, labels):
    #plot the median best fitness per generation for each experiment
    for i, median_best_fitness in enumerate(all_median_fitnesses):
        plt.plot(range(1, len(median_best_fitness) + 1), median_best_fitness, marker='o', linestyle='-', label=labels[i])

    plt.title('Median Best Fitness per Generation')
    plt.xlabel('Generation')
    plt.ylabel('Median Best Fitness')
    plt.legend()
    plt.grid(True)
    plt.show()


#plots the graph for each experiment
plot_average_best_fitness(all_median_fitnesses, labels)


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

plt.figure(figsize=(10, 6))
plt.errorbar(df_results["Experiment"].values, df_results["Average Fitness"].values, yerr=df_results["Standard Deviation"].values, fmt='o')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Experiment')
plt.ylabel('Average Fitness')
plt.title('Average Fitness of Experiments')
plt.tight_layout()
plt.show()

'''
