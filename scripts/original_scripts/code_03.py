#! /usr/bin/env python

'''third script, shows how to import a module and use the 
regex module to transcribe DNA to RNA
'''

#import regular expression module
import re

#setting the DNA string
dna = 'ACGTTGCAACGTTGCAACGTTGCA'

#assigning a new regex and compiling it 
#to find all Ts
regexp = re.compile('T')

#create a new string tha will receive 
#the regex result with Us replacing Ts
rna = regexp.sub('U', dna)

print rna
