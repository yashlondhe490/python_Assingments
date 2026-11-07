'''
23. Check whether a string is a palindrome.

'''


str1=input("Enter the string ")

rev=str1[::-1]

if(str1==rev):
    print("Palindrome")
else:
    print("Not an palindrome")