#!/usr/bin/env python

'''
making a function to count nucleotides
'''

import sys

def count_nucleotide_types(seq):
    '''counting nucleotides and returning a list with counts'''
    result = []
    total_a = seq.count('A')
    total_c = seq.count('C')
    total_g = seq.count('G')
    total_t = seq.count('T')

    result.append(total_a)
    result.append(total_c)
    result.append(total_g)
    result.append(total_t)

    return result

#opening the file
sequencefile = open(sys.argv[1], 'r').readlines()
#joining a sequence as a list into a string
sequence = ''.join(sequencefile)
#replacing carriage returns
sequence = sequence.replace('\n', '')
#counting the nucleotides
values = count_nucleotide_types(sequence)
#printing the results
print values
