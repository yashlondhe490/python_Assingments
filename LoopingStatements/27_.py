'''
27. Print all factors of a number.
'''
num=int(input("Enter the number "))
j=1
for j in range(1,num+1):
    if(num%j==0):
        print(j)