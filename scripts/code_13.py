#!/usr/bin/env python

'''
very simple script to generate random DNA sequences
'''

#random module is needed
import random
import sys

#sequence length is a parameter
length = int(sys.argv[1])

#template DNA is a list with ACGT repeats
dnaseq = list('ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGT')

#print the template
print dnaseq

result = ''
for i in range(length):
    #for the simulated sequence we use random.choice
    #that randonly selects items of a list
    result += random.choice(dnaseq)

print result