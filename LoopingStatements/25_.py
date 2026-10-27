'''
25. Count consonants in a string.
'''
str1=input("Enter the word : ").lower()

countConsonent=0
countVowels=0
for i in range(len(str1)):
    if(str1[i]=='a'or str1[i]=='e'or str1[i]=='i'or str1[i]=='o'or str1[i]=='u'):
        countVowels+=0
    elif(str1[i]==" "):
        pass
    else:
        countConsonent+=1

print(countConsonent)