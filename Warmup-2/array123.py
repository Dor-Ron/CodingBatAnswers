#Instructions
#Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere. 


def array123(nums):
  a,b,c = 1,2,3
  if a and b and c in nums:
    return True
  else:
    return False
