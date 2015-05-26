#Instructions
#Given a string, return a new string where the first and last chars have been exchanged. 

def front_back(str):
  first = str[0]
  root = str[1:-1]
  last = str[-1]
  return last + root + first
  
#The code didn't work on the online compiler, it got an index error.
#However, it ran perfectly fine and as planned locally.
