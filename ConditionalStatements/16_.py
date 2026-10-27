'''
16. Write a program to find the greatest of three numbers.
'''
num1 = int(input("Enter the number1 : "))
num2 = int(input("Enter the number2 : "))
num3= int(input("Enter the number2 : "))
big= num1
if(num1>num2 and num1>num3):
    big=num1
elif(num2>num3 ):
    big=num2
else:
    big=num3
print(big)