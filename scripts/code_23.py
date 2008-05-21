import sys
import re

gbfile = open(sys.argv[1], 'r').readlines()

sequence = ''
issequence = False
for line in gbfile:
    if issequence == True:
        sequence += line
    elif line.find('ORIGIN') >= 0:
        issequence = True

print sequence