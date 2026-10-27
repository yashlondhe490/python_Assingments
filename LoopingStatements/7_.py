'''
7. Calculate factorial of a number using for loop.
'''
num= int(input("Enter the number : "))
fact=1
for num in range(num,num!=0,-1):
    fact= fact*num

print(fact)