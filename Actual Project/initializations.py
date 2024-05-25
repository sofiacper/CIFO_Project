import numpy as np
from random import shuffle, choice, sample, random


def melody_rules(length, max_step):
    melody = []
    current_note = np.random.randint(60, 72) #starts at random point in the center scale
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

