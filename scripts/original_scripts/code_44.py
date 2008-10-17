#!/usr/bin/env python

from collections import defaultdict
import sys
import fasta

seqs = fasta.get_seqs(open(sys.argv[1]).readlines())
length = int(sys.argv[2])

quorum = defaultdict(list)

seq_number = 0
for i in seqs:
    seq_number += 1
    for n in range(len(i.sequence) - int(length)):
        if not seq_number in quorum[i.sequence[n : n + length]]:
            quorum[i.sequence[n : n + length]].append(seq_number)

for i in quorum:
    print ''.join(i).upper(), len(quorum[i])
