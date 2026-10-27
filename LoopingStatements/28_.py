'''

28. Check whether a number is Armstrong.
'''
num=int(input("Enter the number :"))

# conting the digits length for detecting power
def lenthDigit():
    dup=num
    count=0
    while(dup!=0):
        dup=dup//10
        count+=1
    return count

power=lenthDigit()
print(power)
dup=num
op=0
while dup!=0:
    last=dup%10
    op+=last**power
    dup=dup//10
if(num==op):
    print("Armstrong ")
else:
    print("not")




