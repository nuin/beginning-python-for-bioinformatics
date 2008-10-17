import sys
import re
import fasta

#function that reads the enzyme list
def read_enzymes(file):
    #initialize dictionary
    resenz = {}
    start = False
    for line in file:
        #if we found the string we jump a line and start reading the list
        if line.find('Rich Roberts') >= 0:
            start = True
            line = file.next()
        if start == True and len(line) > 10:
            buffer = line.split()
            #populating the dictionary
            resenz[buffer[0]] = buffer[-1].replace('^', '')
    return resenz

#function that checks if the input enzyme name was found in the list
def check_enzyme(input, set):
    if set.has_key(input):
        return True
    else:
        return False

def find_sites(input, set, sequence):
    #this is the IUPAC code
    iupacdict = {'A':'[A]',
    'C':'[C]',
    'G':'[G]',
    'T':'[T]',
    'M':'[AC]',
    'R':'[AG]',
    'W':'[AT]',
    'S':'[CG]',
    'Y':'[CT]',
    'K':'[GT]',
    'V':'[ACG]',
    'H':'[ACT]',
    'D':'[AGT]',
    'B':'[CGT]',
    'X':'[ACGT]',
    'N':'[ACGT]'}

    #we get the site
    site = set[input]
    pattern = ''
    positions = []
    #transform the site from IUPAC to nucleotides
    for i in site:
        pattern += iupacdict[i]
    #search the pattern
    searchpattern = re.compile(pattern)
    #search all entries of the pattern
    sites = searchpattern.findall(sequence)
    temppos = searchpattern.finditer(sequence)
    for i in temppos:
        begin, end = i.span()
        positions.append(begin)

    return sites, positions

#read the enzyme name
enzyme = sys.argv[1]
#read the list
enzymeset = read_enzymes(open('bionet.709', 'r'))
isname = check_enzyme(enzyme, enzymeset)

if isname:
    print 'Name found'
    #if we found the enzyme name we read the sequence file
    sequences = fasta.read_fasta(open(sys.argv[2], 'r').readlines())
    for item in sequences:
        #let's search
        sites, positions = find_sites(enzyme, enzymeset, item.sequence)
        #print the sequence name
        print item.name[:20]+'...'
        #and use the zip function to combine the lists and print
        for i in zip(sites,positions):
            print i[0], '->', i[1]
#if the name is not found, we bail out
else:
    print 'Enzyme name not found, please try again'
