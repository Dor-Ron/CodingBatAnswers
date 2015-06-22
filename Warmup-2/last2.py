#Instructions
#Given a string, return the count of the number of times that a substring length 2 appears in the string
#and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring). 

#original solution
def last2(str):
  count = 0
  for two in range(len(str) - 2):
    if str[two: two + 2] == str[-2:]:
      count += 1
  return count


