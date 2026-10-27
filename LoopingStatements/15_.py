'''
15. Find sum of digits of a number.

'''

num=int(input("enter the number : "))
total=0
while(num!=0):
    last=num %10
    total+=last
    num= num//10

print(total)
