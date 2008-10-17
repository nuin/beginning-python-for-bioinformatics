#!/usr/bin/env python

'''
an extremely simple dice game
'''

#we need the random module
import random
import string

#generating two dices, between 1 and 6 for the human player
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

#generating two dices, between 1 and 6 for the computer player
computerdice1 = random.randint(1, 6)
computerdice2 = random.randint(1, 6)

#summing up both dices for each player
mine = dice1 + dice2
his_hers = computerdice1 + computerdice2

#printing the values
print 'mine = ' + str(mine) + ' vs. computer = ' + str(his_hers)

#chdking the results and proclaiming the winner
if mine > his_hers:
    print "I won"
elif mine < his_hers:
    print "Computer won"
else:
    print "Tie. Try again"


