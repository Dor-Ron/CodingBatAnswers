#!/usr/bin/env python

'''
Instructions:
Return the sum of the numbers in the array, returning 0 for an empty array.
Except the number 13 is very unlucky, so it does not count and numbers that
come immediately after a 13 also do not count. 
'''

def sum13(nums):
  while 13 in nums:
    if nums[-1] == 13:
      nums.append(0)
    nums[nums.index(13)+1] = 0
    nums[nums.index(13)] = 0
  return sum(nums)
