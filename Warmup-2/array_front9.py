#Instructions
#Given an array of ints, return True if one of the first 4 elements in the array is a 9. 
#The array length may be less than 4. 

#original solution
def array_front9(nums):
  if 9 in nums[:4]:
    return True
  else:
    return False
  
#One-liner
def array_front9(nums):
  return 9 in nums[:4]
