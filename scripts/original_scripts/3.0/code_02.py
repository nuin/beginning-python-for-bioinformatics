#! /usr/bin/env python

'''second script available, shows a simple way to concatenate
two DNA sequences, strings'''

myDNA = "ACGTACGTACGTACGTACGTACGT"
myDNA2 = "TCGATCGATCGATCGATCGA"
print("First and Second sequences")
print(myDNA, myDNA2)
myDNA3 = myDNA + myDNA2
print("Concatenated sequence")
print(myDNA3)