#Instructions
#Given 2 ints, a and b, return their sum. 
#However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20. 

#original solution
def sorta_sum(a, b):
  if (a + b) in range(10, 20):
    return 20
  else:
    return a + b 

#one-liner
def sorta_sum(a, b):
  return 20 if (a + b) in range(10, 20) else a + b 
