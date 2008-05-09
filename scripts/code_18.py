#!/usr/bin/env python

'''
translating DNA into proteins
'''

#import our homemade module that has the DNA
#translating function
import dnatranslate

#OK, we are using the same DNA file
dnafile = open("AY162388.seq", 'r').readlines()

#opening the file and stripping and joining the lines
sequence = ''
for line in dnafile:
    sequence += line.strip()

#call the function in our module and translating the sequence
protein = dnatranslate.translate_dna(sequence)

#output, simple, we could make it better
print sequence, len(sequence)
print
print protein, len(protein)

