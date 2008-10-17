#!/usr/bin/env python

import sys
import fasta

file = sys.argv[1]
temp = file.split('.')
filename = temp[0]
tag = temp[1]

sequences = fasta.read_fasta(open(file, 'r').readlines())

count = 1
for i in sequences:
    output = open(filename+'_'+str(count)+'.'+tag, 'w')
    output.write(i.name+'\n')
    output.write(i.sequence)
    count += 1