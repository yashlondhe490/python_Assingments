'''
38. Find smallest digit in a number.
'''
num= int(input("Enter the number "))
small=9
while(num!=0):
    lastDigit=num%10
    if(small >= lastDigit):
        small=lastDigit

    num=num//10
    
print(small)

