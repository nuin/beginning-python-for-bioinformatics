import sys

gbfile = open(sys.argv[1], 'r').readlines()

locus = ''
organism = ''
accession = ''
for line in gbfile:
    if line.find('LOCUS') >= 0:
        locus = line
    elif line.find('ACCESSION') >= 0:
        accession = line
    elif line.find('ORGANISM') >= 0:
        organism = line

print locus.strip()
print organism.strip()
print accession.strip()