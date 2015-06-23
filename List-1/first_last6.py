#Instructions
#Given an array of ints, return True if 6 appears as either the first or last element in the array. 
#The array will be length 1 or more. 

#original solution
def first_last6(nums):
  if nums[0] == 6 or nums[-1] == 6:
    return True
  else:
    return False

#one-liner
def first_last6(nums):
  return True if nums[0] == 6 or nums[-1] == 6 else False
