'''
48. Check whether number is strong number.
'''
num=int(input("Enter the number : "))
temp=num
sum=0

while(temp!=0):
    last=temp%10

    fact=1
    while(last>0):
        fact*=last
        last-=1
    sum+=fact
    temp=temp//10
if(num==sum):
    print("The given number is STRONG number")
else:
    print("The given number is NOT a STRONG number")

