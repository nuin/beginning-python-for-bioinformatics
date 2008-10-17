#!/usr/bin/env python

import dnatranslate

dnafile = open("AY162388.seq", 'r').readlines()

sequence = ''
for line in dnafile:
    sequence += line.strip()


protein = dnatranslate.translate_dna(sequence)

print sequence, len(sequence)
print
print protein, len(protein)

