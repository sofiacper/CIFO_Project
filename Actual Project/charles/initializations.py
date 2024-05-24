import numpy as np
from random import shuffle, choice, sample, random

def melody_rules(length):
    melody = []
    current_note = 60 #starting in the central C
    for _ in range (length):
        next_note = current_note + np.random.choice([-2, -1, 0, 1, 2])
        next_note = max(0, min(127, next_note))
        melody.append(next_note)
        current_note = next_note
    return melody
