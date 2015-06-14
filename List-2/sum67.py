#!/usr/bin/env python

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
