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
total_a = temp.count('A')
total_c = temp.count('C')
total_g = temp.count('G')
total_t = temp.count('T')

#printing results
print str(total_a) + ' As found'
print str(total_c) + ' Cs found'
print str(total_g) + ' Gs found'
print str(total_t) + ' Ts found'

