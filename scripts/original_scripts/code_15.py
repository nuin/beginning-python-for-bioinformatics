#!/usr/bin/env python

'''
a even more elaborated DNA sequence simulation script with
sequence identity calculation (not overall, just neighbours)
'''

import random
import sys

def simulate_sequence(length):
    '''function that simulates the sequences'''
    #nucleotides list
    dna = ['A', 'C', 'G', 'T']
    sequence = ''
    #randomly picking from the nucleotide list
    for i in range(length):
        sequence += random.choice(dna)
    return sequence

def nucleotide_percentage(sequence):
    #counting the nucleotides
    print str(sequence.count('A')) + ' As ',
    print str(sequence.count('C')) + ' Cs ',
    print str(sequence.count('G')) + ' Gs ',
    print str(sequence.count('T')) + ' Ts '

def sequence_identity(seqset):
    '''function that calculates sequence identies'''
    iden = []
    count = 0.0
    #iterates through the sequences in the set -1
    #and calculates sequence identities
    for x in range(len(seqset) - 1):
	print str(x), str(x+1)
        for n in range(len(seqset[x])):
            #iterates over all nucleotides and checks for identical ones
            if seqset[x][n] == seqset[x + 1][n]:
                count += 1
        iden.append(count / len(seqset[x]))
        count = 0.0
    return iden

#input parameters
setsize = int(sys.argv[1])
minlength = int(sys.argv[2])
maxlength = int(sys.argv[3])

#generates simulated sequence sets
sequenceset = []
for i in range(setsize):
    rlength = random.randint(minlength, maxlength)
    sequenceset.append(simulate_sequence(rlength))

#calculate sequence identities
identity = sequence_identity(sequenceset)

#prints the results
for i in range(len(sequenceset)):
    print sequenceset[i]
    if i < len(sequenceset) - 1:
        print 'sequence identity to next sequence : ' + str(identity[i])
    nucleotide_percentage(sequenceset[i])
    print
