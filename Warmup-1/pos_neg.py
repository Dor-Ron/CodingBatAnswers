#Instructions
#Given 2 int values, return True if one is negative and one is positive. 
#Except if the parameter "negative" is True, then return True only if both are negative. 

#original solution
def pos_neg(a, b, negative):
  if (negative != True) and (a < 0 and b > 0):
    return True
  elif (negative != True) and (a > 0 and b < 0):
    return True
  elif (negative == True) and (a < 0 and b < 0):
    return True
  elif (negative == False) and (a < 0 and b < 0):
    return False
  else:
    return False
    
#one-liner
def pos_neg(a, b, negative):
  return True if not negative and (a < 0 and b > 0) or not negative and (a > 0 and b < 0) or negative and (a < 0 and b < 0) else False
