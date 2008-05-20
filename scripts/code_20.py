#!/usr/bin/env python

'''
simple to translate dna into proteins
'''

#importing the dnatranslate module
import dnatranslate
import sys
import fasta

#opening and reading the file in one take
dna = fasta.read_fasta(open(sys.argv[1], 'r').readlines())

#iterate over the sequences and translate them
for item in dna:
    protein = dnatranslate.translate_dna(item.sequence)
    print item.name
    print protein