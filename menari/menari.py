import time
import datetime
from random import randint


def exercises(rounds, correct, not_correct):
  '''This function creates an exercise and gets the user input from the console.
  
  returns -- list with the result of correct and not correct solutions
  '''
  results = []

  for x in range(0,rounds):    
    x = randint(1,50)
    y = randint(1,100)
    result = 0

    if randint(1,2) == 1:
      result = x + y
      print(str(x) + " + " + str(y) + " =")
    else:
      result = y - x
      print(str(y) + " - " + str(x) + " =")
    
    user_result = int(input('Result: '))

    if user_result == result:
      correct += 1
      print(str(user_result) + ' is correct\n')
    else:
      not_correct += 1
      print(str(user_result) + ' is not correct. The Solution is ' + str(result) + '\n')
  
  results.append(correct)
  results.append(not_correct)
  return results


def get_current_time():
  return int(round(time.time()))


def write_results(rounds, results, duration):
  '''Saves the results in a csv file.'''
  with open('data/results.csv', 'a') as file:
    file.write(str(datetime.datetime.now()))
    file.write(",")
    file.write(str(rounds))
    file.write(",")
    file.write(str(results[0]))
    file.write(",")
    file.write(str(results[1]))
    file.write(",")
    file.write(str(duration))
    file.write(",")
    file.write(str(duration/rounds) + "\n")

def main():
  '''The main()-function invokes the functions and sets a start and endpoint, 
  to see how much time the user spend with the exercises.
  Afterwards the re2sults will be appended to the data/results.csv'''
  rounds = 10
  correct = 0
  not_correct = 0
  duration = 0
  
  start = get_current_time()
  results = exercises(rounds, correct, not_correct)
  end = get_current_time()

  duration = end-start
  print('\n')
  print(str(duration) + ' Seconds')
  
  write_results(rounds, results, duration)


print('---- MENARI\n')
main()
print('\n---- MENARI')