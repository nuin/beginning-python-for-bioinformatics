#!/usr/bin/env python

'''
script that counts the number of each nucleotide in a sequence using 
user input and saving to a file.
'''

import sys
import re


fileentered = True #flag that determines if a filename has been entered

while fileentered == True:
    #ask the user to input a filename
    filename = raw_input('Please enter a file to check: ')
    #if a filename was entered, go ...
    if len(filename) >= 1:
        try:
            #open the file
            seqlist = open(filename, 'r').readlines()
            #sequence is read as a list, convert to string
            sequence = ''.join(seqlist)
            #remove carriage returns
            sequence = sequence.replace('\n', '')
            #counting
            total_a = sequence.count('A')
            total_c = sequence.count('C')
            total_g = sequence.count('G')
            total_t = sequence.count('T')
            #create a regex object with non-nucleotide letters to check for "errors"
            otherletter = re.compile('[BDEFHIJKLMNOPQRSUVXZ]+')
            #find possible non-nucleotides
            extra = re.findall(otherletter, sequence)
            #open an output filename to output counts
            output = open(filename + '.count', 'w')
            #writing the output
            output.write('Count report for file ' + filename + '\n')
            output.write('A = ' + str(total_a) + '\n')
            output.write('C = ' + str(total_c) + '\n')
            output.write('G = ' + str(total_g) + '\n')
            output.write('T = ' + str(total_t) + '\n')
            #if there are non-nucleotides in the sequence, report them
            if len(extra) > 0:
                output.write('Also were found ' + str(len(extra)) + ' errors\n')
                for i in extra:
                    output.write(i + ' ')
            else:
                output.write('No error found')
            print 'Result file saved on ' + filename + '.count'
        except:
            print 'File not found. Please try again.'
    else:
        #if no filename entered, exit
        fileentered = False
        sys.exit()
