import sys

gbfile = open(sys.argv[1], 'r').readlines()

sequence = ''
issequence = False
for line in gbfile:
    if issequence == True and not line.find('/') == 0:
        sequence += line.lstrip('0123456789 ').replace(' ', '')
    elif line.find('ORIGIN') >= 0:
        issequence = True

print sequence