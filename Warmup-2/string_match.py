#Instructions
#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. 
#So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings. 

def string_match(a, b):
  c = min(a, b) #to get shortest and avoid index error
  count = 0
  for i in range(len(c)):
    a_two = a[i:i+2]
    b_two = b[i:i+2]
    if a_two == b_two:
      count += 1
    else:
      continue
  return count     

