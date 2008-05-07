#! /usr/bin/env python

'''simple script to open a file and print all lines'''

#assigning a filename to a variable
dnafile = "AY162388.seq"

#opening the file
file = open(dnafile, 'r')

#printing each line of the file
for line in file:
    print line,