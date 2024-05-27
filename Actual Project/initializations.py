import numpy as np
from scipy.stats import qmc
from random import shuffle, choice, sample, random


def melody_rules(length, max_step):
    melody = []
    #current_note = np.random.randint(60, 72) #starts at random point in the center scale
    current_note = 60
    for _ in range (length):
        next_note = current_note + np.random.choice(range(-max_step, max_step))
        next_note = max(0, min(127, next_note))
        melody.append(next_note)
        current_note = next_note
    return melody

def major_scale(length):
    scale = [60, 62, 64, 65, 67, 69, 71, 72] #central major scale
    melody = []
    for _ in range (length):
        note = np.random.choice(scale)
        melody.append(note)
    return melody

def sobol_sequence(length):
    sobol = qmc.Sobol(d=1)
    sobol_seq_values = sobol.random_base2(m=int(np.log2(length)))

    #flatten and scale the values to the range [0, 127]
    sobol_seq_values = sobol_seq_values.flatten()[:length]
    sobol_seq_scaled = sobol_seq_values * 127

    return sobol_seq_scaled