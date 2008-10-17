import fasta
import sys

def permutations(items, n):
    if n == 0:
        yield ''
    else:
        for i in range(len(items)):
            for base in permutations(items, n - 1):
                yield str(items[i]) + str(base)

seqs = fasta.get_seqs(open(sys.argv[1]).readlines())
length = sys.argv[2]

nucleotides = ['A', 'C', 'G', 'T']

merged_seqs = ''
for i in seqs:
    merged_seqs += i.sequence

for i in permutations(nucleotides, int(length)):
    print i + '\t' + merged_seqs.count(i)
