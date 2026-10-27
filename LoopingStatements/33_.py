'''
33. Print reverse of a string.
'''

name=input("Enter the string :")

for i in range(len(name)-1,-1,-1):
    print(name[i],end=" ")