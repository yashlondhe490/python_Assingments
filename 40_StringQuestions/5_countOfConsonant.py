'''
5. Count the number of consonants in a string.

'''

str1=input("Enter the String :")
vovel_count=0
for i in str1:
    if(i not in "aeiouAEIOU"):
        vovel_count+=1
print("Total consonant count is :",vovel_count)

