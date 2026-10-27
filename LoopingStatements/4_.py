'''
4. Print all odd numbers between 1 and 50.
'''
i = 0 

print("odd numbers form 1 to 50 are : ")
for i in range(1,51,1):
    if(i % 2!=0):
        print(i , end=",")
