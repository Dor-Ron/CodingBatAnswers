#Instructions
#Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
#return a string of the form "7:00" indicating when the alarm clock should ring. 
#Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
#Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off". 

#original solution
def alarm_clock(day, vacation):
  if vacation:
    if day in range(1, 6):
      return "10:00"
    else:
      return 'off'
  else:
    if day in xrange(1, 6):
      return '7:00'
    else:
      return '10:00'
  
#one-liner
def alarm_clock(day, vacation):
  return "7:00" if not vacation and day in xrange(1, 6) else "10:00" if not vacation and day in [0, 6] or vacation and day in xrange(1, 6) else "off"
