#Instructions
#Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements. 


def middle_way(a, b):
  mid_one = a[len(a) / 2]
  mid_two = b[len(b) / 2]
  return [mid_one, mid_two] 
  
#Alternitavely couldve done one-liner return [a[1], b[1]]
#But I wanted a more general use functions, that could work for lengths > 3 which are odd.
#If, there is no one middle index, there are two.
