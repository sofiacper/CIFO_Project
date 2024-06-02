'''
This file is dedicated to the development of the selection algorithms (selects one individual from the population, repeat N independent executions, until indivs in pop = N ):
:
    1) fps: Fitness Proportionate Selection (FPS) - Roulette Wheel
    2) rank_sel: Rank Selection
    3) tournament_sel: Tournament Selection
'''

#----------Imports-----------------
from operator import attrgetter
from random import uniform, choice


#----------Selection Algorithms------
def fps(population):
    """Fitness proportionate selection implementation - Roulette Wheel.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """
    if population.optim == "max":
        total_fitness = sum([i.fitness for i in population])        # ** .fitness questions
        r = uniform(0, total_fitness)
        position = 0

        for individual in population:
            position += individual.fitness

            if position > r:
                return individual

    elif population.optim == "min":
        # total fitness of the population to define wheel
        # inverting fitness values so lower values of fitness get bigger probability
        # since our fitness can reach 0 (ideally), we add a small constant to avoid division by zero
        total_fitness = sum([1 / (i.fitness + 1e-4) for i in population])
        # random number between 0 and total fitness to select individual (''where roulette stops'')
        r = uniform(0, total_fitness)
        # accumulates inverted fitness values of each individual (according to math expression on S6-08ABR)
        position = 0

        for individual in population:
            position = position + (1.0 / (individual.fitness + 1e-4))

            if position > r:
                return individual
    else:
        raise Exception(f"Optimization not specified (max/min)")


def rank_sel(population):
    """Rank selection implementation.
        Sorts the population by fitness,
            from worst to best:
            (MAX problem - worst = lower fitness, best = higher fitness)
            (MIN problems - worst = higher fitness, best = lower fitness)
        then assigns a rank to each individual.
        Higher rank = better fitness for the min/max problem.
        The probability of selection is proportional to the rank.

    Args:
        population (Population): The population we want to select from.

    Returns:
        Individual: selected individual.
    """
    if population.optim == "max":
        # .sort(reverse=False) sorts in ascending order (1st rank = worst/lower fitness)
        population.sort(key=attrgetter('fitness'), reverse=False)
        total_rank = sum([i + 1 for i in range(len(population))])
        r = uniform(0, total_rank)
        position = 0

        for i, individual in enumerate(population):
            # rank is i+1 since i has 0 index
            position += i + 1

            if position > r:
                return individual

    elif population.optim == "min":
        # .sort(reverse=True) sorts in descending order (1st rank = worst/higher fitness)
        population.sorted_pop()
        total_rank = sum([i + 1 for i in range(len(population))])
        r = uniform(0, total_rank)
        position = 0

        for i, individual in enumerate(population):
            position += i + 1

            if position > r:
                return individual
    else:
        raise Exception(f"Optimization not specified (max/min)")


def tournament_sel(population, tour_size=3):
    """Tournament selection implementation.
        Since 1st step at random, it's not needed to evaluate all fitnesses.
        Only get fitness from individuals selected into tournament.
        Then deterministic choice of best individual in tournament.

    Args:
        population (Population): The population we want to select from.
        tour_size (int): The size of the tournament - must be smaller than P.
                        (higher number -> higher selection pressure, but lower diversity)
    
    Returns:
        Individual: selected individual.
    """
    tournament = [choice(population) for _ in range(tour_size)]     # random choice with uniform distribution

    if population.optim == "max":
        return max(tournament, key=attrgetter('fitness'))

    elif population.optim == "min":
        return min(tournament, key=attrgetter('fitness'))
    