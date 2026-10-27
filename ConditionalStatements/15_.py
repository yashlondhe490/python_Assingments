'''
15. Write a program to check whether a number is divisible by both 3 and 7 or not.
'''
num = int(input("Enter the number : "))
if(num % 3==0 and num % 7==0):
    print("number is divisible by 3 & 7")
else:
    print("number is not divisible by 3 & 7")