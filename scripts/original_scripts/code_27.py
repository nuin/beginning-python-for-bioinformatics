#!/usr/bin/env python

import sys
import fasta

file = sys.argv[1]
temp = file.split('.')
filename_base = temp[0]
tag = temp[1]

sequences = fasta.read_fasta(open(file, 'r').readlines())

count = 1
for i in sequences:
    f = filename_base + '_' + str(count) + '.' + tag
    output = open(f, 'w')
    output.write(i.name + '\n')
    output.write(i.sequence)
    count += 1
