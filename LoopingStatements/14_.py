'''
14. Print Fibonacci series up to n terms.

'''
num=int(input("Enter the end value of febonacci series : "))
num1=0
num2=1
count=0
while(count!=num):
    num3=num1+num2
    print(num1,end=" ")
    num1=num2
    num2=num3
    count+=1    
