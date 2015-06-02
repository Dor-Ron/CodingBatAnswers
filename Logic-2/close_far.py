#!/usr/bin/env python

'''
Instructions:
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1),
while the other is "far", differing from both other values by 2 or more.
Note: abs(num) computes the absolute value of a number. 
'''

def close_far(a, b, c):
  if (a == b or a == c or b == c) and (abs(a - c) >= 2 or abs(a - b) >= 2 or abs(b - c) >= 2):
    return True
  if max(a, b, c) - min(a, b, c) <= 2:
    return False
  else:
    return True

