from random import randint, sample, choices, shuffle, choice

def swap_mutation(individual):
    """
    Perform a swap mutation on a given individual.

    This mutation involves randomly selecting two positions in the individual
    and swapping their values. 

    Args:
    individual (list): A list representing the chromosome (individual) to be mutated.

    Returns:
    list: The mutated individual with two elements swapped.
    """
    mut_indexes = sample(range(0, len(individual)), 2)
    individual[mut_indexes[0]], individual[mut_indexes[1]] = individual[mut_indexes[1]], individual[mut_indexes[0]]
    return individual

def random_reseting(individual, n=5): 
    """
    Perform random resetting mutation on an array of numbers.

    In random resetting, n random positions are selected in the individual, and their
    values are replaced with random values from a specified range (127 MIDI notes).

    Args:
    individual (list): A list representing the chromosome (individual) to be mutated.
    n (int): The number of positions to be randomly reset. Default is 5.

    Returns:
    list: The mutated individual with n positions reset to random values.
    """

    mut_indexes = sample(range(0, len(individual)), n)
    new_numbers = choices(range(128), k=n)

    for i in range(n):
        individual[mut_indexes[i]] = new_numbers[i]

    return individual

def inversion_mutation(individual):
    """
    Perform inversion mutation on a given individual.

    In inversion mutation, a segment of the chromosome between two randomly
    selected points is reversed (inverted).

    Args:
    individual (list): A list representing the chromosome (individual) to be mutated.

    Returns:
    list: The mutated individual with a segment inverted.
    """

    mut_indexes = sample(range(len(individual)),2)
    mut_indexes.sort()
    individual[mut_indexes[0]: mut_indexes[1]] = individual[mut_indexes[0]:mut_indexes[1]][::-1]

    return individual

def scramble_mutation(individual):
    """
    Perform a scramble mutation on a given individual.

    In scramble mutation, a subset of the chromosome is randomly shuffled.
    Two random indices are selected, and the elements between these indices
    are shuffled to create variation.

    Args:
    individual (list): A list representing the chromosome (individual) to be mutated.

    Returns:
    list: The mutated individual with a scrambled subset of genes.
    """
    mut_indexes = (sample(range(len(individual)),2))
    mut_indexes.sort()

    subset = individual[mut_indexes[0]: mut_indexes[1]]
    shuffle(subset)

    individual[mut_indexes[0]: mut_indexes[1]] = subset

    return individual


def centre_inverse_mutation(individual):
    """
    Perform a centre inverse mutation on a given individual.

    The chromosome is divided into two sections at a random index, and the genes in each
    section are inversely placed (reversed).

    Args:
    individual (list): A list representing the chromosome (individual) to be mutated.

    Returns:
    list: The mutated individual with each section reversed
    """

    mut_index = choice(range(len(individual)))
    individual[:mut_index] = individual[:mut_index][::-1]
    individual[mut_index:] = individual[mut_index:][::-1]

    return individual

#testing functions
#test = [1,2,3,4,5,6,7,8,9]
#random_reseting(test)
