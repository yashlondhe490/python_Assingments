'''
22. Find sum of even digits in a number.
'''
num=int(input("enter the number : "))
total=0
while(num!=0):
    last=num %10
    if(last%2==0):
        total+=last
        
        
    num= num//10

print("Total of odd digits: ",total)
