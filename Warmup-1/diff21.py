#Instructions
#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21. 

#original-solution
def diff21(n):
  if n <= 21:
    return abs(n-21)
  else:
    return abs(n-21) * 2

#one-liner
def diff21(n):
  return abs(n-21) if n <= 21 else abs(n-21) * 2
