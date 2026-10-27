'''
34. Write a program to check whether a year is a leap year and century year.
'''
year = int(input("Enter a year: "))

# Leap year check
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

# Century year check
if year % 100 == 0:
    print(year, "is a century year")
else:
    print(year, "is not a century year")