#!/usr/bin/env python

'''
Instructions:
Given a string, return a string where for every char in the original,
there are two chars.
'''

def double_char(str):
  string = ""
  for char in str:
    string += char * 2
  return string
  
  
#one-liner
def double_char(str):
  return "".join([char * 2 for char in str])
