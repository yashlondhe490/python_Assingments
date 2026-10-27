'''
42. Write a program to perform calculator operations using match case.
'''
print("-------Weclome to Calculator---------")

print()

num1=int(input("Enter num1 :"))
num2=int(input("Enter num1 :"))

print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print()
op=int(input("Enter your option : "))

match(op):
    case 1:
         ans=num1+num2
    case 2:
             ans=num1-num2
    case 3:
             ans=num1*num2
    case 4:
             ans=num1/num2
    case _:
              print("Envalid option ")
print("ans=",ans)