#! /usr/bin/env python

import sys

file = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

size = 0
linesize = 0
segment = []
for line in open(file, 'r'):
    if not line.startswith('>'):
        size += len(line)
    else:
        name = line
        if size >= start and size <= end+linesize:
            segment.append(line.strip())
            linesize = len(line.strip())

startline = (start / linesize) + 1
endline = (end / linesize) + 1

if not start % linesize == 0 and not end % linesize == 0:
    segment[0] = segment[0][startline*linesize-start:]
    segment[-1] = segment[-1][endline*linesize-end:]
elif not start % linesize == 0:
    segment[0] = segment[0][startline*linesize-start:]
elif not end % linesize == 0:
    segment[-1] = segment[-1][endline*linesize-end:]

print name, '\n'.join(segment)
