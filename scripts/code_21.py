#!/usr/bin/env python

#import two modules
import dnatranslate
import fasta
import sys


#read the fasta file in one line: open the file, read the contents
#and send it to the fasta reading function
dna = fasta.read_fasta(open(sys.argv[1], 'r').readlines())

for item in dna:
    #translate the DNA
    protein = dnatranslate.translate_dna(item.sequence)
    print item.name
    #format and print the protein
    print fasta.format_output(protein, 60)