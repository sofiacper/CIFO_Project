import seaborn as sns
import matplotlib.pyplot as plt
from copy import copy

# Susana To-Do List on the end of this file


# COMPARISON AGAINST ITERATIONS:
"""
MAIN QUESTIONS - PLEASE I NEED BRAINSTORMING WITH YOU :)

Posso só definir funções ou vou ter que criar uma classe para suportar as funções?
Como é que ponho o P.evolve do 55_song a dar output de generations e best fitness per generation?
A partir daqui é só acertar as nomenclaturas e raciocínio & it should work.
"""

# Function to repeat independent runs of genetic algorithm
def repeat_n_runs(implementation, n_runs):
    """Repeat N independent executions (n_runs).

    Args:
        implementation (P.evolve): Genetic algorithm implementation. ***
        n_runs (int): Number of independent runs.

    Returns:
        array: number of generations per independent run with the best fitness per generation.

*** 55_song
I need to get P.evolve to output generations (generations) and best fitness per generation(bfit_per_gen).
How tf do I do that?
    """
# Which of the options makes more sense?
# OP 1

    all_gens = []  # Initialize list to store generations per run

    for _ in range(n_runs):
        # Execute the genetic algorithm implementation
        # Assuming implementation returns generations and best fitness per generation
        generations, bfit_per_gen = implementation()  

        # Append the number of generations along with best fitness per generation to the list
        all_gens.append((generations, bfit_per_gen))

    return all_gens

# OP 2

    pop_list = []
    for i in range(n_runs):
        pop = copy(implementation.population)
        generations = []
        best_fitness = []
        while len(pop) < implementation.N:
            # Run the genetic algorithm for one generation
            pop.run_one_generation()
            # Save the generation number and best fitness
            generations.append(pop.generation)
            best_fitness.append(pop.best_fitness)
        pop_list.append((generations, best_fitness))
    return pop_list


# Function to get ABF
def get_ABF(all_gens):
    """Get the average best fitness (ABF) per each generation, over all independent runs.

    Args:
        all_generations (array): number of generations per independent run with the best fitness per generation.

    Returns:
        float: average best fitness over all independent runs.
    """
    # Initialize list to store best fitness per generation
    ABF_per_gen = []

    # Iterate over all independent runs
    for generations, best_fitness in all_gens:
        # Append the best fitness per generation to the list
        ABF_per_gen.append(best_fitness)

    # Calculate the average best fitness over all independent runs
    ABF = sum(ABF_per_gen) / len(ABF_per_gen)

    return ABF


# Function to plot ABF - for now one plot per implementation
# After deciding between which ones to compare, I'll adjust the code to it?
def plot_ABF(all_gens):
    """Plot the average best fitness (ABF) per generation, over all independent runs.

    Args:
        all_generations (array): number of generations per independent run with the best fitness per generation.

    Returns:
        plot: plot of the average best fitness over all independent runs.
    """
    # Get the average best fitness over all independent runs
    ABF = get_ABF(all_gens)

    # Plot the average best fitness per generation
    plt.plot(ABF)
    plt.show()


# Function to get MBF
def get_MBF(all_gens):
    """Get the median value of best fitness (MBF) per each generation, over all independent runs.

    Args:
        all_generations (array): number of generations per independent run with the best fitness per generation.

    Returns:
        float: median value of best fitness over all independent runs.
    """
    # Initialize list to store best fitness per generation
    MBF_per_gen = []

    # Iterate over all independent runs
    for generations, best_fitness in all_gens:
        # Append the best fitness per generation to the list
        MBF_per_gen.append(best_fitness)

    # Calculate the median value of best fitness over all independent runs

    # how to get median value of best fitness per generation?
    # MBF = sum(MBF_per_gen) / len(MBF_per_gen) - not like this !?

    return MBF

















# SUSANA TO-DO:
# Function to repeat independent runs of genetic algorithm.
# Function to get ABF
# Fucntion to plot ABF
# Function to get_MBF
# Function to plot_MBF
# Function to get SR (successful runs)