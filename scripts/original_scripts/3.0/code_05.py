#!/usr/bin/env python

'''
simple script to find motifs on DNA sequences using regex
the script is interactive 
'''

# we use the RegEx module
import re
import string

#still keep the file fixed
dnafile = "AY162388.seq"

#opening the file, reading the sequence and storing in a list
seqlist = open(dnafile, 'r').readlines()

#let's join the the lines in a temporary string
temp = ''.join(seqlist)

#assigning our sequence, with no carriage returns to our
#final variable/object
sequence = temp.replace('\n', '')

#we start to deal with user input
#first we use a boolean variable to check for valid input
inputfromuser = True

#while loop: while there is an motif larger than 0
#the loop continues
while inputfromuser:
    #raw_input received the user input as string
    inmotif = input('Enter motif to search: ')
    #now we check for the size of the input
    if len(inmotif) >= 1:
        #we compile a regex with the input given
        motif = re.compile('%s' % inmotif)
        #looking to see if the entered motif is in the sequence
        if re.search(motif, sequence):
            print('Yep, I found it')
        else:
            print('Sorry, try another one')
    else:
        print('Done, thanks for using motif_search')
        inputfromuser = False
