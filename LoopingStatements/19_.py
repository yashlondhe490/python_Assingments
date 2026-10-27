'''
19. Check whether a number is prime.
'''
num=int(input("Enter the number "))
j=1
count=0
for j in range(1,num+1):
    if(num%j==0):
        count+=1

if(count==2):
    print("The given number is prime")
else:
    print("Given number is not an prime Number ")