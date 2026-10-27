'''
18. Print prime numbers between 1 and 50.

'''
 
num=1
for num in range(1,50+1):
    count=0
    for i in range(1,50+1):
        if(num %i ==0):
            count+=1
    
    if(count==2):
        print(num)