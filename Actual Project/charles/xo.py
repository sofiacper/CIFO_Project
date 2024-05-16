import random
from random import randint
from random import uniform

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
4. Cycle Crossover
5. Partially Mapped Crossover
6. Order Crossover
7. Arithmetic Crossover
8. Blend Crossover
9. BLX-Alpha Crossover
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
        if random.random() < 0.5:
            offspring1[i] = parent1[i]
            offspring2[i] = parent2[i]
        else:
            offspring1[i] = parent2[i]
            offspring2[i] = parent1[i]
    return offspring1, offspring2

'''
def cycle_xo(p1, p2):
    # Offspring placeholders - None values make it easy to debug for errors
    offspring1 = [None] * len(p1.representation)
    offspring2 = [None] * len(p2.representation)
    # While there are still None values in offspring, get the first index of
    # None and start a "cycle" according to the cycle crossover method
    while None in offspring1:
        index = offspring1.index(None)
        val1 = p1.representation[index]
        val2 = p2.representation[index]

        # copy the cycle elements
        while val1 != val2:
            offspring1[index] = p1.representation[index]
            offspring2[index] = p2.representation[index]
            val2 = p2.representation[index]
            index = p1.representation.index(val2)

        # copy the rest
        for element in offspring1:
            if element is None:
                index = offspring1.index(None)
                if offspring1[index] is None:
                    offspring1[index] = p2.representation[index]
                    offspring2[index] = p1.representation[index]

    return offspring1, offspring2


def pm_xo(parent1, parent2):
    size = len(target) #CHANGE THIS
    p1, p2 = [0] * size, [0] * size

    #Initialize the position of each indices in the individuals
    for k in range(size):
        p1[ind1[k]] = k
        p2[ind2[k]] = k
    #Choose crossover points
    cxpoint1 = random.randint(0, size)
    cxpoint2 = random.randint(0, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:  # Swap the two cx points
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

#apply crossover between cx points
    for k in range(cxpoint1, cxpoint2):
    # Keep track of the selected values
        temp1 = ind1[k]
        temp2 = ind2[k]
    #swap the matched value
        ind1[k], ind1[p1[temp2]] = temp2, temp1
        ind2[k], ind2[p2[temp1]] = temp1, temp2
    #record position
        p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
        p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

    return ind1, ind2


def order_xo(parent1, parent2):

'''

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
    alpha = 0.5

    for i in range(len(parent1)):
        weight1 = alpha * parent1[i] + (1 - alpha) * parent2[i]
        weight2 = (1 - alpha) * parent1[i] + alpha * parent2[i]

        offspring1.append(weight1)
        offspring2.append(weight2)

    return offspring1, offspring2

def blx_alpha_xo(parent1, parent2):
    alpha = 0.5  # Exploration intensity parameter
    offspring1 = []
    offspring2 = []

    for i in range(len(parent1)):
        weight_min = min(parent1[i], parent2[i])  # Minimum value between corresponding weights in parents
        weight_max = max(parent1[i], parent2[i])  # Maximum value between corresponding weights in parents

        range_val = weight_max - weight_min  # Range of values between the minimum and maximum

        weight_lower = weight_min - alpha * range_val  # Lower bound of the range
        weight_upper = weight_max + alpha * range_val  # Upper bound of the range

        weight_final_1 = random.uniform(weight_lower, weight_upper)  # Choosing the value in a random way within the range for offspring 1
        weight_final_2 = random.uniform(weight_lower, weight_upper)  # Choosing the value in a random way within the range for offspring 2

        offspring1.append(weight_final_1)   # Add the selected value to offspring 1
        offspring2.append(weight_final_2)   # Add the selected value to offspring 2

    return offspring1, offspring2
