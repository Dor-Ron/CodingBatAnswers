#Instructions
#Given a string, return the string made of its first two chars, 
#so the String "Hello" yields "He". If the string is shorter than length 2, 
#return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "". 

#original solution
def first_two(str):
  if len(str) < 2:
    return str
  else:
    return str[:2]

#one liner
def first_two(str):
  return str if len(str) < 2 else str[:2]
