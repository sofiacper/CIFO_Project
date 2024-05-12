from charles.charles import Population, Individual
#from charles.search import hill_climb, sim_annealing
from copy import copy
from math import sqrt
from charles.selection import fps, tournament_sel
from charles.mutation import swap_mutation
from charles.xo import cycle_xo, single_point_xo

def get_fitness(self):
    """A simple objective function to calculate distances
    for the TSP problem.

    Returns:
        int: the total distance of the path
    """
    fitness = 0
    target = [60,60,62,64,64,62,60,59,59,60,60,59,59,60,60,62,64,64,62,60,59,59,60,59, 60, 59, 59, 59,59, 60, 59, 60, 62, 60, 59, 60, 59, 60, 62, 64, 62, 60, 60, 62, 64, 64, 62, 60, 59, 59, 60, 59,60, 59, 59]
    for i in range(len(self.representation)):
        fitness += ((target[i] - self.representation[i]))**2
    return round(sqrt(fitness))


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

P = Population(size=40, optim="min", sol_size=55,
                 valid_set=[i for i in range(127)], repetition = True)

P.evolve(gens=30, xo_prob=0.9, mut_prob=0.15, select=tournament_sel,xo=single_point_xo, mutate=swap_mutation, elitism=True)

#hill_climb(P)
#sim_annealing(P)