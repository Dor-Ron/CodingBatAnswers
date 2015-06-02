#!/usr/bin/env python

'''
Instructions:
We want make a package of goal kilos of chocolate.
We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. 
Return -1 if it can't be done. 
'''

def make_chocolate(small, big, goal):
    big *= 5
    required = goal - big
    if big + small < goal or goal % 5 > small:
        return -1
    if required < 0:
        return required % 5
    else:
        return required
