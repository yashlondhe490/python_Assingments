#21. Write a program to find the smallest of three numbers

num1 = int(input("Enter the number1 : "))
num2 = int(input("Enter the number2 : "))
num3= int(input("Enter the number2 : "))
small= num1
if(num1<num2 and num1<num3):
    small=num1
elif(num2<num3 and num2<num1 ):
    small=num2
else:
    small=num3
print(small)