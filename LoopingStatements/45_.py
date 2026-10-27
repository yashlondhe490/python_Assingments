'''

45. Print numbers skipping multiples of 3.

'''
num=int(input("Enter the End-Value : "))
i=1
while(i<=num):
    if i%3!=0:
        print(i)

    i+=1