import numpy as np
def geometric_xo(parent1, parent2, alpha=0.9):
    """Implementation geometric semantic crossover.

    Args:
        parent1 (Individual): First parent for crossover.
        parent2 (Individual): Second parent for crossover.
        alpha (float): Crossover parameter that indicates the contribution of each parent.

    Returns:
        Individuals: Two offspring, resulting from the crossover.
    """
    # Create an array to store the child chromosomes
    offspring1 = np.zeros_like(parent1)
    offspring2 = np.zeros_like(parent2)

    # Perform crossover for each gene in the chromosomes
    for i in range(len(parent1)):
        # Perform geometric crossover
        offspring1[i] = alpha * parent1[i] + (1 - alpha) * parent2[i]
        offspring2[i] = (1 - alpha) * parent1[i] + alpha * parent2[i]

    return offspring1, offspring2


"""""# Example usage
parent1 = [1, 2, 3, 4, 5]
parent2 = [6, 7, 8, 9, 10]
alpha = 0.5

# Perform geometric crossover
offspring1, offspring2 = geometric_xo(parent1, parent2, alpha)

# Print the results
print("Offspring 1:", offspring1)
print("Offspring 2:", offspring2)
"""



def geometric_mutation(individual, mutation_step=0.9):
    """
    Perform geometric semantic mutation on an individual.

    Parameters:
        Individual: The individual to be mutated.
        mutation_rate (float): The probability of mutation for each gene.
        mutation_step (float): The scale parameter for generating the mutation value.

    Returns:
        Individual: The mutated individual.
    """
    mutated_individual = np.copy(individual)

    # Perform mutation for each gene in the individual
    for i in range(len(individual)):
        # Generate a random mutation value from a uniform distribution
        mutation_value = np.random.uniform(-mutation_step, mutation_step)

        # Apply mutation to the gene
        mutated_individual[i] += mutation_value

        #Atention:PROBLEM SPECIFICATIONS
        #--All individual values should stay within the range [1, 127]
        mutated_individual[i] = np.clip(mutated_individual[i], 1, 127)
        # --All individual values must be integer
        mutated_individual[i] = round(mutated_individual[i])

    return mutated_individual




"""""
# Example usage
parent1 = [1, 2, 3, 4, 5]
off1=geometric_mutation(parent1)
print(off1)
"""