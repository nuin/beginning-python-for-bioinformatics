#! /usr/bin/env python

'''
reading a sequence file and printing first and last lines
'''

dnafile = "AY162388.seq"
file = open(dnafile, 'r').readlines()
print 'I want the first line'
print file[0]
print 'now the last line'
#print file[len(file)-1]
print file[-1]
