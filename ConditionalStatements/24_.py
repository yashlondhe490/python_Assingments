'''
24. Write a program to check exam results (Distinction, First Class, Pass, Fail).
'''

print("Enter subject marks outof 100")
print()

num1 = int(input("Enter the marks of 'MARATHI': "))
num2 = int(input("Enter the marks of 'ENGLISH': "))
num3 = int(input("Enter the marks of 'MATHS': "))
num4 = int(input("Enter the marks of 'SCIENCE: ' "))
num5 = int(input("Enter the marks of 'HISTORY': "))
num6 = int(input("Enter the marks of 'GEOGRAPHY': "))

total=num1+num2+num3+num4+num5+num6;
per=int((total/600)*100);

if(per>80 and per<100):
    print(per,"Distinction")
elif(per>60 and per<80):
    print(per,"First-class")
elif(per>40 and per<60):
    print(per,"Pass")
else:
    print(per,"fail")
