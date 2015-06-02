#!/usr/bin/env python

'''
Instructions:
We want to make a row of bricks that is goal inches long. We have a number of small bricks
(1 inch each) and big bricks (5 inches each).
 Return True if it is possible to make the goal by choosing from the given bricks.
This is a little harder than it looks and can be done without any loops.
'''

def make_bricks(small, big, goal):
    for five in range(0, (big * 5) + 1, 5):
        for one in range(small + 1):
            if five + one == goal:
                return True
                break
    return False


#test cases
print make_bricks(3, 1, 8)
print make_bricks(5, 2, 17)
print make_bricks(3, 3, 18)
print make_bricks(3, 5, 110)

#Alternative solution that works online, took me a while to get

def make_bricks(small, big, goal):
    if goal >  big * 5 + small: 
        return False
    elif goal % 5 > small:
        return False
    else:
        return True
