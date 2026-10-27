'''
41. Print numbers which are perfect cubes between 1 and 100
'''

num=1
print("The perfect Qubes betwwenn 1 to 100 are :")
while(num<=100):
    i=1
    while(i*i*i<=num):
        if(i*i*i==num):
            print(i,":",num, end=" , ")
        i+=1

    num+=1
