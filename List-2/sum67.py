#!/usr/bin/env python

'''
Instructions:
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
and extending to the next 7 (every 6 will be followed by at least one 7).
Return 0 for no numbers. 
'''

def sum67(nums):
  for k in xrange(len(nums)):
    if nums[k] == 6:
      nums[k] = 0
      for q in xrange(k + 1, len(nums)):
        temp = nums[q]
        nums[q] = 0
        if temp == 7:
          k = q + 1
          break
  return sum(nums)
