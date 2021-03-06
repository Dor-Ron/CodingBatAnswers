#Instructions
#You are driving a little too fast, and a police officer stops you. 
#Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. 
#If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
#If speed is 81 or more, the result is 2.
#Unless it is your birthday -- on that day, your speed can be 5 higher in all cases. 

#original solution
def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <= 65:
      return 0
    elif speed in xrange(66, 86):
      return 1
    else:
      return 2
  else:
    if speed <= 60:
      return 0
    elif speed in xrange(61, 81):
      return 1
    else:
      return 2
      
#one-liner
def caught_speeding(speed, is_birthday):
  return 0 if is_birthday and speed <= 65 or not is_birthday and speed <= 60 else 1 if is_birthday and speed in xrange(66, 86) or not is_birthday and speed in xrange(61, 81) else 2 
