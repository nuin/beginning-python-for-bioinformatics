#!/usr/bin/env python

'''
using the fasta module to read sequences
'''

#import our freshly created module
import fasta
import sys

#read the fasta file in one line: open the file, read the contents
#and send it to the fasta reading function
sequences = fasta.read_fasta(open(sys.argv[1], 'r').readlines())

temp = []
for i in sequences:
    #print the sequence name
    print i.name
    #use range with a step of 80, printing 80 characters at
    #a time. The value could be set by a input parameter
    for j in range(0,len(i.sequence),80):
        print i.sequence[j:j+80]
