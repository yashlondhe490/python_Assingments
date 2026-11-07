'''

4. Count the number of vowels in a string.
'''
str1=input("Enter the String :")
vovel_count=0
for i in str1:
    if(i in "aeiouAEIOU"):
        vovel_count+=1
print("Total vowel count is :",vovel_count)

