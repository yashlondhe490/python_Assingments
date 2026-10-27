'''
30. Write a program to check the type of number (single, double, or three digit).
'''
num = int(input("Enter a number: "))

    

if num < 10:
    print("Single digit number")
elif num < 100:
    print("Double digit number")
elif num < 1000:
    print("Three digit number")
else:
    print("More than three digits")