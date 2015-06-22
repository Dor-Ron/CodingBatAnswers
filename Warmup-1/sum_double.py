#Instructions
#Given two int values, return their sum. Unless the two values are the same, then return double their sum. 


#original solution
def sum_double(a, b):
  if a != b:
    return a+b
  else:
    return (a+b)*2

#one-liner
def sum_double(a, b):
  return a + b if a != b else (a + b) * 2
