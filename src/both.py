def both(number1, number2):
  # Type your code
  if number1>0 and number2>0 :
    return True
  elif number1<0 and number2<0:
    return True
  elif number1==0 and number2==0:
    return True
  else:
    return False

#test
#print(both(1,0))