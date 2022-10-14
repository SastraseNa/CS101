import time
from IPython.display import clear_output

char = set('0123456789.+-/*()') #List of characters that may be used
print('Calculator Instructions/Guide:\nInput numbers and operations (+,-,*,/) in the correct order \nExample : 1+1+3')

run = True
while run:
    Equation = input('\nInput equation: \n')
    clear_output()
    if any((a not in char) for a in Equation): #Checks if there are any unauthorized characters in equation
      time.sleep(2)
      print('Equation inputted: ' + Equation)
      print('Try again!\nOnly input numbers and operations (+,-,*,/)')
    else:
      time.sleep(2)
      print('Equation inputted: ' + Equation)
      print('Result: ' + str(eval(Equation))) #Calculates equation using +,-,*,/
