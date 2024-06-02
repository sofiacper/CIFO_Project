#__________________Imports________________________
from math import sqrt
from charles.charles import Individual, Population


#__________________Target________________________
target = [76, 12, 76, 12, 20, 12, 76, 12, 20, 12, 72, 12, 76, 12, 20, 12, 79, 12, 20, 36, 67, 12, 20, 36, 72, 12, 20,
          24, 67, 12, 20, 24, 64, 12, 20, 24, 69, 12, 20, 12, 71, 12, 20, 12, 70, 12, 69, 12, 20, 12, 67, 16, 76, 16,
          79, 16, 81, 12, 20, 12, 77, 12, 79, 12, 20, 12, 76, 12, 20, 12, 72, 12, 74, 12, 71, 12, 20, 24, 48, 12, 20,
          12, 79, 12, 78, 12, 77, 12, 75, 12, 60, 12, 76, 12, 53, 12, 68, 12, 69, 12, 72, 12, 60, 12, 69, 12, 72, 12,
          74, 12, 48, 12, 20, 12, 79, 12, 78, 12, 77, 12, 75, 12, 55, 12, 76, 12, 20, 12, 84, 12, 20, 12, 84, 12, 84,
          12, 55, 12, 20, 12, 48, 12, 20, 12, 79, 12, 78, 12, 77, 12, 75, 12, 60, 12, 76, 12, 53, 12, 68, 12, 69, 12,
          72, 12, 60, 12, 69, 12, 72, 12, 74, 12, 48, 12, 20, 12, 75, 24, 20, 12, 74, 24, 20, 12, 72, 24, 20, 12, 55,
          12, 55, 12, 20, 12, 48, 12, 72, 12, 72, 12, 20, 12, 72, 12, 20, 12, 72, 12, 74, 12, 20, 12, 76, 12, 72, 12,
          20, 12, 69, 12, 67, 12, 20, 12, 43, 12, 20, 12, 72, 12, 72, 12, 20, 12, 72, 12, 20, 12, 72, 12, 74, 12, 76,
          12, 55, 12, 20, 24, 48, 12, 20, 24, 43, 12, 20, 12, 72, 12, 72, 12, 20, 12, 72, 12, 20, 12, 72, 12, 74, 12,
          20, 12, 76, 12, 72, 12, 20, 12, 69, 12, 67, 12, 20, 12, 43, 12, 20, 12, 76, 12, 76, 12, 20, 12, 76, 12, 20,
          12, 72, 12, 76, 12, 20, 12, 79, 12, 20, 36, 67, 12, 20, 36]

#print(len(target))

#__________________Methods________________________
'''   def get_fitness(self):
    """A simple objective function to calculate distances
    for the TSP problem.

    Returns:
        int: the total distance of the path
    """
    fitness = 0
    for i in range(len(self.representation)):
        if self.representation[i] is not None:
            fitness += (target[i] - self.representation[i]) ** 2
    return round(sqrt(fitness))
'''


def get_fitness(self, weight_distance=0.5, weight_non_matching=0.5):
    """A weighted objective function combining two criteria for the TSP problem.

    Args:
        weight_existing (float): Weight assigned to the existing fitness criterion. Default is 0.7.
        weight_non_matching (float): Weight assigned to the non-matching characters criterion. Default is 0.3.

    Returns:
        float: The combined fitness value of the individual.
    """
    dist_fitness = 0
    for i in range(len(self.representation)):
        if self.representation[i] is not None:
            dist_fitness += (target[i] - self.representation[i]) ** 2

    non_matching_fitness = sum(1 for i in range(len(self.representation)) if target[i] != self.representation[i])

    fitness = (weight_distance * sqrt(dist_fitness)) + (weight_non_matching * non_matching_fitness)
    return round(fitness)

def get_neighbours(self):
    """A neighbourhood function for the TSP problem. Switch
    indexes around in pairs.

    Returns:
        list: a list of individuals
    """
    n = [copy(self.representation) for _ in range(len(self.representation)-1)]

    for i, ne in enumerate(n):
        ne[i], ne[i+1] = ne[i+1], ne[i]

    n = [Individual(ne) for ne in n]
    return n

# Monkey patching
Individual.get_fitness = get_fitness
Individual.get_neighbours = get_neighbours

P = Population(size=20, optim="min", sol_size=312,
                 valid_set=[i for i in range(127)], repetition=True)



