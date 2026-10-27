'''

47. Find product of digits of a number.
'''
num=int(input("Enter the digit : "))
pro=1
while(num!=0):
    last=num%10
    pro*=last
    num=num//10
print(pro)