'''
5. Print multiplication table of a given number.
'''
num = int(input("enter which table u want : "))
i = 1
for i in range(1,11,1):
    print(num,"*",i,"=",num*i)