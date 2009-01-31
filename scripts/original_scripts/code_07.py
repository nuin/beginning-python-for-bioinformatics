#!/usr/bin/env python

'''
counting the nucleotides in a sequence, iterating
through lists
'''

#let's keep the file fixed for now
dnafile = "AY162388.seq"

#opening the file, reading the sequence and storing in a list
file = open(dnafile, 'r')

#initialize a string to receive the data
sequence = ''
for line in file:
    sequence += line.strip() #notice the strip, to remove \n

#"exploding" the sequence in a list
seqlist = list(sequence)

#initializing integers to store the counts
total_a = 0
total_c = 0
total_g = 0
total_t = 0

#checking each item in the list and updating counts	
for base in seqlist:
    if base == 'A':
        total_a += 1
    elif base == 'C':
        total_c += 1
    elif base == 'G':
        total_g += 1
    elif base == 'T':
        total_t += 1

print str(total_a) + ' As found'
print str(total_c) + ' Cs found'
print str(total_g) + ' Gs found'
print str(total_t) + ' Ts found'


