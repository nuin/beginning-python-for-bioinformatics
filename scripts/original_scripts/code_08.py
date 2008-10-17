#!/usr/bin/env python

'''script that counts the number of bases in a DNA sequence
showing the string.count() method'''

#still keep the file fixed
dnafile = "AY162388.seq"

#opening the file, reading the sequence and storing in a list
seqlist = open(dnafile, 'r').readlines()

#let's join the the lines in a temporary string
temp = ''.join(seqlist)

#counting
totalA = temp.count('A')
totalC = temp.count('C')
totalG = temp.count('G')
totalT = temp.count('T')

#printing results
print str(totalA) + ' As found'
print str(totalC) + ' Cs found'
print str(totalG) + ' Gs found'
print str(totalT) + ' Ts found'

