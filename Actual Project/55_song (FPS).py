from copy import copy
from math import sqrt
import seaborn as sns
import matplotlib.pyplot as plt
from random import uniform

from charles.charles import Population, Individual
from charles.geooperators import geometric_xo, geometric_mutation
from charles.mutation import (swap_mutation, random_reseting, inversion_mutation,
                              scramble_mutation, centre_inverse_mutation)
from charles.selection import fps, rank_sel, tournament_sel
from charles.utils_functions import repeat_n_runs, get_ABF, plot_ABF, get_MBF
from charles.xo import (single_point_xo, two_point_xo, uniform_xo,
                        order_one_xo, arithmetic_xo, blend_xo, blx_alpha_xo)

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

print(len(target))


def get_fitness(self):
    """Function that calculates distances between the notes.

    Returns:
        int: the total distances of the path
    """
    fitness = 0
    for i in range(len(self.representation)):
        if self.representation[i] is not None:
            fitness += (target[i] - self.representation[i]) ** 2
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

P = Population(size=100, optim="min", sol_size=312,
                 valid_set=[i for i in range(127)], repetition=True)


"""
                                    TESTING COMBINATIONS FOR FPS

# SELECTION = FPS
# MUTATION PROB = 0.15
# CROSSOVER (XO) PROB = 0.9
"""

"""
FIXED SELECTION + XO SINGLE_POINT_XO
"""
# FPS - XO: single_point_xo - M: swap_mut                       (552, 564, 524)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=single_point_xo, mutate=swap_mutation, elitism=True)


# FPS - XO: single_point_xo - M: random_resetting               (668, 488, 601)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=single_point_xo, mutate=random_reseting, elitism=True)


# FPS - XO: single_point_xo - M: inversion_mutation             (503, 453, 456)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=single_point_xo, mutate=inversion_mutation, elitism=True)


# FPS - XO: single_point_xo - M: scramble_mutation              (491, 487, 559)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=single_point_xo, mutate=scramble_mutation, elitism=True)


# FPS - XO: single_point_xo - M: centre_inverse_mutation        (512, 542, 530)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=single_point_xo, mutate=centre_inverse_mutation, elitism=True)

"""
FIXED SELECTION + XO TWO_POINT_XO
"""
# FPS - XO: two_point_xo - M: swap_mut                       (517, 500, 507)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=two_point_xo, mutate=swap_mutation, elitism=True)


# FPS - XO: two_point_xo - M: random_resetting               (604, 574, 553)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=two_point_xo, mutate=random_reseting, elitism=True)


# FPS - XO: two_point_xo - M: inversion_mutation             (513, 505, 590)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=two_point_xo, mutate=inversion_mutation, elitism=True)


# FPS - XO: two_point_xo - M: scramble_mutation              (515, 497, 591)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=two_point_xo, mutate=scramble_mutation, elitism=True)


# FPS - XO: two_point_xo - M: centre_inverse_mutation        (617, 479, 523)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=two_point_xo, mutate=centre_inverse_mutation, elitism=True)


"""
FIXED SELECTION + XO UNIFORM_XO

For all mutations:
AttributeError: 'builtin_function_or_method' object has no attribute 'random')
"""
# FPS - XO: uniform_xo - M: swap_mut                        (
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=uniform_xo, mutate=swap_mutation, elitism=True)


# FPS - XO: uniform_xo - M: random_resetting               (
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=uniform_xo, mutate=random_reseting, elitism=True)


# FPS - XO: uniform_xo - M: inversion_mutation             (
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=uniform_xo, mutate=inversion_mutation, elitism=True)


# FPS - XO: uniform_xo - M: scramble_mutation              (
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=uniform_xo, mutate=scramble_mutation, elitism=True)


# FPS - XO: uniform_xo - M: centre_inverse_mutation        (
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=uniform_xo, mutate=centre_inverse_mutation, elitism=True)


"""
FIXED SELECTION + XO ORDER_ONE_XO
Quite slower than combinations before
"""
# FPS - XO: order_one_xo - M: swap_mut                        (503, 511, 478)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=order_one_xo, mutate=swap_mutation, elitism=True)


# FPS - XO: order_one_xo - M: random_resetting               (431, 445, 456)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=order_one_xo, mutate=random_reseting, elitism=True)


# FPS - XO: order_one_xo - M: inversion_mutation             (457)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=order_one_xo, mutate=inversion_mutation, elitism=True)


# FPS - XO: order_one_xo - M: scramble_mutation              (516)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=order_one_xo, mutate=scramble_mutation, elitism=True)


# FPS - XO: order_one_xo - M: centre_inverse_mutation        (511)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=order_one_xo, mutate=centre_inverse_mutation, elitism=True)


"""
FIXED SELECTION + XO ARITHMETIC_XO
"""
# FPS - XO: arithmetic_xo - M: swap_mut                        (681, 682, 695)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=arithmetic_xo, mutate=swap_mutation, elitism=True)


# FPS - XO: arithmetic_xo - M: random_resetting               (672, 650, 679)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=arithmetic_xo, mutate=random_reseting, elitism=True)


# FPS - XO: arithmetic_xo - M: inversion_mutation             (688, 676, 691)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=arithmetic_xo, mutate=inversion_mutation, elitism=True)


# FPS - XO: arithmetic_xo - M: scramble_mutation              (683, 687, 681 - estagna antes das 100gens)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=arithmetic_xo, mutate=scramble_mutation, elitism=True)


# FPS - XO: arithmetic_xo - M: centre_inverse_mutation        (701, 690,685 - estagna antes das 100gens)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=arithmetic_xo, mutate=centre_inverse_mutation, elitism=True)


"""
FIXED SELECTION + XO BLEND_XO
"""                                                      # interval between gen 0 - gen 500)
# FPS - XO: blend_xo - M: swap_mut                          (777-683, 782-686, 769-687)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=blend_xo, mutate=swap_mutation, elitism=True)


# FPS - XO: order_one_xo - M: random_resetting               (533-450, 547-449, 543-442)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=order_one_xo, mutate=random_reseting, elitism=True)


# FPS - XO: order_one_xo - M: inversion_mutation             (555-484, 543-506, 547-489)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=order_one_xo, mutate=inversion_mutation, elitism=True)


# FPS - XO: order_one_xo - M: scramble_mutation              (549-472)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=order_one_xo, mutate=scramble_mutation, elitism=True)


# FPS - XO: order_one_xo - M: centre_inverse_mutation        (559-485)
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=order_one_xo, mutate=centre_inverse_mutation, elitism=True)


"""
FIXED SELECTION + XO BLX_APLHA_XO
AttributeError: 'builtin_function_or_method' object has no attribute 'uniform'
"""
# FPS - XO: blx_alpha_xo - M: swap_mut                        (
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=blx_alpha_xo, mutate=swap_mutation, elitism=True)


# FPS - XO: blx_alpha_xo - M: random_resetting               (
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=blx_alpha_xo, mutate=random_reseting, elitism=True)


# FPS - XO: blx_alpha_xo - M: inversion_mutation             (
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=blx_alpha_xo, mutate=inversion_mutation, elitism=True)


# FPS - XO: blx_alpha_xo - M: scramble_mutation              (
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=blx_alpha_xo, mutate=scramble_mutation, elitism=True)


# FPS - XO: blx_alpha_xo - M: centre_inverse_mutation        (
# P.evolve(gens=500, xo_prob=0.9, mut_prob=0.15, select=fps,
# xo=blx_alpha_xo, mutate=centre_inverse_mutation, elitism=True)
