# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer
age = ''
while age.isdigit() == False:
  age = input('Enter a dog\'s age in human years: ')

age = int(age)

def dog_years(dog_age):
  acc = 0
  total = 0
  for i in range(dog_age):
    acc += 1
    if acc in [1,2]:
      total += 10
    else:
      total += 7
  return total

print(f'The dog\'s age in dog years is {dog_years(age)}')