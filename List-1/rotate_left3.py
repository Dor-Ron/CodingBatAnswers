#Instructions
#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}. 


def rotate_left3(nums):
  first = nums[0]
  nums.remove(first)
  nums.insert(2, first)
  return nums
