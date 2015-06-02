#!/usr/bin/env python

'''
Instructions:

Return the number of times that the string "code" appears anywhere in the given string,
except we'll accept any letter for the 'd', so "cope" and "cooe" count.
'''

def count_code(str):
  permutations = []
  count = 0
  for letter in "abcdefghijklmnopqrstuvwxyz":
    permutations.append("co" + letter + "e")
  for k in permutations:
      count += str.count(k) 
  return count
