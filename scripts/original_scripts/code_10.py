#! /usr/bin/env python

'''
Python functions
'''

def add_tail(seq):
    '''function that adds a poly-T tail to sequences'''
    result = seq + 'TTTTTTTTTTTTTTTTTTTTT'
    return result

#opening the file
dnafile = 'AY162388.seq'
file = open(dnafile, 'r')

#reading the sequence from the file
sequence = ''
for line in file:
    sequence += line.strip()

#printing result
print sequence
#calling the function to add the tail
sequence = add_tail(sequence)
#printing new sequence
print sequence
