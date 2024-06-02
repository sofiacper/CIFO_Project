'''
This file is dedicated to the development of the geometric operators:
    1) geometric_xo
    2) geometric_mutation
'''

#----------Imports-----------------
import numpy as np
from random import uniform

#----------Geometric Operators------
def geometric_xo(parent1, parent2):
    """Implementation of geometric crossover.

    Args:
        parent1 (Individual): First parent for crossover.
        parent2 (Individual): Second parent for crossover.

    Returns:
        individuals: Two offspring, resulting from the crossover.
    """
    # Create arrays to store the child chromosomes
    offspring1 = np.zeros_like(parent1)
    offspring2 = np.zeros_like(parent2)

    # Perform crossover for each gene in the chromosomes
    for i in range(len(parent1)):
        alpha=uniform(0,1)
        # Perform geometric crossover
        offspring1[i] = alpha * parent1[i] + (1 - alpha) * parent2[i]
        offspring2[i] = (1 - alpha) * parent1[i] + alpha * parent2[i]

    return offspring1, offspring2

'''
#______________Test Example___________________
parent1 = [64, 2, 3, 4, 5]
parent2 = [13, 7, 8, 9, 10]
alpha = 0.4

offspring1, offspring2 = geometric_xo(parent1, parent2, alpha)

# Print the results
print("Offspring 1:", offspring1)
print("Offspring 2:", offspring2)
'''

def geometric_mutation(individual, mutation_step=1):
    """
    Perform geometric mutation on an individual.
    Parameters:
        individual: The individual to be mutated.
        mutation_step (float): The scale parameter for generating the mutation value.

    Returns:
        individual: The mutated individual.
    """
    mutated_individual = np.copy(individual)

    # Perform mutation for each gene in the individual
    for i in range(len(individual)):
        # Generate a random mutation value from a uniform distribution
        mutation_value = np.random.uniform(-mutation_step, mutation_step)

        # Apply mutation to the gene
        mutated_individual[i] += mutation_value

        #Atention: PROBLEM SPECIFICATIONS
        #--All individual values should stay within the range [1, 127]
        mutated_individual[i] = np.clip(mutated_individual[i], 1, 127)

    return mutated_individual

'''
#______________Test Example___________________
parent1 = [127, 127, 1, 3, 8]
off1=geometric_mutation(parent1)
print(off1)
'''