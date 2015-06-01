#!/usr/bin/env python

'''
Instructions:
Given 3 int values, a b c, return their sum.
However, if one of the values is the same as another of the values,
it does not count towards the sum. 
'''

def lone_sum(a, b, c):
  if a == b == c:
    return 0
  elif b == c:
    return a
  elif a == b:
    return c
  elif a == c:
    return b
  else:
    return a + b + c  
