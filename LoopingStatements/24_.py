'''
24. Count vowels in a string.
'''
str1=input("Enter the word : ").lower()

countVowel=0
for i in range(len(str1)):
    if(str1[i]=='a'or str1[i]=='e'or str1[i]=='i'or str1[i]=='o'or str1[i]=='u'):
        countVowel+=1
    

print(countVowel)