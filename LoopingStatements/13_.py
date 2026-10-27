'''
13. Check whether a number is palindrome.
'''
num = int(input("Enter digits: "))#123
dup=num
rev=0
while(dup!=0):                
    digit= dup %10            
    rev=(rev*10)+digit       
    dup=dup//10               
print(rev)
if(num==rev):
    print(num," : Is palindrome ")
else:
    print(num," : Not a palindrome ")