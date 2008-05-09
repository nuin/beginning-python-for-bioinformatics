#!/usr/bin/env python

'''
making a function to count nucleotides
'''

import sys

def count_nucleotide_types(seq):
    '''counting nucleotides and returning a list with counts'''
    result = []
    totalA = seq.count('A')
    totalC = seq.count('C')
    totalG = seq.count('G')
    totalT = seq.count('T')

    result.append(totalA)
    result.append(totalC)
    result.append(totalG)
    result.append(totalT)

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
