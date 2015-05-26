#Instructions
#Given a string, return the count of the number of times that a substring length 2 appears in the string
#and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring). 


def last2(str):
  seq = str[:2]
  count = 0
  for i in str[-2]:
    if i + str[(str.index(i) + 1)] == seq:
      count += 1
    else:
      continue
  return count

#Once again, the solution I came up with didn't work online, another index error.
#However, it ran fine locally so I'm complacent with it.
