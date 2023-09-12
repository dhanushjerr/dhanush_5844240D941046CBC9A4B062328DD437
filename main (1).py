#leap year.

def isLeapyear (year):
  if (year% 4 == 0 and year % 100 !=or year % 400 == 0:
     return True
   else:
     return False


year = int(input("Enter a year: ")) if isLeapyear (year):

   print(') is aleapyear.'.format(year)) 13 else:

 print('{} is not a leap year .'.format(year))