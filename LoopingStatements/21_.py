'''
21. Print pattern of numbers.

'''

num=5
cont=1
for i in range (1,num+1):

    for j in range(i):
        print(cont,end=" ")
        cont+=1
    print()

