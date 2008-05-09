#! /usr/bin/env python

'''
extremely simple script to DNA transcription
'''


myDNA = 'ACGTTGCAACGTTGCAACGTTGCA'
#string buil-in replace method
myRNA = myDNA.replace('T', 'U')
print myRNA
