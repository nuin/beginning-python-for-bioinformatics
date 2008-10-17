#!/usr/bin/env python

import random
import sys

def simulate_sequence(length):
    dna = ['A', 'C', 'G', 'T']
    sequence = ''
    for i in range(length):
        sequence += random.choice(dna)
    return sequence

setsize = int(sys.argv[1])
minlength = int(sys.argv[2])
maxlength = int(sys.argv[3])
nsets = int(sys.argv[4])

for i in range(nsets):
    sequenceset = []
    for i in range(setsize):
        rlength = random.randint(minlength, maxlength)
        sequenceset.append(simulate_sequence(rlength))

    for sequence in sequenceset:
        print sequence

    print
