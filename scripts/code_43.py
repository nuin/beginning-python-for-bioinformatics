#!/usr/bin/env python

from collections import defaultdict
import sys
import fasta

seqs = fasta.get_seqs(open(sys.argv[1]).readlines())
length = int(sys.argv[2])

#for a missing key, the dict entry is initialized to zero
counts = defaultdict(int)

#count the length-element subsequences in each sequence
for i in seqs:
	for n in range(len(i.sequence) - length):
		counts[i.sequence[n : n + length]] += 1

#counts.keys() will then return the nucleotide sequences
#that were actually in merged_seqs

#print out the sequences that occur more than once
for count in counts:
        print ''.join(count), counts[count]
