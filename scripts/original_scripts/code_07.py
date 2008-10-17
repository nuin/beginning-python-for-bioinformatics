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
totalA = 0
totalC = 0
totalG = 0
totalT = 0

#checking each item in the list and updating counts	
for base in seqlist:
    if base == 'A':
        totalA += 1
    elif base == 'C':
        totalC += 1
    elif base == 'G':
        totalG += 1
    elif base == 'T':
        totalT += 1

print str(totalA) + ' As found'
print str(totalC) + ' Cs found'
print str(totalG) + ' Gs found'
print str(totalT) + ' Ts found'


