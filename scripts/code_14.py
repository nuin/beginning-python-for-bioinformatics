#!/usr/bin/env python

'''
a more elaborated script to generate random DNA sequences
'''

import random
import sys

def simulate_sequence(length):
    '''function the generates the simulations'''
    #list with nucleotides
    dna = ['A', 'C', 'G', 'T']
    #initializing the sequence
    sequence = ''
    #iterates over the input sequence length ...
    for i in range(length):
        #and chooses randomly the nucletides
        sequence += random.choice(dna)
    #returns simulated sequence
    return sequence

#first parameter is the number of sequences to generate
setsize = int(sys.argv[1])
#minimum and maximum sequence lengths
minlength = int(sys.argv[2])
maxlength = int(sys.argv[3])

#initializes a list to store the sequence set
sequenceset = []
for i in range(setsize):
    #generate a random integer between min and max seq lenght
    rlength = random.randint(minlength, maxlength)
    #appending to the sequence set and calling simulated sequence
    #function
    sequenceset.append(simulate_sequence(rlength))

#printing output
for sequence in sequenceset:
    print sequence
