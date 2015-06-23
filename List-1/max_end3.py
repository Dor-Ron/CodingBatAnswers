#Instructions
#Given an array of ints length 3, figure out which is larger between the first and last elements in the array, 
#and set all the other elements to be that value. Return the changed array. 

#original solution
def max_end3(nums):
  largest = max(nums[0], nums[-1])
  return [largest, largest, largest]

#one-liner
def max_end3(nums):
  return [max(nums[0], nums[-1]) for i in xrange(3)]
