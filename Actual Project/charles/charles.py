'''
This file is dedicated to the development of the classes for our project
    1) Individual
    2) Population
'''

#----------Imports----------
from operator import attrgetter
from random import choice, sample, random
from copy import copy
from initializations import melody_rules, major_scale, sobol_sequence


#----------Classes-----------
#1) Individual
class Individual:
    #Initialization
    def __init__(self, representation=None, size=None, valid_set=None, repetition=True):

        if representation is None:

            if repetition:
                # Different Initializations: Random as the Default/Baseline
                self.representation = [choice(valid_set) for i in range(size)]
                #self.representation = melody_rules(size, 2)
                #self.representation = major_scale(size)
                #self.representation = sobol_sequence(size)

            else:
                self.representation = sample(valid_set, size)

        else:
            self.representation = representation

        self.fitness = self.get_fitness()

    # Individual's Methods
    def get_fitness(self):
        raise Exception("You need to monkey patch the fitness function.")

    def get_neighbours(self):
        raise Exception("You need to monkey patch the neighbourhood function.")

    def index(self, value):
        return self.representation.index(value)

    def __len__(self):
        return len(self.representation)

    def __getitem__(self, position):
        return self.representation[position]

    def __setitem__(self, position, value):
        self.representation[position] = value

    def __repr__(self):
        return f" Fitness: {self.fitness}"

#2) Population
class Population:
    #Initialization
    def __init__(self, size, optim, **kwargs):

        # population size
        self.size = size

        # defining the optimization problem as a minimization or maximization problem
        self.optim = optim

        self.individuals = []

        # appending the population with individuals
        for _ in range(size):
            self.individuals.append(
                Individual(
                    size=kwargs["sol_size"],
                    valid_set=kwargs["valid_set"],
                    repetition=kwargs["repetition"]
                )
            )

    # Population's Methods
    def evolve(self, gens, xo_prob, mut_prob, select, xo, mutate, elitism):

        for i in range(gens):
            new_pop = []

            if elitism:
                if self.optim == "max":
                    elite = copy(max(self.individuals, key=attrgetter('fitness')))
                elif self.optim == "min":
                    elite = copy(min(self.individuals, key=attrgetter('fitness')))

                new_pop.append(elite)

            while len(new_pop) < self.size:
                # selection
                parent1, parent2 = select(self), select(self)
                # xo with prob
                if random() < xo_prob:
                    offspring1, offspring2 = xo(parent1, parent2)
                # replication
                else:
                    offspring1, offspring2 = parent1, parent2
                # mutation with prob
                if random() < mut_prob:
                    offspring1 = mutate(offspring1)
                if random() < mut_prob:
                    offspring2 = mutate(offspring2)

                new_pop.append(Individual(representation=offspring1))
                if len(new_pop) < self.size:
                    new_pop.append(Individual(representation=offspring2))

            self.individuals = new_pop

            #if self.optim == "max":
                #print(f"Best individual of gen #{i + 1}: {max(self, key=attrgetter('fitness'))}")
            #elif self.optim == "min":
                #print(f"Best individual of gen #{i + 1}: {min(self, key=attrgetter('fitness'))}")

    def __len__(self):
        return len(self.individuals)

    def __getitem__(self, position):
        return self.individuals[position]

    def sorted_pop(self):
        return sorted(self, key=attrgetter('fitness'), reverse=True)
    # reverse=True by default because used in rank_selection --> sorts in descending order (1st rank = worst/higher fitness)

