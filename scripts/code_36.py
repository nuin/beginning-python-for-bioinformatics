#! /usr/bin/env python

'''
input is a GenBank file. The script searches for gene annotations, extract all lines
from the file and then parses these lines in order to extract protein sequences
Ribosomal genes and other non-coding genes are not extracted - plan to do it later
output is a fasta formatted file
'''

import sys
import fasta

class Protein:
    '''
    class that stores protein information
    '''
    def __init__(self, gi, id, sequence):
        self.gi = gi
        self.id = id
        self.sequence = sequence

def parse_entry(gene_data):
    '''
    parses the entry received from the main function
    in order to extract information as protein id
    gi, etc
    '''
    prot_id = ''
    sequence = ''
    gi_id = ''
    gene_data = gene_data.splitlines()
    for line in gene_data:
        if line.find('/product') >=0:
            prot_id = line[line.find('=') + 2:-1]
        elif line.find('protein_id') >= 0:
            prot_id += '\t' + line[line.find('=') + 2: -1]
        elif line.find('GI:') >= 0:
            gi_id = 'gi' + line[line.find('GI:')+3:-1]
        elif line.find('/translation') >= 0:
            sequence = line[line.find('=') + 2:]
            temp = gene_data.index(line)
            for i in range(temp+1, len(gene_data)):
                if gene_data[i].find('sig_peptide') >= 0:
                    break
                else:
                    sequence += gene_data[i].strip()

    return Protein(gi_id, prot_id, sequence)

#only input is a genbank file
gbfile = open(sys.argv[1])

proteins = []
index = 0
entry = ''
for line in gbfile:
    if line.find('  gene ') >= 0:
        if index >= 1:
            #parses the CDS and appends to a list
            proteins.append(parse_entry(entry))
            entry = ''
        index += 1
        entry += line
    elif line.find('ORIGIN') >= 0:
        #found the DNA sequence, we can stop now
        break
    else:
        entry += line

#parses the last entry after leaving the loop
proteins.append(parse_entry(entry))

#output
for i in proteins:
    if len(i.gi) > 2:
        print i.gi, i.id
        output = open(i.gi + '.fasta', 'w')
        output.write('>' + i.gi + '\t' + i.id + '\n')
        i.sequence = i.sequence.replace('\"', '')
        output.write(fasta.format_output(i.sequence, 80))
        print i.id
