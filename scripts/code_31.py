#! /usr/bin/env python

import sys

file = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

size = 0
segment = ''
for line in open(file, 'r'):
    if not line.startswith('>'):
       size += len(line)
    else:
        name = line
    if size >= start and size <= end:
        segment += line

print name, segment
