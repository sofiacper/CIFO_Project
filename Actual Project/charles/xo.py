from random import randint, uniform, choice, sample, random


"""Implementation of crossovers.
Args:
    parent1 (Individual): First parent for crossover.
    parent2 (Individual): Second parent for crossover.
Returns:
    Individuals: Two offspring, resulting from the crossover.
    
Crossovers:
1. Single Point Crossover
2. Two Point Crossover
3. Uniform Crossover
4. Order Crossover
5. Arithmetic Crossover
6. Blend Crossover
7. BLX-Alpha Crossover
"""

def single_point_xo(parent1, parent2):
    xo_point = randint(1, len(parent1) - 1)
    offspring1 = parent1[:xo_point] + parent2[xo_point:]
    offspring2 = parent2[:xo_point] + parent1[xo_point:]
    return offspring1, offspring2

#can have several breaking points
def two_point_xo(parent1, parent2): #this one in specific is two point xo
    xo_point1 = randint(1, len(parent1) - 2)
    xo_point2 = randint(xo_point1 + 1, len(parent2) - 1)
    #make sure the second crossover point is bigger than the first to avoiding indexing errors
    offspring1 = parent1[:xo_point1] + parent2[xo_point1:xo_point2] + parent1[xo_point2:]
    offspring2 = parent2[:xo_point1] + parent1[xo_point1:xo_point2] + parent2[xo_point2:]
    return offspring1, offspring2


#differently from cycle_xo, a random decision is made independently of the other gene positions
def uniform_xo(parent1, parent2):
    #initialize offspring with the same length as parents
    offspring1 = [None] * len(parent1)
    offspring2 = [None] * len(parent2)
    for i in range(len(parent1)):
        #randomly decide whether to inherit from parent 1 or parent 2
        if random() < 0.5:
            offspring1[i] = parent1[i]
            offspring2[i] = parent2[i]
        else:
            offspring1[i] = parent2[i]
            offspring2[i] = parent1[i]
    return offspring1, offspring2


def order_one_xo(parent1, parent2):
    size = len(parent1.representation)
    offspring1 = [None] * size
    offspring2 = [None] * size

    #randomly select a subsequence
    start, end = sorted(sample(range(size), 2))

    #copy the subsequence into the offspring
    offspring1[start:end + 1] = parent1.representation[start:end + 1]
    offspring2[start:end + 1] = parent2.representation[start:end + 1]

    #fill the remaining positions in both offspring
    current_pos1, current_pos2 = (end + 1) % size, (end + 1) % size
    for gene in parent2.representation:
        if gene not in offspring1:
            offspring1[current_pos1] = gene
            current_pos1 = (current_pos1 + 1) % size
        if gene not in offspring2:
            offspring2[current_pos2] = gene
            current_pos2 = (current_pos2 + 1) % size

    return offspring1, offspring2

def arithmetic_xo(parent1, parent2):
    # create r - only one randomly generated value between 0 and 1, in a uniform distribution
    alpha = uniform(0,1)

    offspring1 = []
    offspring2 = []

    for i in range(len(parent1)):
        offspring1.append(alpha * parent1[i] + (1 - alpha) * parent2[i])
        offspring2.append((1 - alpha) * parent1[i] + alpha * parent2[i])

    return offspring1, offspring2

def blend_xo(parent1, parent2):
    offspring1 = []
    offspring2 = []

    for i in range(len(parent1)):
        # Determine the range based on parent values
        weight_min = min(parent1[i], parent2[i])
        weight_max = max(parent1[i], parent2[i])

        # Randomly select a value within the range for offspring
        weight1 = uniform(weight_min, weight_max)
        weight2 = uniform(weight_min, weight_max)

        # Add the selected value to offspring
        offspring1.append(weight1)
        offspring2.append(weight2)

    return offspring1, offspring2

def blx_alpha_xo(parent1, parent2):
    alpha = 0.5  # exploration intensity parameter
    offspring1 = []
    offspring2 = []

    for i in range(len(parent1)):
        #minimum and maximum value between corresponding weights in parents
        weight_min = min(parent1[i], parent2[i])
        weight_max = max(parent1[i], parent2[i])

        range_val = weight_max - weight_min  # Range of values between the minimum and maximum

        weight_lower = weight_min - alpha * range_val  #lower bound of the range
        weight_upper = weight_max + alpha * range_val  #upper bound of the range

        # choosing the value in a random way within the range for offsprings
        weight_final_1 = uniform(weight_lower, weight_upper)
        weight_final_2 = uniform(weight_lower, weight_upper)

        # Add the selected value to offsprings
        offspring1.append(weight_final_1)
        offspring2.append(weight_final_2)

    return offspring1, offspring2
