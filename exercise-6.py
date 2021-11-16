# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
month = ''
day = ''
while month not in months:
  month = input('Enter the month of the year (Jan - Dec): ').lower()
while day.isdigit() == False or int(day) >= 31:
  day = input('Enter the day of the month: ')

day = int(day)

if month in months[0:2]:
  if month == 'Mar' and date > 19:
    season = 'Spring'
  else:
    season = 'Winter'
elif month in months[3:5]:
  if month == 'Jun' and date > 20:
    season = 'Spring'
  else:
    season = 'Summer'
elif month in months[6:8]:
  if month == 'Sep' and date > 21:
    season = 'Fall'
  else:
    season = 'Summer'
elif month == 'Dec' and date > 20:
  season = 'Winter'
else:
  season = 'Fall'

print(f'{month.capitalize()} {day} is in {season}')
