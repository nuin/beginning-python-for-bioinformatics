#!/usr/bin/env python

'''
another script to find motifs on DNA sequences with more features than
code_05.py
'''

# we use the RegEx module
import re
import string
#we also import the sys module
import sys

#set the variable to control the loop
fileinput = True
while fileinput == True:
    #ask user for the input
    filename = raw_input('Enter file name:')
    if len(filename) > 0:
        #we try to open the file
        try:
            dnafile = open(filename, 'r')
            #success! we finish the loop and move to the next input
            fileinput = False
        except:
            #no dice, file does not exist
            #keep the loop on and ask again
            print 'File does not exist'
    else:
#        fileinput = False
        sys.exit()


#opening the file, reading the sequence and storing in a list
seqlist = open(filename, 'r').readlines()

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
    inmotif = raw_input('Enter motif to search: ')
    #now we check for the size of the input
    if len(inmotif) >= 1:
        #we compile a regex with the input given
        motif = re.compile('%s' % inmotif)
        #looking to see if the entered motif is in the sequence
        if re.search(motif, sequence):
            print 'Yep, I found it'
        else:
            print 'Sorry, try another one'
    else:
        print 'Done, thanks for using motif_search'
        inputfromuser = False
