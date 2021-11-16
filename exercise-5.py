# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it

def fibonacci():
  numbers = [0, 1]
  for i in range(2,50):
    new_num = numbers[i-2] + numbers[i - 1]
    numbers.append(new_num)
  for i in range(50):
    print(f'term: {i + 1} / number: {numbers[i]}')
  
fibonacci()