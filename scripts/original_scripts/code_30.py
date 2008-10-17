#! /usr/bin/env python

import fasta
import sys

data = fasta.read_seqs(open(sys.argv[1], 'r').readlines())
print map(lambda seq:len(seq), data)
