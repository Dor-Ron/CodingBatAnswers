#Instructions
#Given an int n, return True if it is within 10 of 100 or 200.

#original solution
def near_hundred(n):
  if abs(n-100) <= 10 or abs(n-200) <= 10:
    return True
  else:
    return False

#one-liner
def near_hundred(n):
  return abs(n-100) <= 10 or abs(n-200) <= 10
