'''
11. Count number of digits in a number.
'''
num = int(input("Enter digits: "))
count=0
while(num!=0):
    count+=1
    num= num//10
print(count)