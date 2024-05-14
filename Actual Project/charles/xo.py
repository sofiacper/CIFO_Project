import random
from random import randint

"""Implementation of crossovers.
Args:
    parent1 (Individual): First parent for crossover.
    parent2 (Individual): Second parent for crossover.
Returns:
    Individuals: Two offspring, resulting from the crossover.
"""

def single_point_xo(parent1, parent2):
    xo_point = randint(1, len(parent1) - 1)
    offspring1 = parent1[:xo_point] + parent2[xo_point:]
    offspring2 = parent2[:xo_point] + parent1[xo_point:]
    return offspring1, offspring2

#can have several breaking points
def multi_point_xo(parent1, parent2): #this one in specific is two point xo
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
def cycle_xo(parent1, parent2):
    offspring1 = [None] * len(parent1)
    offspring2 = [None] * len(parent2)
    visited = [False] * len(parent1) #initialize a array to track visited indices
    cycle_start = 0
    while True:
        index = cycle_start
        while not visited[index]:
            #inherit genes from the current parent
            offspring1[index] = parent1[index]
            offspring2[index] = parent2[index]
            visited[index] = True #mark the index as visited
            #find corresponding index in the other parent
            index = parent1.index(parent2[index])

        #switch to the other parent
        cycle_start = visited.index(False)

        if cycle_start == 0: #when the cycle is complete
            break

    #fill in remaining genes
    for i in range(len(parent1)):
        if offspring1[i] is None:
            offspring1[i] = parent2[i]
        if offspring2[i] is None:
            offspring2[i] = parent1[i]

    return offspring1, offspring2


def pm_xo(parent1, parent2):
    size = len(cities) #CHANGE THIS
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