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

def multi_point_xo(parent1, parent2): #this one in specific is two point xo
    xo_point1 = randint(1, len(parent1) - 2)
    xo_point2 = randint(xo_point1 + 1, len(parent2) - 1) #make sure the second crossover point is
    #bigger than the first to avoiding
    #indexing errors
    offspring1 = parent1[:xo_point1] + parent2[xo_point1:xo_point2] + parent1[xo_point2:]
    offspring2 = parent2[:xo_point1] + parent1[xo_point1:xo_point2] + parent2[xo_point2:]
    return offspring1, offspring2


'''
def uniform_crossover(parent1, parent2):


def cycle_xo(p1, p2):
    # offspring placeholders
    offspring1 = [None] * len(p1)
    offspring2 = [None] * len(p1)

    while None in offspring1:
        index = offspring1.index(None)
        val1 = p1[index]
        val2 = p2[index]

        # copy the cycle elements
        while val1 != val2:
            offspring1[index] = p1[index]
            offspring2[index] = p2[index]
            val2 = p2[index]
            index = p1.index(val2)

        # copy the rest
        for element in offspring1:
            if element is None:
                index = offspring1.index(None)
                if offspring1[index] is None:
                    offspring1[index] = p2[index]
                    offspring2[index] = p1[index]

    return offspring1, offspring2

def pm_xo(parent1, parent2):

def order_xo(parent1, parent2):
'''