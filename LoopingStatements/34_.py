'''
34. Check whether a string is palindrome.
'''
name=input("Enter the String ")
rev=""
i=0
while(len(name)>i):
    rev=name[i] + rev
    # print(rev)
    i+=1

if(name==rev):
    print("isplindrome ")
else:
    print("not")